## Thanks for using [quick-doc-py](https://pypi.org/project/quick-doc-py). If you like this project, you can support it on [ko-fi](https://ko-fi.com/draggamestudio). Your support helps improve the project and add new features. Thank you!
Quick-doc-py is a Python library that automates the documentation generation for any project or code. This tool is designed to make the process of creating project documentation simple and efficient. It can create Markdown documentation, which is easy to read and can be easily converted to other formats (like HTML) if needed.

Features:
- Generate documentation for code files
- Supports multiple languages (English, Russian, Ukrainian, Chinese, Spanish, Polish)
- Integration of gpt-4 and gpt-3.5-turbo for better code explanation
- Simple command line interface

Structure:
Quick-doc-py consists of multiple Python modules. The main `quick_doc_py` directory contains:

- `config.py`: It includes configuration settings, language-to-index mapping, and lists of ignored files.
- `log_logic/req.py`: Contains the `ReqToServer` class that is responsible for interactions and data exchange with the server (if needed).
- `utilities.py`: Contains utility classes and decorators, such as `ProgressBar`, `TimeManager`, and so on.
- `main.py`: It is the entry point of the application, including classes like `ReqHendler`, `GptHandler`, `AnswerHandler`, and `AutoDock`.
- `providers_test.py`: It includes the `ProviderTest` class which is used to test the compatibility between gpt-4/gpt-3.5-turbo and different providers.

Usage:
To generate project documentation, you need to do the following steps:

1. Install quick-doc-py via pip:
```
pip install quick-doc-py
```

2. Run the command, specifying required arguments. You can see a configurable example below:
```
python -m quick_doc_py \
  --name_project "My Project" \
  --root_dir "./my_project" \
  --ignore '["*README.md", "*__pycache__", "*dist"]' \
  --languages '[(en,), (ru,), (ua,)]' \
  --gpt_version "gpt-4" \
  --provider "Mhystical" \
  --general_prompt "Write general idea of code in Markdown (use Google Style) in en language write only about Overview, Features, Structure, Usage. Dont add ```markdown. Dont invent code talk only about that code." \
  --default_prompt "Write documentation for this file in Markdown (use Google Style) in en language. Write only about usage and describe every methods. Remember that it is not full documentation, it is just addition. Dont add ```markdown. Dont invent code talk only about that code."
```

This command will generate project documentation by using gpt-4 and the Mhystical provider. Quick-doc-py will also create separate Markdown files for each language specified.
# ./LICENSE

The `./LICENSE` file contains the MIT License for the software.

## Usage

This license file must be included with the software and its associated documentation.

## Methods

1. `Copyright` - Indicates the year(s) and copyright holder(s) of the software.
2. `Permission` - Grants users the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, as well as allowing others to do the same.
3. `Conditions` - Provides specific requirements for using and sharing the software. The copyright notice and this permission notice must be included in all copies or significant portions of the software.
4. `Disclaimer` - States that the software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement.
5. `Liability` - Indicates that, under no circumstances, shall the authors or copyright holders be liable for any claim, damages, or other liability arising from the use of the software or its derivatives.

```markdown
# Important Note
This file does not include full documentation, but an addition to it. Follow the structure and customize it to include other relevant information for the actual software. This example focuses solely on the usage and methods of the MIT License file.

# Customization
1. Replace `[2024]` with the actual year for which you are claiming copyright protection.
2. Replace `[Drag_GameStudio]` with the name of the company, group, or individual behind the software.
3. Include other required components or files, if any, in your documentation.
```
# PyProject TOML Usage Documentation

This `pyproject.toml` file is used for configuring the project with Poetry.
It specifies the package information, dependencies, and other project metadata.

## `[tool.poetry]` section

### name
The `name` field specifies the name of the package, which is "quick-doc-py" in this case.

### version
The `version` field specifies the version of the package, which is "1.1.1" in this case.

### description
The `description` field provides a brief description of the package, "This code can make documentation for your project" in this case.

### authors
The `authors` field is a list of strings that specify the authors of the package. In this case, it is set to ["Dmytro <sinica911@gmail.com>"].

### readme
The `readme` field specifies the name of the README file for the package, "README.md" in this case.

### packages
The `packages` field defines a list of packages to include in the package. Each package is specified by a dictionary with an `include` field indicating the directory containing the package.

### license
The `license` field specifies the license for the package, which is "MIT" in this case.

### repository
The `repository` field specifies the URL of the repository where the package is hosted, which is "https://github.com/Drag-GameStudio/Quick-Documentation" in this case.

### `[tool.poetry.scripts]` section

