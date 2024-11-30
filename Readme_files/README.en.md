# Auto Dock

## Overview
Auto Dock is a Python project designed to automate the generation of documentation for codebases. It scans the specified directories, collects source code files, and utilizes language models to generate documentation in multiple languages. The tool is particularly useful for developers looking to create coherent and structured documentation from their existing code in a quick and efficient manner.

## Features
- **Multilingual Support**: Generate documentation in several languages, including English, Russian, Ukrainian, Chinese, Spanish, and Polish.
- **Automatic File Discovery**: Recursively search through specified directories to collect relevant source code files while providing the option to ignore certain files or folders.
- **Documentation Generation**: Use language models to create structured documentation that covers important sections like Overview, Features, Structure, and Usage based on the collected code snippets.
- **Custom Project Naming**: Users can define names for their projects to tailor the output documentation.
- **Progress Monitoring**: Visual progress indication during the documentation generation process to enhance user experience.

## Structure
The project is organized into several key modules:
- **config.py**: Contains configurations related to language settings and classes for generating language-specific prompts.
- **main.py**: The primary entry point for running the Auto Dock application, responsible for managing file exploration and documentation generation workflows.
- **providers_test.py**: A module designed for testing different language model providers to ensure they function properly.
- **utilities.py**: A collection of utility functions and classes for handling text styling, progress bar implementation, and timing.
- **requirements.txt**: Lists the external libraries and modules required for the project to function correctly.

## Usage
To utilize Auto Dock, you would execute the `main.py` script from the command line, providing the necessary arguments:
- `--name_project`: Specify the name of the project to be documented.
- `--root_dir`: Indicate the root directory that contains the source code files.
- `--ignore`: Provide a list of files or directories that should be excluded from scanning.
- `--languages`: Specify a list of languages for which documentation should be generated.

### Example Command
```bash
python main.py --name_project "MyProject" --root_dir "/path/to/project" --ignore "['ignored_file.py']" --languages "['en', 'ru']"
```
This command will generate documentation for "MyProject" in both English and Russian while ignoring "ignored_file.py". The resulting documentation will be stored in the `Readme_files` directory.
# Usage Documentation for `./config.py`

This document serves as an additional reference for using the functions and classes defined in the `./config.py` file. Here, you will find information on how to utilize the `GenerateLanguagePrompt` class and its methods.

## Class: `GenerateLanguagePrompt`

The `GenerateLanguagePrompt` class is designed to generate language-specific prompts for documentation purposes. It takes a dictionary of languages and their corresponding integer indices as input.

### Methods

#### `__init__(self, languages: dict[str, int]) -> None`

The constructor method initializes the `GenerateLanguagePrompt` instance.

- **Parameters**:
  - `languages` (dict[str, int]): A dictionary where the keys are language codes (e.g., "en", "ru") and the values are unique integers representing those languages. 

#### `generate(self) -> dict`

This method generates a dictionary of prompts for each language defined in the `languages` attribute.

- **Returns**:
  - `dict`: A dictionary where each key is an index (integer) and the value is a prompt for the corresponding language.

- **Example**:
  ```python
  GLP = GenerateLanguagePrompt(language_type)
  language_prompt = GLP.generate()
  ```

#### `gen_prompt(self, language: str) -> list[str]`

This method creates a base prompt specific to the provided language code.

- **Parameters**:
  - `language` (str): A string representing the language code (e.g., "en" for English).

- **Returns**:
  - `list[str]`: A list of strings representing the generated prompts tailored for the specified language.

- **Detailed Functionality**:
  - The generated prompts include instructions for writing documentation in the Google Style format.
  - It specifies sections for "Overview," "Features," "Structure," and "Usage" and emphasizes that it is not full documentation but rather additional information.

- **Example**:
   ```python
   prompt = GLP.gen_prompt(language="en")
   ```

### Example Usage

To utilize the `GenerateLanguagePrompt` class, you can create an instance and call the `generate` method to produce language prompts, as illustrated below:

```python
from config import GenerateLanguagePrompt, language_type

GLP = GenerateLanguagePrompt(language_type)
language_prompt = GLP.generate()

# Print the generated prompts for each language
for index, prompt in language_prompt.items():
    print(f"Prompt for {list(language_type.keys())[index]}: {prompt}")
```

This example initializes the `GenerateLanguagePrompt` with the `language_type` dictionary and prints out the generated documentation prompts for each language supported. 

### Conclusion

The `./config.py` file provides tools for generating language-specific documentation prompts in a structured format. By utilizing the `GenerateLanguagePrompt` class and its methods, users can easily create tailored instructions for documenting codebases in multiple languages.
# Documentation for `./main.py` (Usage)

