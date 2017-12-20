[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Microsoft/cognitive-services-notebooks/master) [![AzureNB](https://notebooks.azure.com/launch.png)](https://notebooks.azure.com/import/gh/Microsoft/cognitive-services-notebooks)
# Interactive Jupyter notebooks for Microsoft Cognitive Services 
This repository contains Jupyter notebooks that illustrate various features of [Microsoft Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/). 

## How to run notebooks
* The simplest way to run the samples is via [MyBinder](https://mybinder.org) by clicking on [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Microsoft/cognitive-services-notebooks/master)
* If you have a Microsoft LiveID, you can also run the notebooks on [Azure notebooks](https://notebooks.azure.com) by clicking on [![AzureNB](https://notebooks.azure.com/launch.png)](https://notebooks.azure.com/import/gh/Microsoft/cognitive-services-notebooks).
* To run notebooks on a local Jupyter installation:
    * Clone the repo: `git clone https://github.com/Microsoft/cognitive-services-notebooks.git`
    * Go into the samples directory: `cd cognitive-services-notebooks`
    * Install the required packages: `pip install -r requirements.txt` or `conda install --file requirements.txt` 
    * Start Jupyter notebooks: `jupyter notebook`

## How to generate markdown
While you can use `jupyter nbconvert --to-markdown` to convert the notebooks to Markdown, you can also use the tool `notebook_to_markdown` in the [tools](tools) directory as follows:

``
python notebook_to_markdown.py notebook_name [--output-dir output_directory]
``

`notebook_to_markdown` generates self-contained markdown files by replacing image references with inlined base64-encoded images. Therefore, HTML output generated from the resulting markdown files are also fully self-contained.

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all others rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
