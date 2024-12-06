

Overview:
- The code consists of three main components: utilities (for timers), providers_test (for testing various AI providers), and quick_doc_py (for generating project documentation).

Features:
- Ability to choose the desired programming language for documentation.
- Customizable prompts for general and default usage.
- Can ignore specific files or folders in the project directory.
- Utilizes multi-threading to handle multiple files simultaneously.

Structure:
- The utilities module contains timer functions for managing and displaying elapsed time.
- The providers_test module allows for testing multiple AI providers and their responses.
- The quick_doc_py module contains classes to handle task requests, handle GPT interactions, and combine responses to generate documentation.

Usage:
- First, install the required dependencies (g4f, colorama) and set up the Gitignore file to exclude necessary files from documentation.
- Define the project directory, language, and name in the command line arguments.
- Run the main.py script with the desired parameters in the command line.
```bash
gen-doc --name_project "Quick Doc py" --root_dir "./" --ignore "[' ']" --languages "['en']" --with_git True --general_prompt "Add exaple of usege this lib take from pyproject.toml" --default_prompt "Add ditails"
```
Note: CLI input Includes specific arguments like:

- --name_project: Name of the project
- --root_dir: The project directory
- --ignore: Ignored files or folders (as list)
- --languages: List of languages for which documentation to be generated
- --with_git: Denotes if Git is used (Boolean)
- --gpt_version and --provider:Specify GPT version and provider (for GPT Handler)
- --general_prompt and --default_prompt: Customizable prompts (_txt)

The script will create a Google-style documentation file for each supported language in the project directory.# pyproject.toml Documentation

This `pyproject.toml` file is used to manage the project's dependencies, build system, and other metadata. Below, you'll find a description of its usage, along with descriptions of each method related to the file content.

## Usage

The `pyproject.toml` file is primarily used by tools like Poetry to manage and install project dependencies. It also contains metadata, such as the project's name, version, description and author(s) information.

## Description of methods

| Section | Description |
|---------|-------------|
| `[tool.poetry]` | This section contains the metadata and configuration options for the project. |
| `name = "quick-doc-py"` | The name of your project. |
| `version = "0.8.9"` | The version of your project. |
| `description = "This code can make documentation for your project"` | A short, one-line description of your project. |
| `authors = ["Dmytro <sinica911@gmail.com>"]` | A list of project authors and their contact information. |
| `readme = "README.md"` | The name of the file that serves as the project's README. |
| `packages = [{ include = "quick_doc_py" }]` | Specifies which packages should be included in the final build. |
| `repository="https://github.com/dima-on/Auto-Dock"` | The URL of the project's repository. |
| `[tool.poetry.scripts]` | This section defines the scripts that can be run from the command line. |
| `gen-doc = "quick_doc_py.main:main"` | Defines a script named `gen-doc` that runs the `main` function within the `quick_doc_py` module. |
| `providers-test = "quick_doc_py.providers_test:main"` | Defines a script named `providers-test` that runs the `main` function within the `providers_test` module. |
| `[tool.poetry.dependencies]` | This section defines the project's dependencies. |
| `python = "^3.12"` | The required version of Python for this project. |
| `colorama="^0.4.6"` | A dependency on the `colorama` package with a minimum version of 0.4.6. |
| `g4f="^0.3.8.3"` | A dependency on the `g4f` package with a minimum version of 0.3.8.3. |
| `[build-system]` | This section defines the build system for your project. |
| `requires = ["poetry-core"]` | The required dependencies for the build system. |
| `build-backend = "poetry.core.masonry.api"` | The build backend to use with the defined build system. |

Remember that this is not a full documentation, only an addition that describes the methods and usage of this specific file.# Config Module Documentation

The `config.py` file contains essential configuration settings for the project.

## LANGUAGE_TYPE

A dictionary that maps language codes to their respective integer indices:

- `"en"`: English (0)
- `"ru"`: Russian (1)
- `"ua"`: Ukrainian (2)
- `"chs"`: Chinese (3)
- `"es"`: Spanish (4)
- `"pl"`: Polish (5)

## DEFAULT_IGNORED_FILES

A list of file patterns that are ignored by default, including:
- `README.md`
- `__pycache__`
- `dist`

## GIT_IGNORED_FILES

A list of file patterns that should be ignored in the `.gitignore` file, including:
- Everything within the `.github` folder
- Everything within the `.git` folder
- Everything within the `.venv` folder
- The current `.gitignore` file

## GenerateLanguagePrompt Class

The `GenerateLanguagePrompt` class initiates a generator of language prompts.

### `__init__` Method

