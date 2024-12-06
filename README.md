Name: Quick Doc py

Overview:
Quick Doc py is a Python project that generates documentation for your project using an AI-powered language model, specifically applied to code organization, file structure, and functionality explanation. This project aims to make the documentation process more efficient and less time-consuming for developers and project maintainers.

Features:
- Supports multiple languages with corresponding translations
- Reads and processes code files from a specified directory
- Excludes specified files and directories from processing
- Generates readable Markdown documentation
- Sends prompt inquiries to an AI model to enhance the documentation scope with general or specific prompts
- Organizes documentation into an overview, features, structure, and usage sections
- Evaluates which code files to process based on ignored files list (default and git-specific)
- Applies timeouts and progress bars for more user-friendly experience during code processing and AI response waiting

Structure:
The repository structure comprises several Python files and modules with specific functionality. Notable components include:

- `config.py`: Defines language-specific options and lists of ignored files.
- `quick_doc_py`: The main module containing the main.py script which handles command-line arguments and starts the documentation generation.
- `providers_test.py`: A testing module for evaluating different AI providers.
- `utilities.py`: General utility module that provides helper functions like progress bars and time-tracking decorators.

Usage:
To use Quick Doc py, simply clone or download the repository and navigate to the root directory. Install the required dependencies using pip:

```python
pip install -r requirements.txt
```

Once installed, you can start the documentation generation with the command:

```bash
python main.py --name_project "Your Project Name" --root_dir "path/to/your/project" --ignore '["*.venv", "*.git", "*.github"]' --languages '{"en", "ru", "ua"}' --general_prompt "Provide additional context about the code organization" --default_prompt "Describe the specific file xyz.py"
```

Replace placeholders as necessary and customize prompts according to your needs. The documentation will then be generated in Markdown format, per language, in the project's root directory. You can find the generated documentation files in the matching language-specific name, for example, README.en.md, README.ru.md, and so on.# pyproject.toml Markdown Documentation

This documentation provides a description of the `pyproject.toml` file in Markdown format for the `quick-doc-py` project. This guide covers the usage, and describes each of the methods available within the file.

## Usage

The `pyproject.toml` file is used in Python projects to manage project settings and dependencies. Below is the content of this specific file, along with explanations for each section:

```toml
[tool.poetry]
name = "quick-doc-py"
version = "0.9.3"
description = "This code can make documentation for your project"
authors = ["Dmytro <sinica911@gmail.com>"]
readme = "README.md"
packages = [
    { include = "quick_doc_py" }
]
repository="https://github.com/dima-on/Auto-Dock"

[tool.poetry.scripts]
gen-doc = "quick_doc_py.main:main"
providers-test = "quick_doc_py.providers_test:main"

[tool.poetry.dependencies]
python = "^3.12"
colorama="^0.4.6"
g4f="^0.3.8.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### Sections
- `[tool.poetry]`: Contains metadata about the project. The `name`, `version`, and `description` are self-explanatory. The `authors` field is a list of contributors, where each author is represented as "name" (optional) and email. The `readme` points to the location of the README file in the repository. The `packages` field lists the packages to be included in the distribution.

- `[tool.poetry.scripts]`: Defines commands that users can run from the command line after installing the package.
   - `gen-doc`: Invokes the `main` function from `quick_doc_py` package.
   - `providers-test`: Invokes the `main` function from `quick_doc_py.providers_test` module.

- `[tool.poetry.dependencies]`: Defines the project dependencies required to run the code.
   - `python`: The minimum Python version required for the project.
   - `colorama` and `g4f`: Dependencies for color formatting in the output.

- `[build-system]`: Specifies the build system requirements. In this case, `poetry-core` is the required dependency, and `poetry.core.masonry.api` serves as the build backend.

## Running the script

To execute the script, install the module using pip:

```bash
pip install ./path_to/quick-doc-py
```

After installation, you can run the script from the command line using the following commands:

```shell
gen-doc -- generates documentation for your project
providers-test -- tests the providers (optional)
```

Use the provided commands to create documentation or test the code's functionality. Remember to modify these commands to suit your project specifics according to the usage requirements.# Config

This file (`config.py`) contains various settings and configurations for generating language-specific prompts.

## Configurations

The following variables are defined in this file:

### LANGUAGE_TYPE

A dictionary mapping language codes to their corresponding numeric values:

- `"en"`: 0 - English
- `"ru"`: 1 - Russian
- `"ua"`: 2 - Ukrainian
- `"chs"`: 3 - Simplified Chinese
- `"es"`: 4 - Spanish
- `"pl"`: 5 - Polish

### DEFAULT_IGNORED_FILES

A list of file patterns to be ignored in the default search:

- `"*README.md"` - all README.md files
- `"*__pycache__"` - all directories named `__pycache__`
- `"*dist"` - all directories and files named `dist`

### GIT_IGNORED_FILES

A list of Git-ignored directory patterns:

- `"*.github"` - all files and directories starting with `.github`
- `"*.git"` - the `.git` directory
- `"*.venv"` - all directories and files named `venv`
- `"*.gitignore"` - the `.gitignore` file

## Usage

To use this file, you can import the configurations in another Python script:

```python
from config import LANGUAGE_TYPE, DEFAULT_IGNORED_FILES, GIT_IGNORED_FILES
```

To create and use language prompts, you would use the `GenerateLanguagePrompt` class:

```python
from config import GenerateLanguagePrompt, LANGUAGE_TYPE