### gen-doc
The `gen-doc` field specifies a script entry point. The specified script is used for generating the documentation for your project by running `gen-doc` or `python -m quick_doc_py.main`.

### providers-test
The `providers-test` field specifies another script entry point, which can be used for testing your documentation providers. It can be run by using `providers-test` or `python -m quick_doc_py.providers_test`.

## `[tool.poetry.dependencies]` section

This section lists the dependencies of the package, including Python version and required packages such as `colorama`, `requests`, and `g4f`.

### python
The `python` field specifies the required Python version, which in this case is `^3.10` (greater than or equal to 3.10). 

### colorama
The `colorama` field specifies the required version of the `colorama` package to be `^0.4.6` (greater than or equal to 0.4.6).

### requests
The `requests` field specifies the required version of the `requests` package to be `^2.32.3` (greater than or equal to 2.32.3).

### g4f
The `g4f` field specifies the required version of the `g4f` package to be `^-4.0.0` (greater than or equal to 0.4.0.4).

## `[build-system]` section

This section specifies the requirements and build backend for the package.

### requires
The `requires` field specifies the required dependencies for building the package, which in this case is `["poetry-core"]`.

### build-backend
The `build-backend` field specifies the build backend for the package, which in this case is `"poetry.core.masonry.api"`.
}
# Quick Doc Py - Configuration

The `config.py` file contains configuration settings for the Quick Doc Py project. Below you will find a description of each method and usage instruction:

## Variables

### LANGUAGE_TYPE

A dictionary that maps language codes to their respective integer indices. Currently, it supports the following languages:

```python
LANGUAGE_TYPE = {
    "en": 0,  # English
    "ru": 1,  # Russian
    "ua": 2,  # Ukrainian
    "chs": 3, # Chinese
    "es": 4,  # Spanish
    "pl": 5   # Polish
}
```

### DEFAULT_IGNORED_FILES

A list of strings that represent file patterns to be ignored during documentation generation by default. These include:

- `README.md`
- `\*__pycache\__`
- `\*dist`

### GIT_IGNORED_FILES

A list of strings that represent file or directory patterns to be ignored in a `gitignore` file. These include:

- `.github`
- `.git`
- `.venv`
- `.gitignore`

### GPT_MODELS

A list of strings representing available GPT models to be used for generating documentation.

## Classes

### GenerateLanguagePrompt

This class is responsible for generating language-specific prompts based on the provided `LANGUAGE_TYPE` configuration.

```python
class GenerateLanguagePrompt:
    def __init__(self, languages: dict[str, int]) -> None:
        self.languages = list(languages.keys())

    def generate(self) -> dict:
        language_prompt = {}
        for language_index in range(len(self.languages)):
            language_prompt[language_index] = self.gen_prompt(language=self.languages[language_index])

        return language_prompt

    def gen_prompt(self, language: str) -> list[str]:
        BASE_PROMPT = [
            f"""Write general idea of code in Markdown (use Google Style) in {language} language write only about Overview, 
                        Features, Structure, Usage. Dont add ```markdown. Dont invent code talk only about that code.""", 

            f"projects name is", 

            f"""Write documentation for this file in Markdown (use Google Style) in {language} language. 
                       Write only about usage and discribe every methods. 
                       Remember that it is not full documantation it is just addition. Dont add ```markdown. Dont invent code talk only about that code."""]
        return BASE_PROMPT
```

#### Usage

1. Create an instance of the `GenerateLanguagePrompt` class by passing the `LANGUAGE_TYPE` dictionary:

```python
GLP = GenerateLanguagePrompt(LANGUAGE_TYPE)
```

2. Generate language-specific prompts using the `generate()` method:

```python
language_prompt = GLP.generate()
```

3. Access individual prompts by their language index, e.g., `language_prompt[0]` for English prompts.

The prompts generated by this class can be used to guide the writing of Markdown documentation for various programming tasks.
# ReqToServer

The `ReqToServer` class contains methods for interacting with a server, specifically for creating a session and adding data to the session.

## Usage

```python
from req import ReqToServer

# Create a ReqToServer object
req = ReqToServer()

# Use the create_session method to create a new session
session_response = req.create_session()
print("Session response:", session_response)

# Use the add_to_session method to add data to the session
add_data = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}
req.add_to_session(session_code="some_session_code", data=add_data)
```

## Methods

### `__init__(self, link: str="https://sdwwwwsvbvgfgfd.pythonanywhere.com")`

- **Parameters**: `link` (optional, default: `"https://sdwwwwsvbvgfgfd.pythonanywhere.com"`): The base URL for the server's API.
- **Description**: Initializes the `ReqToServer` object with a given base URL for the server's API.

