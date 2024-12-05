## Overview "Quick-doc-py" is a Python package designed to quickly generate documentation for your projects in various languages using the Google Style Markdown. 
It can extract code from your source files, create prompts, and utilize AI language models to generate documentation about the code's structure, features, and usage.

Features
- Supports multiple languages: English, Russian, Ukrainian, Chinese, Spanish, and Polish
- Extracts code from source files
- Generates prompts for AI language models
- Uses AI language models to create documentation in Markdown format
- Supports custom prompts for specific needs
- Easy integration with popular AI language models

Structure
- The package includes a `pyproject.toml` file for managing package dependencies and configurations.
- Source code is located in the `quick_doc_py` subdirectory.
- The `config.py` file contains language type definitions and language-specific prompts.
- The `main.py` file is the entry point for executing the package. It handles command-line arguments and initializes the documentation generation process.
- The `providers_test.py` file is used for testing different AI language model providers.
- The `utilities.py` module contains helper functions for progress and time tracking.

Usage
To use "Quick-doc-py," follow these steps:

1. Install the package using pip:
```
pip install quick-doc-py
```

2. Run the documentation generation script:
```
gen-doc --name_project "My Project" --root_dir "./src" --ignore ["__init__.py"] --languages '{"en": "English", "ru": "Russian"}' --gpt_version "gpt-3.5-turbo" --provider "DarkAI" --general_prompt "" --default_prompt ""
```

This command will generate documentation for your project in the specified languages, using the specified AI language model, provider, and prompts.# pyproject.toml Documentation - Usage

This document provides information on how to use the `pyproject.toml` file in your Python project.

## Purpose

The `pyproject.toml` file is used to define project metadata and dependency information for your Python project. It helps ensure that all developers using your project have the correct dependencies installed in their environment. Additionally, this file is essential for build systems and package managers like pip and flit to install the project's dependencies correctly.

By defining dependencies, metadata, and other settings in this file, you can provide a uniform and standardized environment for everyone working on your project, thus reducing conflicts and issues due to incompatible or missing dependencies.

## Usage

1. Create a new or update an existing file named `pyproject.toml` in the root directory of your Python project.

2. Fill in the necessary information under the appropriate sections, like the example provided below:

```toml
[tool.poetry]
name = "quick-doc-py"
version = "0.8.3"
description = "This code can make documentation for your project"
authors = ["Dmytro <sinica911@gmail.com>"]
readme = "README.md"
packages = [
    { include = "quick_doc_py" }
]

[tool.poetry.scripts]
gen-doc = "quick_doc_py.main:main"
providers-test = "quick_doc_py.providers_test:main"

[tool.poetry.dependencies]
python = "^3.12"
colorama="^0.4.6"
g4f="^0.3.8.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

3. Save the `pyproject.toml` file.

4. In order to install dependencies listed in the `pyproject.toml` file, use pip:

```
pip install -r requirements.txt
```

5. To generate documentation or run other specific commands, you can use the provided scripts. For example:

```shell
gen-doc
```

### Sections and Attributes

- `[tool.poetry]`: This section contains project metadata. Common attributes include:
  - `name`: Your package's name.
  - `version`: Your package's version number.
  - `description`: A brief description of your package.
  - `description_file`: Path to the file containing the description.
  - `authors`: A list of authors and their contact information.
  - `readme`: Path to the README file.
  - `packages`: A list of package specifications. This can include subdirectories to include in the package.

- `[tool.poetry.scripts]`: This section enables you to define scripts that can be run from the command line.

- `[tool.poetry.dependencies]`: This section lists the external packages and their versions that your project depends on.

- `[build-system]`: This section specifies build-time requirements and the build-backend to use.

## Conclusion

The `pyproject.toml` file offers a structured way to maintain and manage project settings, dependencies, and metadata in Python projects. By updating this file and following the provided template, you can ensure that your development environment is consistent across your team, increasing productivity and reducing potential issues.# config.py Quick Documentation

The `config.py` file contains a configuration class `GenerateLanguagePrompt` for generating language-specific prompts for writing documentation.

## Usage

To use the `GenerateLanguagePrompt` class, initialize an instance of it by passing a dictionary of languages mapped to integers:

```python
from config import language_type
from doc_generator import GenerateLanguagePrompt