## Overview

This module provides functionality for analyzing project files, generating prompts based on their content, and retrieving responses using a specified AI provider. It consists of several classes, each with specific roles to manage file handling, AI interaction, and response management.

## Classes

### ReqHendler

The `ReqHendler` class is responsible for managing the collection and processing of files within the specified project directory.

#### Methods

- **`__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project")`**
  
  Initializes the `ReqHendler` instance with specified parameters:
  
  - `root_dir`: The root directory of the project.
  - `language`: The language preference for responses (default is "en").
  - `ignore_file`: A list of file paths to be ignored.
  - `project_name`: The name of the project.

- **`get_files_from_directory(self, current_path: str = "") -> None`**
  
  Recursively retrieves files from the specified directory, ignoring any files in the `ignore_file` list and storing them in `self.all_files`.

- **`is_ignored(self, path: str) -> bool`**
  
  Checks if a specific file path should be ignored based on the `ignore_file` list.

- **`get_code_from_file(self) -> None`**
  
  Reads the contents of each file collected in `self.all_files` and stores them in a dictionary `self.codes` with file paths as keys and file contents as values.

- **`make_prompt(self) -> str`**
  
  Constructs a prompt string that includes project information and the contents of the files.

### GptHandler

The `GptHandler` class manages the interaction with an AI provider for generating responses to prompts.

#### Methods

- **`__init__(self, provider: str = "DarkAI")`**
  
  Initializes the `GptHandler` instance with the specified AI provider.

- **`get_answer(self, prompt: str) -> str`**
  
  Sends the provided prompt to the AI service and returns the generated response.

### AnswerHandler

The `AnswerHandler` class is responsible for managing AI responses and saving documentation.

#### Methods

- **`__init__(self, answer: str)`**
  
  Initializes the `AnswerHandler` instance with an initial answer.

- **`save_documentation(self, name: str = "README.md") -> None`**
  
  Saves the combined responses to a specified markdown file. If the file exists, it will be cleared before writing.

- **`combine_response(self, new_response: str) -> None`**
  
  Appends a new response to the existing answers.

- **`make_start_req_form(cls, prompt: str) -> list`**
  
  Creates a formatted request list with the initial prompt for the AI.

### AutoDock

The `AutoDock` class orchestrates the overall functionality by utilizing the other classes to handle the project analysis and response generation.

#### Methods

- **`__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project")`**
  
  Initializes the `AutoDock` instance and processes files for the project.

- **`get_response(self, codes: dict) -> AnswerHandler`**
  
  Collects responses from the AI for each file's content based on the generated prompt.

- **`get_part_of_response(self, prompt: str, answer_handler: AnswerHandler = None) -> AnswerHandler`**
  
  Retrieves a response from the AI for a given prompt, optionally combining it with an existing `AnswerHandler`.

- **`save_dock(self, answer_handler: AnswerHandler, name: str = "Readme_files/README") -> None`**
  
  Saves the documented responses to a markdown file with a specific naming convention based on the selected language.

## Main Entry Point

The main section of the script uses the `argparse` library to gather user input and initiate the `AutoDock` workflow based on the provided project details, directory structure, files to ignore, and languages. It handles command-line arguments for project configuration and executes the process accordingly.

### Usage Example

To run the script, use the following command structure in the terminal:

```bash
python ./main.py --name_project "MyProject" --root_dir "/path/to/project" --ignore "['ignored_file1.py', 'ignored_file2.txt']" --languages "['en', 'de']"
```

This command will analyze the specified project directory, ignore the listed files, and generate documentation in the specified languages.
# Provider Test Documentation

## Usage

This module allows testing of various providers for a specific model using the `g4f` library. The main focus is on invoking methods related to text generation or chat completion while also providing a progress bar visual feedback. To run the tests, you need to specify a model name via command line arguments.

### Classes and Methods

#### `TextStyle`

This class handles text styling using the `colorama` library.

- **`__init__(self)`**
  - Initializes the `TextStyle` class and sets up colorama.

- **`get_text(self, text: str, color: any = "", back: any = "") -> str`**
  - Returns a styled string combining the specified text, foreground color, and background color.
  - **Parameters:**
    - `text` (str): The text to be styled.
    - `color` (any, optional): The color to be applied to the text.
    - `back` (any, optional): The background color to be applied to the text.
  - **Returns:**
    - A string with the applied color styles.

#### `ProgressBar`

This class represents a progress bar for visual feedback during the provider testing.

- **`__init__(self, part)`**
  - Initializes the `ProgressBar` with the total number of parts (i.e., providers to test).
  - **Parameters:**
    - `part` (int): The total number of providers to be tested.