### `create_session(self) -> str`

- **Parameters**: None
- **Returns**: The server's response in string format.
- **Description**: Sends a POST request to the server to create a new session.
- **Example**:
  - Request:
  - Response: Some session response text

### `add_to_session(self, session_code: str, data: dict) -> None`

- **Parameters**: `session_code` (the session code to use), `data` (a dictionary containing data to be added to the session).
- **Returns**: None.
- **Description**: Adds the given data to the session associated with the provided session code. The data is sent as form data in a POST request.
- **Example**:
  - Request:
    - SESSION_ENDPOINT: /add_to_session
    - Body:
      - session_key: some_session_code
      - name: John Doe
      - age: 30
      - email: johndoe@example.com
  - Response: None
# Quick-Doc-Py Usage Documentation

This markdown file will describe the usage of the `quick_doc_py/main.py` file. This will include a detailed explanation of the methods and their usage.

## AutoDock Class

The `AutoDock` class is a class that automates the documentation generation process. Some of its primary functions include setting up `ReqHandler` and `GptHandler` instances and generating documentation from user prompts.

### Constructor

```python
def __init__(self, 
             root_dir: str, 
             language: str = "en", 
             ignore_file: list[str] = None,
             project_name: str = "Python Project",
             provider: str = "Mhystical",
             gpt_model: str = "gpt-4",
             general_prompt: str = "",
             default_prompt: str = "") -> None:
```

- `root_dir` - The root directory from where the code files will be fetched.
- `language` - The language for the documentation generation (default: "en").
- `ignore_file` - A list of files or patterns to ignore during the documentation process.
- `project_name` - The name of the project to be included in the generated documentation.
- `provider` - The provider to be used for GPT (default: "Mhystical").
- `gpt_model` - GPT model to be used (default: "gpt-4").
- `general_prompt` - A general prompt for additional features.
- `default_prompt` - A default prompt for the documentation process.

### Methods

- `get_response(codes)` - Generates the documentation by iterating over each code file, getting a response for each file, and maintaining the order for final documentation.
- `get_part_of_response(prompt, answer_handler)` - Gets a response from GPT for a given prompt and combines it to the `answer_handler`.

## GptHandler Class

The `GptHandler` class interacts with the GPT model using a specified provider. It allows sending prompts and receiving responses from the GPT model.

### Constructor

```python
def __init__(self, provider: str, model: str) -> None:
```
- `provider` - The provider to be used for GPT (default: "Mhystical").
- `model` - The GPT model to be used (default: "gpt-4").

### Methods

- `get_answer(prompt)` - Returns the response from GPT for the given prompt.

## ReqHendler Class

The `ReqHendler` class collects and processes files from the provided root directory and manages ignored files.

### Constructor

```python
def __init__(self, 
             root_dir: str, 
             language: str = "en", 
             ignore_file: list[str] = None,
             project_name: str = "Python Project") -> None:
```

- `root_dir` - The root directory from where the code files will be fetched.
- `language` - The language for the documentation generation (default: "en").
- `ignore_file` - A list of files or patterns to ignore during the documentation process.
- `project_name` - The name of the project to be included in the generated documentation.

### Methods

- `get_files_from_directory(current_path)` - Gets code files from the given `current_path` in the provided `root_dir`.
- `is_ignored(path)` - Checks if the given `path` is in the ignored files list.
- `get_code_from_file()` - Obtains the code from fetched files and stores it in a dictionary.

## AnswerHandler Class

The `AnswerHandler` class stores and manages the response(s) obtained for code documentation. It also aggregates the answers into a single output.

### Constructor

```python
def __init__(self, answer: str) -> None:
```

- `answer` - The initial response string for the documentation.

### Methods

- `combine_response(new_response)` - Combines a new response to the existing `answer`.
- `save_documentation(name)` - Saves the aggregated documentation into a file with the given `name`.

### Class Method

- `make_start_req_form(prompt)` - Creates a list of dictionaries to initiate a request for the given `prompt`.

## Script Usage

To run the script, use the following command:

```bash
python main.py --name_project <project_name> --root_dir <root_directory> --ignore <ignore_files> --languages <list_of_languages> --gpt_version <gpt_model> --provider <provider> --general_prompt <prompt> --default_prompt <prompt> --with_git <bool_value>
```

Replace all placeholders with the desired values, such as the project name, directories, providers, and prompts. Note that `<list_of_languages>` should be provided in a list format (e.g., `['en', 'fr', 'es']`). The `<bool_value>` should be a boolean (True or False) if the git option is used.

All the command-line options and their usage are as follows:

