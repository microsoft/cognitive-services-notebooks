import unittest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=ImportWarning)

class NotebookTestSuite(unittest.TestCase):
    def setUp(self):
        from nbconvert.preprocessors import ExecutePreprocessor
        self.preprocessor = ExecutePreprocessor(timeout=600, enabled=True, allow_errors=False)

    @staticmethod
    def _discover_notebooks():
        import os, fnmatch
        counter = -1
        for dirpath, dirnames, filenames in os.walk("."):
            # skip checkpoint directories
            if "ipynb_checkpoints" in dirpath:
                continue
            dirnames.sort()
            filenames.sort()
            for notebook_file in fnmatch.filter(filenames, "*.ipynb"):
                counter += 1
                yield dirpath, notebook_file

    @classmethod
    def initialize_tests(cls):
        import os, re
        for dirpath, file_name in NotebookTestSuite._discover_notebooks():
            test_name = "test_" + re.sub("\\W+", "_", file_name)
            def make_test(nbfile):
                return lambda instance: instance.verify_notebook(nbfile)
            setattr(cls, test_name, make_test(os.path.join(dirpath, file_name)))

    def verify_notebook(self, nbfile):
        """
        verify_notebook: Runs a notebook and ensures that all cells execute without errors.
        """
        from nbformat import read as read_nb, NO_CONVERT
        try:
            pass
            # First newline avoids the confusing "F"/"." output of unittest
#            print("\nTesting " + nbfile)
            nb = read_nb(nbfile, NO_CONVERT)
            self.preprocessor.preprocess(nb, {})
        except Exception as err:
            self.fail(err)


if __name__ == "__main__":    
    NotebookTestSuite.initialize_tests()
    unittest.main()
