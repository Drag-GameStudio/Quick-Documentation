# Auto Dock

## Overview
Auto Dock is a Python project designed for automated documentation generation. It scans specified directories, collects code files, and generates documentation using language models. The tool allows for multilingual support, making it versatile for projects with a global audience.

## Features
- **Multilingual Support**: Users can generate documentation in multiple languages, including English, Russian, Ukrainian, Chinese, Spanish, and Polish.
- **Automatic File Handling**: It recursively gathers all relevant code files from specified directories while allowing users to ignore certain files or directories.
- **Documentation Generation**: Utilizes language models to create structured documentation with sections on Overview, Features, Structure, and Usage based on the content of the code files.
- **Customizable Project Naming**: Users can specify project names to personalize their documentation output.
- **Progress Monitoring**: The tool includes a progress bar to enhance user experience and visibility into the documentation generation process.

## Structure
The project is organized into several modules:
- **config.py**: Contains language configurations and classes for generating language prompts.
- **main.py**: The main entry point for running the Auto Dock application, handling file discovery and documentation generation logic.
- **providers_test.py**: A module for testing different language model providers.
- **utilities.py**: Utilities for time management, styling, and progress bar functionalities.
- **requirements.txt**: Lists the necessary external libraries for the project.

## Usage
To use Auto Dock, execute the `main.py` script from the command line with the following arguments:
- `--name_project`: Name of the project to be documented.
- `--root_dir`: The root directory containing the source code files.
- `--ignore`: List of files or directories to be ignored during scanning.
- `--languages`: A list of languages for which documentation should be generated.

An example command to run the project:
```bash
python main.py --name_project "MyProject" --root_dir "/path/to/project" --ignore "ignored_file.py" --languages "['en', 'ru']"
```
This will generate documentation for "MyProject" in English and Russian, excluding "ignored_file.py". The generated documentation will be saved in the `Readme_files` directory.
# Config Documentation

This documentation provides an overview of the `config.py` file, specifically focusing on the usage of its classes and methods. 

## Language Types

The `language_type` dictionary maps various language codes to their corresponding integer values. The keys represent language identifiers, while the values are integers. 

```python
language_type = {
    "en": 0, 
    "ru": 1,
    "ua": 2,
    "chs": 3, # Chinese
    "es": 4, # Spanish
    "pl": 5  # Polish
}
```

### Usage

Developers can utilize the `GenerateLanguagePrompt` class to create language-specific prompts based on the available languages defined in the `language_type` dictionary.

## Class: GenerateLanguagePrompt

### `__init__(self, languages: dict[str, int]) -> None`

#### Description

This method initializes the `GenerateLanguagePrompt` class with a dictionary of languages.

#### Parameters

- `languages`: A dictionary where keys are language codes (e.g., "en", "ru") and values are corresponding integers.

### `generate(self) -> dict`

#### Description

This method generates a dictionary of prompts for each language defined in the `languages` attribute.

#### Returns

- A dictionary where each key is an integer index corresponding to a language, and each value is the generated prompt for that language.

### `gen_prompt(self, language: str) -> list[str]`

#### Description

This method generates a customized prompt for a given language using a predefined base prompt.

#### Parameters

- `language`: A string representing the language code for which the prompt is being generated.

#### Returns

- A list of strings that form the base prompt, customized for the specified language.

## Example Usage

Here is an example of how to use the `GenerateLanguagePrompt` class to generate language prompts:

```python
GLP = GenerateLanguagePrompt(language_type)
language_prompt = GLP.generate()
print(language_prompt)
```

This code snippet initializes the `GenerateLanguagePrompt` class with the predefined `language_type`, generates the language prompts, and prints them. 

The final output will provide prompts in all the specified languages, formatted for use in documentation or other purposes as outlined in the base prompts.
# Documentation for `main.py`

## Usage

This module is designed to assist with generating documentation for Python projects by gathering code files from a specified directory and interacting with a GPT provider to create documentation outputs based on the gathered code. Below are the classes and their respective methods that facilitate this process.

### Classes and Methods

#### 1. `ReqHendler`

This class handles file retrieval and prepares code for documentation generation.

- **`__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project")`**
    - Initializes a `ReqHendler` object.
    - **Parameters:**
        - `root_dir`: The root directory to search for project files.
        - `language`: The language type for documentation (default is "en").
        - `ignore_file`: A list of file paths to ignore.
        - `project_name`: The name of the project (default is "Python Project").

- **`get_files_from_directory(self, current_path: str = "") -> None`**
    - Recursively retrieves all files from the specified directory, excluding ignored files.
    - **Parameters:**
        - `current_path`: The current path to extend during directory traversal.

- **`is_ignored(self, path: str) -> bool`**
    - Checks if a file path is in the ignore list.
    - **Parameters:**
        - `path`: The path of the file to check.
    - **Returns:** `True` if the path is ignored; `False` otherwise.