- `--name_project` - The name of the project.
- `--root_dir` - The root directory where code files are located.
- `--ignore` - The list of ignored files or patterns.
- `--languages` - The list of languages for the documentation.
- `--gpt_version` - The GPT model version to be used.
- `--provider` - The provider to be used for GPT.
- `--general_prompt` - The general prompt for additional features.
- `--default_prompt` - The default prompt for the documentation process.
- `--with_git` - A boolean value to indicate if git should be used for ignored files (default: None).
# Documentation for `./quick_doc_py/providers_test.py`

This file provides a set of classes and functions for testing different LLM providers using the G4F (Gutenburg 4 Foundation) chat completion library. The primary objective is to determine if a given provider works and returns expected results.

## Usage

To use this file, first install the required packages (`g4f`, `colorama`, and `argparse`) with the following terminal command:

```bash
pip install g4f colorama argparse
```

Next, create an instance of the `ProviderTest` class by specifying the desired model name. The `main()` function serves as the entry point for the script and accepts a `--name_model` argument for the model name.

```bash
python providers_test.py --name_model "gpt-4"
```

This will test all the available LLM providers and print the successful results, which indicates that the provider is functional and works for the desired model.

## Classes and Methods

### `TextStyle` class

The `TextStyle` class allows custom text styling with color and background support. It uses the `colorama` library for formatting.

- __`get_text(text: str, color: any = "", back: any = "") -> str:`__ This method takes in a text string and optional color and background attributes. It returns the formatted text with the specified style.

### `ProgressBar` class

The `ProgressBar` class provides a simple progress bar mechanism.

- __`__init__(self, part) -> None:`__ This constructor initializes a new progress bar instance with the total count of parts.
- __`progress(self, name):`__ This method updates the progress bar with the given status name.

### `ProviderTest` class

The `ProviderTest` class encapsulates the logic for testing different LLM providers.

- __`__init__(self, model_name: str) -> None:`__ This constructor initializes a new provider test instance with the given model name.
- __`get_providers(self):`__ This method obtains a list of all available provider names from the `g4f.Provider` module.
- __`test_provioder(self, provider_name: str) -> tuple[bool, str]:`__ This method tests if a given provider works with the specified model. It returns a tuple that contains a boolean indicating if the provider works and the response from the test.
- __`test_provider_timeout(self, provider):`__ This method tests a given provider with a timeout control. If the test is successful, it returns the response; otherwise, it returns `None`.
- __`test_providers(self):`__ This method tests all the available providers and stores the ones that work with the specified model.

### Functions

- __`provider_test(model_name: str) -> dict:`__ This function creates an instance of the `ProviderTest` class and tests all the available providers using the given model name.
- __`main():`__ This function parses command line arguments and executes the `provider_test` function with the given model name.

That's the end of the documentation for `./quick_doc_py/providers_test.py` file.
# utilities.py

This document describes the usage of methods present in the `utilities.py` file. The purpose of this file is to provide different helper functions and classes which can be used in various use cases.

## Classes and Functions

### TextStyle

The `TextStyle` class is defined to handle text styles and colors, using the `colorama` library. Here's how to make use of it:

- `__init__()` method: Initializes the `colorama` library.

- `get_text(text, color, back)` method: Returns a colored text based on the `color` and `back` arguments. The `color` and `back` require arguments from the `colorama` library like `Fore`, `Back`, and `Style`. The `text` should be any valid string.

### ProgressBar

The `ProgressBar` class is designed to create and manage a progress bar in the terminal. Here's how to use it:

- `__init__(self, part)` method: Initializes the `ProgressBar` object with a given value `part`.

- `progress(self, name)` method: Updates the progress bar by printing the progress percentage and the message in the terminal. It requires a `name` parameter that represents the task being displayed.

### Functions

- `start(part)`: Starts the progress bar. Requires a `part` parameter that determines the progress calculation.

- `time_manager(func)`: A decorator function for time measurement. It measures the time taken by the given function (`func`) and updates the progress bar accordingly.

Formula for progress calculation:

  *progress = math.ceil(len / 100 * procent)*

## Usage Example

```python
import time

from utilities import start, time_manager, ProgressBar, TextStyle

bar = ProgressBar(part=0)

@time_manager
def dummy():
    time.sleep(1)

# Start the progress bar
start(part=0)

# Run the dummy function
dummy()

# End the progress bar
bar = ProgressBar(part=1)
```

This example demonstrates how to start the progress bar using the `start()` function, define a decorated function using `time_manager()`, and then managing the progress with the `ProgressBar` class. The `dummy()` function here is just an example and will not actually perform any meaningful operation in this case.
### Created by [quick-doc-py](https://pypi.org/project/quick-doc-py)