- **`progress(self, name)`**
  - Updates and displays the progress bar based on the current progress.
  - **Parameters:**
    - `name` (str): The name of the provider currently being processed.

#### `ProviderTest`

This class is responsible for testing the providers.

- **`__init__(self, model_name: str)`**
  - Initializes the `ProviderTest` with the specified model name.
  - **Parameters:**
    - `model_name` (str): The name of the model to use for testing providers.

- **`get_providers(self)`**
  - Retrieves the list of available providers from `g4f.Provider` and initializes a `ProgressBar`.

- **`test_provioder(self, provider_name: str) -> tuple[bool, str]`**
  - Tests a specified provider and returns whether it succeeded and the response.
  - **Parameters:**
    - `provider_name` (str): The name of the provider to be tested.
  - **Returns:**
    - A tuple containing a boolean indicating success and the response from the provider.

- **`test_provider_timeout(self, provider)`**
  - Tests a provider with a set timeout using a decorator.
  - **Parameters:**
    - `provider`: The provider object to be tested.
  - **Returns:**
    - The response from the provider if successful, or None if the operation times out or fails.

- **`test_providers(self)`**
  - Iterates through all available providers, testing each one and displaying progress.
  - Collects and prints the working providers and their responses.
  - **Returns:**
    - A dictionary of providers that successfully responded, with their responses.

#### Entry Point

The script includes a command-line interface that allows the user to specify the model name directly when running the script.

```bash
python ./providers_test.py --name_model <model_name>
```

Make sure to replace `<model_name>` with the actual model you wish to test (e.g., `gpt-4`, `gpt-3.5-turbo`). After invoking this command, the test will start processing each provider and show progress accordingly.
# Documentation for Usage of `Auto Dock`

This documentation provides a detailed overview of the methods and classes implemented in the `Auto Dock` project to assist users in utilizing its features for automated documentation generation of Python projects.

## Usage of `main.py`

The `main.py` file is the central component for running the Auto Dock tool. It facilitates the discovery of source code files and the generation of documentation based on those files.

### Classes and Methods

#### 1. `ReqHendler`

This class is responsible for retrieving files from the specified directory and preparing the code for documentation generation.

- **`__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project")`**
    - Initializes a `ReqHendler` object with the provided parameters.
    - **Parameters:**
        - `root_dir`: Directory where the project files are located.
        - `language`: The language in which the documentation will be generated (defaults to "en").
        - `ignore_file`: A list of files (by path) to exclude from searching.
        - `project_name`: The name of the project (default is "Python Project").

- **`get_files_from_directory(self, current_path: str = "") -> None`**
    - Recursively fetches all relevant files from the specified directory, while excluding those specified in the ignore list.
    - **Parameters:**
        - `current_path`: Tracks the current path during the traversal.

- **`is_ignored(self, path: str) -> bool`**
    - Determines if a given file path should be ignored based on the user's ignore list.
    - **Parameters:**
        - `path`: The file path to check.
    - **Returns:** `True` if the file should be ignored, otherwise `False`.

- **`get_code_from_file(self) -> None`**
    - Reads the contents of the collected code files, storing them in a dictionary format.

- **`make_prompt(self) -> str`**
    - Constructs a prompt utilizing the project name, code snippets, and language-specific details.

#### 2. `GptHandler`

This class manages interactions with the GPT model, sending prompts and retrieving generated responses.

- **`__init__(self, provider: str = "DarkAI")`**
    - Initializes a `GptHandler` object with the specified GPT provider.
    - **Parameters:**
        - `provider`: The GPT provider's name (defaults to "DarkAI").

- **`get_answer(self, prompt: str) -> str`**
    - Sends the provided prompt to the GPT model and retrieves the corresponding response.
    - **Parameters:**
        - `prompt`: The text prompt sent to the GPT.
    - **Returns:** The response generated by the model.

#### 3. `AnswerHandler`

This class orchestrates the management of responses generated by the GPT model.

- **`__init__(self, answer: str) -> None`**
    - Initializes an `AnswerHandler` object to handle the generated responses.
    - **Parameters:**
        - `answer`: The initial response string.

- **`save_documentation(self, name: str = "README.md") -> None`**
    - Saves the compiled responses into a documentation file.
    - **Parameters:**
        - `name`: The filename to save the documentation to, defaulting to "README.md".

- **`combine_response(self, new_response: str) -> None`**
    - Appends a new response to the existing stored answers.

- **`make_start_req_form(cls, prompt: str) -> list`**
    - Prepares a formatted request for the GPT model based on the given prompt.
    - **Parameters:**
        - `prompt`: The prompt to package for request.