Accepts a languages dictionary as input, extracting the keys (language strings) and storing them in `self.languages`.

### `generate` Method

Generates a dictionary `language_prompt` with prompts corresponding to each language.

### `gen_prompt` Method

Generates a list of prompts for a given language. The method returns a fixed list of prompts for writing documentation of different types.

```python
    def gen_prompt(self, language: str) -> list[str]:
        BASE_PROMPT = [
            f"""Write general idea of code in Markdown (use Google Style) in {language} language write only about Overview, 
            Features, Structure, Usage. Dont add ```markdown""",
            
            f"Projects name is",
            
            f"""Write documentation for this file in Markdown (use Google Style) in {language} language. 
            Write only about usage and discribe every methods. 
            Remember that it is not full documantation it is just addition. Dont add ```markdown"""
        ]
        return BASE_PROMPT
```

The `GenerateLanguagePrompt` class is then instantiated with the `LANGUAGE_TYPE` dictionary and its `generate` method called to produce `language_prompt`, containing prompts for each supported language.

Finally, the list of supported languages (keys in `LANGUAGE_TYPE`) is printed.## Documentation for main.py

### Usage

This file, `main.py`, contains a program for generating project documentation using AI-based code completion tools. To begin, you'll need to install the `g4f` package by running the following command:

```bash
pip install g4f
```

#### Options and Arguments

Run the script and provide the necessary arguments as prompted. The script will generate automation documenion tatbased on the provided input.

```python
import sys
import main

if __name__ == "__main__":
    main.main()
```

### Classes and Methods

1. **ReqHendler**:
   - `__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project) -> None:`
   - `get_files_from_directory(self, current_path: str = "") -> None:`
   - `is_ignored(self, path:str) -> bool:`
   - `get_code_from_file(self) -> None:`
   - `make_prompt(self) -> str:`

2. **GptHandler**:
   - `__init__(self, provider: str, model: str) -> None:`
   - `get_answer(self, prompt: str) -> str:`

3. **AnswerHandler**:
   - `__init__(self, answer: str) -> None:`
   - `save_documentation(self, name: str = "README.md") -> None:`
   - `combine_response(self, new_response: str) -> None:`
   - `make_start_req_form(@classmethod, cls, prompt: str) -> list:`

4. **AutoDock**:
   - `__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project", provider: str = "Mhystical", gpt_model: str = "gpt-4", general_prompt: str = "", default_prompt: str = "") -> None:`
   - `get_response(self, codes: dict) -> AnswerHandler:`
   - `get_part_of_response(self, prompt: str, answer_handler: AnswerHandler) -> AnswerHandler:`

5. **Main**:
   - `main():`

#### Functions

- `worker(args):` (`main()`:)
- `save_dock(self, answer_handler: AnswerHandler, name: str = "README"):`# Providers Test Documentation

This script is designed to test various providers from the `g4f` (GPT-4 Faker) library and output the providers that work with the given model. The script utilizes a timeout control mechanism to prevent infinite waiting on slow or non-responsive providers.

## Usage

To use this script, you need to have `g4f` installed. Run the following command to install it:

```bash
pip install g4f
```

After installation, execute the script by passing the name of the model you'd like to test the providers with using the `--name_model` argument.

```bash
python providers_test.py --name_model your_model_name
```

Replace `your_model_name` with the desired model name (e.g., "gpt-4", "gpt-3.5-turbo"). Run the script, and it will display a list of working providers with their corresponding responses.

## Methods:

### `timeout_control(timeout)`

This function is a decorator that adds a timeout mechanism to a function. The `timeout_control` takes one argument, the timeout value in seconds. If the applied function does not return within the specified timeout, it will return `None`.

### `TextStyle()`

This class is responsible for text formatting using the `colorama` library. The `get_text` method receives a string of text and optional color (`Fore.CYAN`, `Fore.GREEN`, etc.) and background (`Back.WHITE`) values to style the text.

### `ProgressBar(part)`

The `ProgressBar` class is used for displaying a progress bar during the provider testing process. The `part` parameter represents the number of parts (providers) to test.

### `ProviderTest(model_name)`

This class is responsible for testing the providers and selecting the working ones for the given model. Use the `get_providers` method to fetch the list of providers. Call `test_providers` to test the providers and get a dictionary of working providers and their responses.

#### Methods for `ProviderTest`:

- `get_providers()`: Fetches the list of available providers from `g4f.Provider`.
- `test_provider(provider_name)`: Tests a single provider by calling the `test_provider_timeout` method.
- `test_provider_timeout(provider)`: Attempts to create a `ChatCompletion` object using the given provider. If successful, it returns the response; otherwise, it returns `None`. This method uses the `timeout_control` decorator.
- `test_providers()`: Tests all available providers and identifies the working ones with the given model.