GLP = GenerateLanguagePrompt(language_type)
language_prompt = GLP.generate()
```

In this example, `language_type` is a dictionary that maps language codes (e.g., "en", "ru", "ua", "chs", "es", "pl") to their respective integers.

The `generate()` method generates a dictionary with language index keys and corresponding prompts. Each prompt includes instructions for writing documentation in the respective language according to Google Style.

## Methods

### GenerateLanguagePrompt

#### `__init__(self, languages: dict[str, int]) -> None`
- **Parameters**: `languages` (dict): A dictionary of languages mapped to integers. 
- **Returns**: `None`
- **Description**: Initializes the `GenerateLanguagePrompt` class by setting the languages attribute with the keys of the provided `languages` dictionary.

#### `generate(self) -> dict`
- **Parameters**: `None`
- **Returns**: `dict`: A dictionary containing language index keys and their respective prompts.
- **Description**: Generates and returns a dictionary of language-specific prompts for writing documentation.

#### `gen_prompt(self, language: str) -> list[str]`
- **Parameters**: `language` (str): The language code for generating the prompt.
- **Returns**: `list[str]`: A list containing the generated prompts.
- **Description**: Generates a list of prompts for writing documentation in the specified `language`. The prompts include details about the type of documentation, usage, and specific instructions.# AutoDock.py Documentation

AutoDock is a Python script that provides a way to create a documentation for a given project by generating responses from GPT using the g4f-provider.

## Usage

Before running the script you will need to install the required dependencies:

```bash
pip install g4f
```

To generate documentation for your project, you can run the script with the following command:

```bash
python main.py --name_project "<YOUR_PROJECT_NAME>" --root_dir "<YOUR_PROJECT_ROOT_DIRECTORY>" --ignore "<YOUR_IGNORE_FILE_LIST>" --languages "<YOUR_LANGUAGES_AS_PYTHON_DICT>"
```

Replace `<YOUR_PROJECT_NAME>`, `<YOUR_PROJECT_ROOT_DIRECTORY>`, `<YOUR_IGNORE_FILE_LIST>` and `<YOUR_LANGUAGES_AS_PYTHON_DICT>` with your required parameter values.

## Parameters

The script accepts several arguments, alongside their default values, to customize the behavior:

- `--name_project`: str (required) - The name of the project to document.
- `--root_dir`: str (required) - The directory containing the project.
- `--ignore`: str (required) - A list of ignored files to be excluded from generating documentation. (Format should be in python dict syntax).
- `--languages`: str (required) - A list of languages for documentation in Python dict format. (e.g. `{'fr': 'French', 'en': 'English'}`, etc.)
- `--gpt_version` (optional) - Specific version of GPT model to use, default is "gpt-3.5-turbo".
- `--provider` (optional) - Specific g4f-provider to use, default is "DarkAI".
- `--general_prompt` (optional) - A general prompt for GPT, influences the output.
- `--default_prompt` (optional) - A default user prompt for GPT, influences the output.

## Methods

- `get_response(codes: dict)`: Generates a response from GPT for the given input codes. This method processes each piece of code in the project and asks GPT for an explanation or elaboration on the content.
- `get_part_of_response(prompt: str, answer_handler: AnswerHandler = None)`: Helper method to the `get_response` method, it returns the response from GPT for a given prompt.
- `save_dock(answer_handler: AnswerHandler, name: str = "README")`: Conserves the GPT generated documentation in a Markdown file.

---

Please note that this documentation only covers the usage and basic methods. For a better understanding of each class and function, please refer to the full documentation.# Providers Test Documentation

This is the documentation for the `providers_test.py` file. It provides information on how to use the file, its classes, methods, and functions.

## Usage:

1. Import required modules:

```python
import g4f
import time
import threading
import time
from colorama import Fore, Back, Style, init
import argparse
```

2. Use the `ProviderTest` class to test providers:

```python
PT = ProviderTest(model_name="your_model_name_here")
PT.get_providers()
work_providers = PT.test_providers()
```

3. The `ProgressBar` class assists in displaying progress and the test status. Its not used directly, but it's part of the `ProviderTest` class process.

4. To run the script, use the command line and pass a model name argument:

```shell
python ./quick_doc_py/providers_test.py --name_model your_model_name_here
```

This will test all the providers available in your installation of g4f and output which providers work with the specified model.

### Classes and Methods:

- `timeout_control(timeout)`: Creates a timeout control decorator for blocking functions. It ensures that a function won't run longer than the specified timeout (in seconds).
  
- `TextStyle`: A class that provides methods to format text with colors and backgrounds using the `colorama` module.
  
  Methods:
  - `init()`: Initializes the `colorama` module (called inside the `__init__` method).
  
  - `get_text(text: str, color: any = "", back: any = "") -> str`: Returns a formatted string with the specified text, color, and background.
  
- `ProgressBar(part)`: A class that helps to show progress while testing the providers. Not meant to be used directly, as it's part of the `ProviderTest` class process.
  
  Methods:
  - `__init__(self, part)`: Initializes the ProgressBar object with the part size.
  
  - `progress(name)`: Updates the progress bar with the input name for the provider.
  
- `ProviderTest(model_name)`: The primary class for testing providers with a specific model.
  
  Methods:
  - `get_providers()`: Retrieves the list of providers from the g4f module.
  
  - `test_provioder(provider_name: str) -> tuple[bool, str]`: Tests a specific provider and returns a boolean indicating if it works, along with the response.
  
  - `test_provider_timeout(provider)`: Tests a provider with a 30-second timeout and returns the response if successful.
  
  - `test_providers()`: Tests all providers and returns a dictionary listing those that work with the specified model.
  
- `main()`: The entry point for the script, accepting an argument for the model to use.
  
  Methods:
  - `Argparse`: Parsers the command-line arguments.
  
  - `ProviderTest`: Initializes a `ProviderTest` object with the provided model name and tests providers.

This documentation mainly describes usage, hoping it helps you work with this code. For more details, consider checking the g4f module and the colorama module's official documentation.# utilities.py

This module provides a set of utilities for creating a progress bar and managing time for functions.

## Usage

To use the utilities module, you need to import it like so:

```python
from utilities import start, ProgressBar, time_manager
```

Now you can start using the utilities:

1. To create a progress bar for a specific task, use the `start` function:

```python
def main_task():
    # Your main task here