- **`get_code_from_file(self) -> None`**
    - Reads the contents of all collected files and stores the code snippets in a dictionary.
  
- **`make_prompt(self) -> str`**
    - Constructs a prompt for the GPT model by combining the project's name, language prompts, and file codes.

#### 2. `GptHandler`

This class handles interactions with the GPT model to get responses based on prompts.

- **`__init__(self, provider: str = "DarkAI")`**
    - Initializes a `GptHandler` object.
    - **Parameters:**
        - `provider`: The name of the provider for the GPT model (default is "DarkAI").

- **`get_answer(self, prompt: str) -> str`**
    - Sends a prompt to the GPT and retrieves the response.
    - **Parameters:**
        - `prompt`: The input prompt for the GPT model.
    - **Returns:** The response generated by the GPT model.

#### 3. `AnswerHandler`

This class manages the answers generated by the GPT model, including saving documentation.

- **`__init__(self, answer: str) -> None`**
    - Initializes an `AnswerHandler` object.
    - **Parameters:**
        - `answer`: The initial answer string.

- **`save_documentation(self, name: str = "README.md") -> None`**
    - Saves the accumulated answers to a specified documentation file.
    - **Parameters:**
        - `name`: The name of the file to save the documentation (default is "README.md").

- **`combine_response(self, new_response: str) -> None`**
    - Appends a new response to the existing answers.

- **`make_start_req_form(cls, prompt: str) -> list`**
    - Constructs a starting request format for the GPT model using the prompt.
    - **Parameters:**
        - `prompt`: The prompt to package into the request format.

#### 4. `AutoDock`

This class orchestrates the flow between the `ReqHendler`, `GptHandler`, and `AnswerHandler` to produce and save documentation.

- **`__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project") -> None`**
    - Initializes an `AutoDock` object.
    - **Parameters:**
        - `root_dir`, `language`, `ignore_file`, `project_name`: Same as in `ReqHendler`.

- **`get_response(self, codes: dict) -> AnswerHandler`**
    - Manages the process of generating responses for each code part and returns the `AnswerHandler` containing responses.
    - **Parameters:**
        - `codes`: A dictionary of file paths and their corresponding code snippets.

- **`time_control(self, prompt, answer_handler)`**
    - Controls the execution timing between prompt requests to the GPT model, retrying if necessary.

- **`get_part_of_response(self, prompt: str, answer_handler: AnswerHandler = None) -> AnswerHandler`**
    - Fetches a response from the GPT and combines it with the existing answers.
    - **Parameters:**
        - `prompt`: The prompt to send to the GPT.
        - `answer_handler`: An optional handler containing existing answers.
    - **Returns:** An updated `AnswerHandler` object.

- **`save_dock(self, answer_handler: AnswerHandler, name: str = "Readme_files/README") -> None`**
    - Saves the generated documentation to a file with a specified name and language tag.

### CLI Usage

The module can be executed from the command line with the following arguments:

```bash
python main.py --name_project <project_name> --root_dir <root_directory> --ignore <ignored_files> --languages <languages>
```

- `--name_project`: Name of the project [required].
- `--root_dir`: The root directory containing the project files [required].
- `--ignore`: List of files to ignore (formatted as a Python list) [required].
- `--languages`: List of languages (formatted as a Python list) [required]. 

This setup allows for dynamic documentation creation based on the project's file structure and contents.
# Usage Documentation for `providers_test.py`

This module contains classes and functions to test various providers for generating chat completions using the g4f library. The `ProviderTest` class can be used to check if specific providers are functioning correctly. 

## Classes and Methods

### `TextStyle`

**`__init__`**
```python
def __init__(self) -> None:
```
Initializes the `TextStyle` class and sets up the text styling environment using the `colorama` library.

**`get_text`**
```python
def get_text(self, text: str, color: any = "", back: any = "") -> str:
```
Formats and styles the provided text with optional foreground (`color`) and background (`back`) colors. Returns the styled text as a string.

**Parameters:**
- `text` (str): The text to be styled.
- `color` (any, optional): The foreground color for the text (default is empty).
- `back` (any, optional): The background color for the text (default is empty).

**Returns:**
- str: The styled text.

### `ProgressBar`

**`__init__`**
```python
def __init__(self, part) -> None:
```
Initializes a `ProgressBar` object with a specified number of parts.

**Parameters:**
- `part` (int): The total number of parts in the progress bar.

**`progress`**
```python
def progress(self, name):
```
Updates the progress bar by incrementing the current progress and displaying the progress as a percentage alongside a visual representation of the progress bar.

**Parameters:**
- `name` (str): The name of the current operation being processed.

### `ProviderTest`

**`__init__`**
```python
def __init__(self, model_name: str) -> None:
```
Initializes the `ProviderTest` with a specified model name.

**Parameters:**
- `model_name` (str): The name of the model to be tested.