#### 4. `AutoDock`

The `AutoDock` class coordinates the documentation process, leveraging other classes to complete the documentation generation workflow.

- **`__init__(self, root_dir: str, language: str = "en", ignore_file: list[str] = None, project_name: str = "Python Project") -> None`**
    - Initializes an `AutoDock` object with details necessary for documentation generation.
    - **Parameters:**
        - Those are similar to parameters required in `ReqHendler`.

- **`get_response(self, codes: dict) -> AnswerHandler`**
    - Processes the collected code parts to generate a comprehensive response from the GPT model.
    - **Parameters:**
        - `codes`: A dictionary where keys are source file paths and values are the corresponding code snippets.

- **`time_control(self, prompt, answer_handler)`**
    - Manages the execution timing for requests sent to the GPT model.

- **`get_part_of_response(self, prompt: str, answer_handler: AnswerHandler = None) -> AnswerHandler`**
    - Fetches GPT-generated responses based on the prompt, combining them with existing answers.
    - **Parameters:**
        - `prompt`: The input prompt for the request.
        - `answer_handler`: An optional argument for an existing answer handler.
    - **Returns:** An updated `AnswerHandler` object with combined responses.

- **`save_dock(self, answer_handler: AnswerHandler, name: str = "Readme_files/README") -> None`**
    - Saves the generated documentation under the specified filename.

### CLI Usage

To run the Auto Dock from the command line, use:

```bash
python main.py --name_project <project_name> --root_dir <root_directory> --ignore <ignored_files> --languages <languages>
```

- `--name_project`: Required; the name of the project.
- `--root_dir`: Required; the directory containing the source files.
- `--ignore`: Required; a list of files to ignore.
- `--languages`: Required; a list of languages for documentation output.

## Example Command

```bash
python main.py --name_project "MyProject" --root_dir "/path/to/project" --ignore "ignored_file.py" --languages "['en', 'ru']"
```

This command will generate documentation for "MyProject" in English and Russian, excluding "ignored_file.py". The output will be saved in the `Readme_files` directory.

## Additional Usage for Other Modules

### Usage of `providers_test.py`

This file is aimed at testing various providers for generating chat completions through GPT.

- Use the **`ProviderTest`** class to check functionality and responses of providers.
- Execute from the command line with your desired model:

```bash
python providers_test.py --name_model gpt-4
```

### Usage of `utilities.py`

The `utilities` module provides helper classes such as `TextStyle` for styled console outputs and `ProgressBar` for tracking progress.

- Instantiate **`TextStyle`** to format text outputs.
- Use **`ProgressBar`** to manage and display the progress of tasks in the console.

The above outlines provide users with a clear understanding of how to utilize the classes and methods within the `Auto Dock` project for creating documentation efficiently.
# utilities.py

## Usage

This module provides utility classes and functions for managing text styling in the console and for displaying progress bars during long-running operations. The `ProgressBar` class helps visualize the progress of tasks, while the `TextStyle` class assists in coloring the text.

### Classes

#### TextStyle

The `TextStyle` class is responsible for applying color and background styles to text output in the console.

##### Methods

- **`__init__(self) -> None`**
  
  Initializes the `TextStyle` instance and configures the colorama library for terminal color support.

- **`get_text(self, text: str, color: any = "", back: any = "") -> str`**
  
  Returns the formatted text wrapped with specified color and background styles.
  
  **Args:**
  
  - `text (str)`: The text to be styled.
  - `color (any)`: The color to be applied to the text (optional).
  - `back (any)`: The background color to be applied (optional).
  
  **Returns:**
  
  - `str`: The styled text as a string.

#### ProgressBar

The `ProgressBar` class provides a method to visualize the progress of a task.

##### Methods

- **`__init__(self, part) -> None`**
  
  Initializes the `ProgressBar` instance.
  
  **Args:**
  
  - `part`: Number of parts for calculating total progress (used to determine progress completion).

- **`progress(self, name: str)`**

  Updates and displays the progress bar in the console with the current percentage of completion.

  **Args:**
  
  - `name (str)`: The name of the operation being performed, displayed alongside the progress bar.

### Global Functions

#### `start(part)`

Initializes a `ProgressBar` instance and sets it for global use.

**Args:**

- `part`: Specifies the total parts for the progress calculation.

#### `time_manager(func)`

A decorator that wraps a function to measure its execution time and update the progress bar before and after the function execution.

**Args:**

- `func`: The function to be wrapped by the decorator.

**Returns:**

- A wrapper function that executes the original function while tracking and displaying progress and execution time.