start(part)
```

2. To create a progress bar in the `main_task` function, you can use the `@time_manager` decorator:

```python
@time_manager
def main_task():
    # Your main task here
```

Make sure to include the `start` function call above the decorator.

## Classes and Methods

### `ProgressBar`

The `ProgressBar` class represents a progress bar for monitoring the progress of a task.

- **`__init__(self, part)`**: initializes the progress bar with a specific part identifier.

- **`progress(self, name)`**: updates the progress bar with the given name and prints it on the screen.

### `TextStyle`

The `TextStyle` class provides methods for formatting text by changing its color and background.

- **`get_text(self, text, color=""
                          , back=""`)**: returns the formatted text with the specified color and background.

### `@time_manager`

The `@time_manager` decorator is used to measure the execution time of a function and display it in the progress bar.

- **`wrapper(*args, **kwargs)`**: a wrapper function that calls the original function, updates the progress bar, and formats the result.
- Usage: Simply add the `@time_manager` decorator above the function you want to time.

## Examples

Here you can find a few examples of how to use the utilities module.

### 1. Creating a progress bar:

```python
from utilities import start, ProgressBar

def main_task():
    # Your main task here

start(part=1)  # Replace '1' with the part identifier of your task
```

### 2. Timing a function and displaying its execution time:

```python
from utilities import start, ProgressBar, time_manager

@time_manager
def main_task():
    # Your main task here

main_task()
```# Quick Documentation for Python Module

## Overview

This Python module (`quick_doc_py/__init__.py`) provides a set of utilities to quickly generate documentation for functions, classes, and modules. The documentation is written in Markdown and is inspired by the Google Style.

## Installation

To install the module, simply use pip:

```shell
pip install quick_doc_py
```

## Usage

To use this module, import it into your project:

```python
from quick_doc_py import generate_documentation
```

### Function Documentation

To document a function, use the `function_doc` decorator on the function you want to document. This decorator will generate a documentation string that contains the function's name, parameters, and return value. An example of a function decorated with the `function_doc` decorator:

```python
import functools
from quick_doc_py import function_doc

@function_doc
def add_numbers(a, b):
    """Adds two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b
```

### Class and Method Documentation

To document a class or its methods, first, decorate the class or method using the `class_doc` or `method_doc` decorator respectively:

```python
import functools
from quick_doc_py import class_doc, method_doc

@class_doc
class Person:
    """Represents a person with attributes like name and age."""

    def __init__(self, name, age):
        """Initializes a newtance o insf the Person class.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    @method_doc
    def introduce(self):
        """Introduces the person."""
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
```

### Generating Documentation

To generate the documentation for your functions, classes, and modules, use the `generate_documentation` function. It takes the following parameters:

- `obj`: The function, class, or module object to generate documentation for.
- `out_file`: (Optional) The output file where the documentation will be saved. If not specified, the documentation will be printed to standard output.

Here's an example of how to generate documentation for one or more objects:

```python
from quick_doc_py import generate_documentation
from my_module import add_numbers, Person

# Generate documentation for a specific function
generate_documentation(add_numbers, out_file="add_numbers.md")

# Generate documentation for a class and its methods
generate_documentation(Person, out_file="person.md")

# Generate documentation for multiple objects
generate_documentation([add_numbers, Person])
```

## Contributing

Please feel free to contribute to the module by opening an issue or a pull request on GitHub.

## License

This project is licensed under the [MIT License](./LICENSE).

## Contact

For any questions or concerns, please contact us at: [email](sinica911@gmail.com)

---