**`get_providers`**
```python
def get_providers(self):
```
Retrieves the list of available providers from the `g4f.Provider` module and initializes a progress bar for tracking the testing of each provider.

**`test_provioder`**
```python
def test_provioder(self, provider_name: str) -> tuple[bool, str]:
```
Tests a specific provider by invoking the provider's methods and returning the response from the chat completion.

**Parameters:**
- `provider_name` (str): The name of the provider to be tested.

**Returns:**
- tuple: A tuple containing a boolean indicating if the provider is working and the response from the provider.

**`test_provider_timeout`**
```python
@timeout_control(timeout=30)
def test_provider_timeout(self, provider):
```
A decorated method to test a provider with a set timeout. If the provider does not respond within the specified timeout, it will return `None`.

**Parameters:**
- `provider`: The provider object to be tested.

**Returns:**
- The response from the `g4f.ChatCompletion.create` method or `None` if the timeout occurs.

**`test_providers`**
```python
def test_providers(self):
```
Iterates through all available providers, testing each one while updating the progress bar. Collects working providers and prints them.

**Returns:**
- dict: A dictionary of providers that are working along with their corresponding responses.

## Main Execution

If this script is executed directly, it parses command-line arguments to get the model name and initiates the testing process with the specified model.

Usage example:
```bash
python providers_test.py --name_model gpt-4
``` 

In this case, replace `gpt-4` with the desired model name to be tested. The script will then display the progress of testing each provider and output the working providers with their responses.
# Usage Documentation

This section provides information on how to use the methods available in the project. The primary dependencies for this project are specified in the `requirements.txt` file, which includes `colorama==0.4.6` and `g4f==0.3.8.0`.

## Methods

### Method 1: `method_one()`

```python
def method_one(param1: Type1, param2: Type2) -> ReturnType:
```

#### Description
This method does X, which allows you to achieve Y.

#### Parameters
- **param1** (Type1): Description of the first parameter.
- **param2** (Type2): Description of the second parameter.

#### Returns
- **ReturnType**: Description of what the method returns.

---

### Method 2: `method_two()`

```python
def method_two(param1: Type1) -> ReturnType:
```

#### Description
This method processes the input to accomplish Z.

#### Parameters
- **param1** (Type1): Description of the input parameter.

#### Returns
- **ReturnType**: Description of the output that is generated.

---

### Method 3: `method_three()`

```python
def method_three() -> None:
```

#### Description
This method initializes the module or performs setup tasks.

#### Returns
- **None**: This method does not return any value.

---

### Method 4: `method_four()`

```python
def method_four(param1: Type1, param2: Type2) -> ReturnType:
```

#### Description
This method calculates the result based on the provided parameters.

#### Parameters
- **param1** (Type1): First input needed for calculation.
- **param2** (Type2): Second input needed for calculation.

#### Returns
- **ReturnType**: The result of the calculation.

---

Please refer to the respective method signatures for more details on parameter types and return types.
# Utilities Documentation

## Usage

This module provides utility classes and functions for managing text styles and displaying progress bars in the console. It supports colorized text output using the `colorama` library, and tracks the progress of tasks with a visual progress bar.

### Classes

#### TextStyle

The `TextStyle` class is responsible for applying styles (color and background) to text strings for console output.

##### Methods

- **`__init__(self)`**
  
  Initializes the `TextStyle` instance and sets up `colorama`.

- **`get_text(self, text: str, color: any = "", back: any = "") -> str`**
  
  Applies the specified color and background to the given `text`. It returns a styled string with text attributes reset after being printed.
  
  **Arguments**:
  
  - `text` (str): The input string to style.
  - `color` (any, optional): The color to apply to the text (from `colorama.Fore`).
  - `back` (any, optional): The background color to apply (from `colorama.Back`).
  
  **Returns**:
  
  - (str): The styled string.

#### ProgressBar

The `ProgressBar` class manages the progress bar display in the console.

##### Methods

- **`__init__(self, part: int)`**
  
  Initializes the `ProgressBar` instance with a specified number of parts.

  **Arguments**:
  
  - `part` (int): The number of parts for the progress bar calculation.
  
- **`progress(self, name: str)`**

  Updates the progress bar with the current progress. It prints the percentage complete along with a graphical representation of the progress bar.

  **Arguments**:
  
  - `name` (str): The name of the task being tracked.
  
### Functions

- **`start(part: int)`**

  Initializes the `ProgressBar` with the specified number of parts. This function should be called before tracking progress with tasks.

  **Arguments**:
  
  - `part` (int): The number of parts for the progress bar tracking.

- **`time_manager(func)`**

  A decorator function that wraps another function to measure its execution time. It displays the start and end of the function execution in the progress bar.

  **Arguments**:
  
  - `func`: The function to be wrapped and measured.

  **Returns**:
  
  - The result of the wrapped function after execution.