### `main()`:

The `main` function is the entry point of the script. It takes command-line arguments for the model name and initializes the `ProviderTest` object. Ultimately, `test_providers` is called to test the providers.

## Note:

This documentation is an overview of the script's usage and methods. For a more comprehensive understanding, refer to the source file and inline comments for detailed implementation.# utilities.py

This module provides utilities to create a dynamic progress bar and time tracking. The `ProgressBar` class displays the progress of a task in the console while the `@time_manager` decorator monitors the time it takes for a function to execute.

## Usage

1. Import the necessary classes and decorators from `utilities.py`:

```python
from utilities import ProgressBar, time_manager, start
```

2. Create an instance of the `ProgressBar` class by using the `start` function and providing the number of parts to be handled. Example:

```python
start(part=3)  # For a 3-part task
```

3. To measure the execution time of any function, decorate it with the `@time_manager` decorator. Inside the function, use the `bar.progress()` method to update and display the progress:

```python
@time_manager
def my_function():
    bar.progress("Working on part 1")
    # Perform your task
    bar.progress("Working on part 2")
    # Perform your other task
```

Now, let's dig into the available methods.

## Methods

### TextStyle
The `TextStyle` class provides methods to style text in the console using the `colorama` library.

#### get_text(text: str, color: any = "", back: any = "") -> str
- **text**: The text that you want to stylize.
- **color** (optional): The color of the text. Default is an empty string (no color).
- **back** (optional): The background color of the text. Default is an empty string (no background color).
- Returns: The stylized text.

### ProgressBar
The `ProgressBar` class helps to display the progress of a task in the console.

#### \_\_init\_\_(self, part) -> None
- **part**: The number of parts that will be handled during the task.

#### progress(self, name)
- **name**: The text to display as the progress status.

### @time_manager
The `@time_manager` decorator is used to measure the execution time of any function.

- Wraps the original function and measures the time spent inside it.
- Displays a start and end message with the execution time in the console.

Note: You must import the `time` module for the `time_manager` to work correctly.

## Additional Information
- Remember to reset the console by using appropriate methods or closing the script before executing this module.
- Make sure `colorama` and `time` modules are also imported for the functionality to work as expected.
- Reset the colorama styles whenever necessary using `Style.RESET_ALL`.# Quick Documentation for `__init__.py`

This file is a part of a Python package named `quick_doc_py`. The package serves to provide additional quick documentation for your Python scripts, modules, or classes. The documentation is written in Markdown and follows the Google Style guide.

## Usage

To use this package, first make sure you have installed it using pip:

```sh
pip install quick_doc_py
```

Next, import the package into your Python script:

```python
import quick_doc_py
```

Now, you can use the functionalities provided by the package. The main function provided by `quick_doc_py` is `quick_doc`. This function helps in generating quick documentation for your methods and classes.

### The quick_doc Function

The `quick_doc` function is designed to create Markdown documentation for your Python methods, classes, and functions. This function requires three arguments mentioned below:

1. **doc_str**: A string containing the given docstring of the method, class, or function. This is the most important parameter for this function, as it determines the shape, content, and language of the generated documentation.
2. **function_name**: A string representing the name of the method, class, or function for which you want to generate quick documentation. This helps in adding the method's name in the resulting documentation.
3. **arguments**: A list containing a tuple of the required arguments for your function, methods, or class along with their explanations. For method and classes, it can be left empty.

#### Example

Assume you have the following function:

```python
def greet(name):
    """
    Greets the given name and returns a greeting

    :param name: string, the person's name to greet
    :return: string, the greeting message
    """
    return f"Hello {name}!"
```

To generate quick Markdown documentation for this `greet` function, use the following code:

```python
doc_string = """
Greets the given name and returns a greeting

:param name: string, the person's name to greet
:return: string, the greeting message
"""
quick_doc_py.quick_doc(doc_string, 'greet', arguments=[('name', 'string, the person's name to greet')])
```

The generated Markdown documentation will look like this:

```markdown
### greet

Greets the given name and returns a greeting

**Arguments**:
- `name`: string, the person's name to greet
**Returns**:
- string, the greeting message
```

__Important Note:__ The `quick_doc` function provided by `quick_doc_py` is a tool to generate quick documentation in Markdown. It's meant to serve as a starting point to create documentation for your scripts, modules, or classes. You must write and expand upon this documentation as needed for your specific use cases.