# Create an instance of GenerateLanguagePrompt class
GLP = GenerateLanguagePrompt(LANGUAGE_TYPE)

# Generate language-specific prompts
language_prompt = GLP.generate()

# Print available language codes
print(list(LANGUAGE_TYPE.keys()))
```# AutoDock Documentation

This guide explains the usage and running of the `main.py` file, which automates the creation of documentation for a given project.

## Requirements

- Python 3.8 or higher is required.
- Installation of required packages (`g4f`, `argparse`, `ast`, `os`, `sys`, `time`) must be pre-installed.

## Installation

The file `main.py` provides needed functions to run AutoDock's functionality. To set it up, simply clone the repository with the file in it or download the `main.py` file.

## Description

AutoDock reads code files in the given directory, generates prompts for the user, and sends them to the GPT-4 (using the g4f library) to create file-specific documentation. All responses are then saved into `README.{language}.md` files.

## AutoDock Usage

First, make sure the ROOT_DIR contains the project files you wish to document. Then, use the command below:

```bash
python main.py --name_project "Your Project Name" --root_dir "/path/to/your/project" --ignore '["*.env", "*.log"]' --languages '["en", "ru"]' --gpt_version "gpt-4" --provider "OpenAI" --general_prompt "Please generate a documentation for the below files" --default_prompt "Describe the functionality of the following function or class."
```

The arguments are:
- `--name_project`: The name for your project to be used in the documentation.
- `--root_dir`: The path to the directory containing the project files.
- `--ignore`: A list of ignored files. E.g., `["*.env", "*.log"]`. To use g4f's default ignore lists, you can pass an empty list along with the default lists during initialization: `--ignore '[]' --default_ignore '["*.env", "*.log"]'`.
- `--languages`: A list of languages to generate documentation in.
- `--gpt_version`: Chose a GPT version, such as "gpt-3.5-turbo" or "gpt-4".
- `--provider`: API provider, e.g., "OpenAI" or "DarkAI".
- `--general_prompt`: A general prompt used in the documentation.
- `--default_prompt`: A default prompt used for individual files.
- `--with_git`: An optional boolean that, when supplied, includes `.gitignore`-listed files, defaulting to `None`.

Please note that AutoDock accepts additional command-line arguments that can be found within the `main()` function to pass to the `argparse.ArgumentParser()`.

## GptHandler & AnswerHandler Usage

These classes complement AutoDock by providing functions to handle user prompts and GPT responses. While you can use them to manage inputs and outputs independently, they're designed to interoperate with AutoDock.

Example of GptHandler:

```python
gpt_handler = GptHandler("OpenAI", "gpt-4")
response = gpt_handler.get_answer("What is the purpose of the `main.py` file?")
```

Example of AnswerHandler:

```python
answer_handler = AnswerHandler(response.content)
answer_handler.save_documentation(name="documentation.md")
```

## Powering up

To adjust the script parameters, you can edit them directly in the `main` function, or create an external `.env` file (as Python's `dotenv`, for example) and load the values:

```python
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.getenv("ROOT_DIR")
```

This will make the script much more flexible and easier to test in development.

Remember that this documentation describes the additional functionalities of the file only. For more exhaustive information, refer to the [full documentation](url_to_full_documentation.md).

Wishing you good luck on your documentation automation journey!# providers_test.py Quick Documentation

This document describes the usage of the `providers_test.py` file which is a Python script. It is designed to test the providers of a given model and check which of the providers are functioning properly.

### Description of Methods

#### timeout_control

The `timeout_control` function is a decorator that defines a timeout for the function it wraps. If the wrapped function does not return within the specified timeout, it will return `None`.

#### TextStyle

This class enables styling of text with colors and backgrounds. The class has the following methods:

- `__init__`: Initializes the `TextStyle` object, also initializes the Colorama library.

- `get_text`: Returns a formatted text string with the specified color and background. Parameters:
  - `text`: Text to be formatted.
  - `color`: Color style for the text. If not specified, will be a plain text.
  - `back`: Background style for the text. If not specified, will be a plain text.

#### ProgressBar

This class defines a progress bar that updates with a given percentage completion. It consists of the following methods:

- `__init__`: Accepts the total parts (`self.all`) that the progress bar should display.
- `progress`: Prints the progress bar on the console, updating the progress percentage. Parameters:
  - `name`: Name of the current task being displayed on the progress bar.

#### ProviderTest

This class represents an instance of provider testing for a given model. It includes the following methods:

- `__init__`: Initializes the `ProviderTest` object with a given model name.
- `get_providers`: Fetches all the providers available for the given model. Initializes a `ProgressBar` to monitor the test's progress.
- `test_provider`: Tests an individual provider to see if it is functioning properly. Parameters:
  - `provider_name`: The name of the provider to test.
- `test_provider_timeout`: Tests a provider within a set timeout period. Parameters:
  - `provider`: The provider object to test.
- `test_providers`: Tests all the providers for the given model, displaying their progress through a `ProgressBar`, and returns a dictionary with working providers and their responses.

#### main

The `main` function is the entry point for the script. It parses the command-line arguments, initializes the `ProviderTest` object with the given model name, and runs the tests.

### How to Use

To use `providers_test.py`, run the script from the command line with the `--name_model` flag followed by the model name:

```bash
python providers_test.py --name_model modelName
```

Replace `modelName` with the name of the model you want to test. This will display the providers that are working correctly for the specified model.# utilities.py Quick Documentation

## Usage

This file contains a set of utility classes and functions to create a progress bar, manage execution time, and apply text formatting using Colorama.

## Classes and Methods

### `TextStyle`

The `TextStyle` class provides a method to format the text with custom colors and background styles.

- **get_text(text: str, color: any = "", back: any = "") → str**
  - Description: This method accepts a text string and allows you to optionally specify color and background for text formatting. It uses the Colorama library for this purpose.

### `ProgressBar`

The `ProgressBar` class is used to create a simple progress bar that updates throughout the execution.

- **__init__(self, part)**
  - Description: The constructor initializes the progress bar based on the given `part`, which is a factor used for constructing the progress bar.

- **progress(self, name)**
  - Description: The `progress` method updates the progress bar with a `name` parameter that is displayed next to the progress bar inside the terminal.

### Time Management Decorator

This file also includes a `time_manager` decorator that can be applied to a function to print progress and execution time.

- **time\_manager(func)**
  - Description: This is a decorator function that wraps the given `func`. It logs the start and end of the function execution, displaying the function name and time taken to complete the function.

## Example Usage

```python
from utilities import start, ProgressBar, time_manager
from time import sleep

@time_manager
def example_function():
    for i in range(5):
        print(i)
        sleep(1)

start(part=1)  # Set the part according to the desired progress bar size.
example_function()
```

This example demonstrates how to apply the `time_manager` decorator, and use `start` and `ProgressBar` classes within your code to inform users about progress and function execution time.from quick_doc_py.core import generate_quick_doc

__all__ = ['generate_quick_doc']

def generate_quick_doc(file_path, output_file_path):
    """
    Generate quick code documentation for a Python file.

    This function takes in a Python file path and generates quick documentation
    using the Google Style format. The documentation will be saved to the output
    file path specified.

    Args:
        file_path (str): The path to the Python source file.
        output_file_path (str): The path to save the generated documentation.

    Returns:
        None
    """


    # Read the content of the Python file.
    with open(file_path, 'r') as file:
        content = file.readlines()

    # Generate the quick documentation.
    generated_doc = generate_quick_doc_py(content)

    # Write the generated documentation to the output file.
    with open(output_file_path, 'w') as file:
        file.write(generated_doc)

    print(f"Successfully generated quick documentation: {output_file_path}")