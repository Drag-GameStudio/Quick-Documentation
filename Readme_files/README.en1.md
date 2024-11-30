# Auto Dock

## Overview
Auto Dock is a Python-based project designed for automated documentation generation of codebases. It comprehensively scans a specified directory for source code files, generates a structured documentation prompt for each file, and utilizes a language model to produce detailed markdown documentation. The output is tailored based on the specified language, ensuring accessibility for diverse audiences.

## Features
- **Multi-language Support:** Auto Dock supports multiple languages, allowing users to generate documentation in English, Russian, Ukrainian, Chinese, Spanish, and Polish.
- **File Filtering:** Users can specify files to be ignored during the documentation generation process.
- **Asynchronous Processing:** The tool can handle multiple files and generate documentation in a time-efficient manner, utilizing threading for time management.
- **Prompt Customization:** The generation of prompts is dynamic and customized according to the language and project name, ensuring clarity and relevance.
- **Progress Tracking:** Provides visual feedback on the documentation generation process with progress bars.

## Structure
The project consists of several key components:
- **config.py:** Defines language mappings and generates language-specific prompts.
- **main.py:** Implements the core functionality for file scanning, code reading, prompt generation, and interaction with the language model.
- **utilities.py:** Contains helper functions for styling text in the console and managing progress.
- **providers_test.py:** Allows for testing different providers for the language model, ensuring functionality and responsiveness.
- **requirements.txt:** Lists necessary dependencies for the project.

## Usage
To use Auto Dock, you must first set up your environment and install the required packages listed in `requirements.txt`. The primary entry point for the application is `main.py`, which accepts command-line arguments for project name, root directory, ignored files, and language preferences.

Here’s a basic command structure:

```bash
python main.py --name_project=YourProjectName --root_dir=YourProjectDirectory --ignore='["ignored_file.py"]' --languages='["en"]'
```

After executing the command, Auto Dock will scan the specified directory, generate documentation for each included file based on the stored prompts, and save the output to a markdown file (defaulted to README.md) in the specified language.# ./config.py

## Overview
The `config.py` file defines a dictionary for language types and a class `GenerateLanguagePrompt` that generates prompts based on the specified languages. It is designed to facilitate the creation of consistent documentation in multiple languages using a specific format.

## Features
- A dictionary `language_type` that maps language codes to their respective indices.
- The `GenerateLanguagePrompt` class that:
  - Initializes with a dictionary of languages.
  - Generates prompts for each language available in the `language_type` dictionary.
  - Provides a method to create a base prompt for documentation purposes.

## Structure
- **Dictionary**:
  - `language_type`: Contains language codes as keys (e.g., "en", "ru") and their respective integer values.

- **Class**:
  - `GenerateLanguagePrompt`: 
    - **Methods**:
      - `__init__(self, languages: dict[str, int])`: Initializes the class with the provided dictionary of languages.
      - `generate(self) -> dict`: Generates and returns a dictionary of language prompts.
      - `gen_prompt(self, language: str) -> list[str]`: Creates a list of base prompts formatted for the specified language.

## Usage
To use the functionality provided in `config.py`, follow these steps:

1. **Initialize the Prompt Generator**:
   - Create an instance of `GenerateLanguagePrompt` by passing the `language_type` dictionary.

   ```python
   GLP = GenerateLanguagePrompt(language_type)
   ```

2. **Generate Prompts**:
   - Call the `generate()` method of the instance to retrieve a dictionary of prompts for each language.

   ```python
   language_prompt = GLP.generate()
   ```

3. **Get List of Languages**:
   - You can also access the list of available languages through the `keys()` method of the `language_type` dictionary to see which languages are supported.

   ```python
   print(list(language_type.keys()))
   ```

### Method Descriptions
- `__init__(self, languages: dict[str, int])`: 
  - Initializes a new instance of `GenerateLanguagePrompt` with the provided dictionary of languages. Creates a list of language keys stored in `self.languages`.

- `generate(self) -> dict`:
  - Iterates over the list of languages and calls `gen_prompt()` for each language to generate a dictionary containing a language index as the key and the corresponding prompt as the value.

- `gen_prompt(self, language: str) -> list[str]`:
  - Takes a language code string and returns a list containing prompts specifically formatted for documentation in that language. Each prompt adheres to a specific structure that encourages consistency and clarity in documentation.# Overview

`main.py` is a Python script designed to automate the process of generating documentation for a software project. It scans a specified directory for code files, collects their content, and uses a language model (GPT) to generate documentation based on this content. The generated documentation can be saved into a markdown file.

# Features

- **Directory Scanning**: Ability to recursively scan through directories and collect file paths while ignoring certain specified files.
- **Code Extraction**: Reads the contents of the identified files to prepare prompts for documentation generation.
- **Documentation Generation**: Utilizes a GPT language model to create documentation based on the extracted code.
- **Response Handling**: Capable of combining responses from the language model for enhanced documentation.
- **File Saving**: Saves the generated documentation in a specified format and location.

# Structure

The code consists of several classes, each responsible for a specific aspect of functionality:

- **ReqHendler**: Manages the retrieval of files from the given directory and processes their content.
  - `get_files_from_directory()`: Scans the directory for files to include.
  - `is_ignored()`: Checks if a file is in the ignore list.
  - `get_code_from_file()`: Reads the content of the collected files.
  - `make_prompt()`: Constructs a prompt to be sent to the GPT model.

- **GptHandler**: Interfaces with the GPT model to get responses based on the constructed prompts.
  - `get_answer()`: Sends a prompt to the GPT model and retrieves the response.

- **AnswerHandler**: Manages generated responses and facilitates saving the final documentation.
  - `save_documentation()`: Saves the documentation to a markdown file.
  - `combine_response()`: Appends new responses to existing ones.
  - `make_start_req_form()`: Creates a structured initial prompt for requests.

- **AutoDock**: Orchestrates the overall process from code retrieval to documentation generation and saving.
  - `get_response()`: Collects responses for each code file.
  - `save_dock()`: Saves the final generated documentation.

# Usage

To run the script, execute it with the required parameters from the command line:

```bash
python main.py --name_project <project_name> --root_dir <directory_path> --ignore <files_to_ignore> --languages <languages_list>
```

### Parameters:
- `--name_project`: Specifies the name of the project.
- `--root_dir`: The root directory to scan for code files.
- `--ignore`: A list of files or patterns to ignore during the scanning.
- `--languages`: A list of language preferences, where the first item will be used for documentation.

### Method Descriptions:

- **ReqHendler**:
  - `get_files_from_directory(current_path: str = "")`: Recursively scans the specified root directory to find files that are not ignored, storing the paths in `self.all_files`.
  - `is_ignored(path: str) -> bool`: Checks if a given file path is in the ignore list.
  - `get_code_from_file()`: Reads the content of each file in `self.all_files` and stores it in `self.codes`.
  - `make_prompt() -> str`: Constructs prompts based on the project's name and collected codes for use with the GPT model.

- **GptHandler**:
  - `get_answer(prompt: str) -> str`: Sends a prompt to the GPT model and retrieves the generated answer.

- **AnswerHandler**:
  - `save_documentation(name: str = "README.md")`: Saves the combined answer content into a specified markdown file.
  - `combine_response(new_response: str)`: Combines a new response with existing ones.
  - `make_start_req_form(prompt: str) -> list`: Prepares the structure for the initial request to the GPT.

- **AutoDock**:
  - `get_response(codes: dict) -> AnswerHandler`: Manages the interaction with the GPT model to generate responses for the collected code files.
  - `get_part_of_response(prompt: str, answer_handler: AnswerHandler = None) -> AnswerHandler`: Sends a prompt to the GPT and combines responses.
  - `save_dock(answer_handler: AnswerHandler, name: str = "Readme_files/README") -> None`: Saves the completed documentation using the provided answer handler.# Overview

The `./providers_test.py` file provides a testing framework for evaluating various providers of a chat model using the `g4f` library. It employs multithreading to handle timeouts while testing the API responses from different providers, displaying progress in a user-friendly manner through a progress bar.

# Features

- **Timeout Control**: Implements a decorator to manage and control execution time limits for provider tests.
- **Dynamic Text Styling**: Utilizes the `colorama` library for coloring text output in the console, enhancing user interaction.
- **Progress Visualization**: Displays a progress bar indicating which provider is currently being tested and the completion percentage.
- **Provider Testing**: Fetches available providers from the `g4f` library and tests each one to check for responsiveness and validity.

# Structure

- **Functions**:
  - `timeout_control(timeout)`: A decorator function that enforces a timeout for any function it decorates.
  
- **Classes**:
  - `TextStyle`: Handles coloring of texts using `colorama`.
    - `get_text`: Returns a formatted string with specified text color and background.
  
  - `ProgressBar`: Manages progress display for provider tests.
    - `progress`: Updates and prints the current progress in the console.
  
  - `ProviderTest`: The core class for testing providers.
    - `__init__`: Initializes the class with a model name.
    - `get_providers`: Retrieves the list of available providers from the `g4f` library.
    - `test_provioder`: Tests the individual provider and returns its status and response.
    - `test_provider_timeout`: A method decorated with timeout control for testing the provider response.
    - `test_providers`: Iterates through all providers and tests them, collecting results.

# Usage

To run the script, execute it from the command line with the necessary argument specifying the model name to test:

```bash
python ./providers_test.py --name_model <model_name>
```

### Methods Description

- **timeout_control(timeout)**: 
  - A decorator that wraps a function to ensure it runs within a specified timeout period. If the function does not finish within the timeout, it returns `None`.

- **TextStyle Class**: 
  - **`get_text(text: str, color: any = "", back: any = "") -> str`**: 
    - Formats and returns the input text with desired foreground color and background color using `colorama`.

- **ProgressBar Class**: 
  - **`__init__(part)`**: 
    - Initializes the progress bar with the total number of providers.
  - **`progress(name)`**: 
    - Updates the progress bar on the console for the current provider being tested and prints the progress percentage.

- **ProviderTest Class**: 
  - **`__init__(model_name: str)`**: 
    - Sets the model name for API interaction.
  - **`get_providers()`**: 
    - Retrieves a list of provider names available in the `g4f` library and initializes the progress bar.
  - **`test_provioder(provider_name: str) -> tuple[bool, str]`**: 
    - Tests if the specified provider responds correctly. Returns a tuple indicating success (bool) and the response (str).
  - **`test_provider_timeout(provider)`**:
    - Tests the interaction with a provider and returns its response, adhering to the timeout control.
  - **`test_providers()`**: 
    - Iterates over all providers, tests each one, and collects successful responses, printing the results at completion.# Overview

The `requirements.txt` file specifies the dependencies needed for a Python project to function correctly. This file is essential for managing package installations and ensuring that the project runs with the appropriate versions of the libraries.

# Features

- Lists all required libraries and their specific versions.
- Facilitates easy installation of dependencies using package management tools like `pip`.
- Enhances project portability, allowing other developers to replicate the development environment effortlessly.

# Structure

The `requirements.txt` file contains a simple list of packages, each on a new line, alongside their version specifications. For example:

```
colorama==0.4.6
g4f==0.3.8.0
```

Each line corresponds to a library name followed by its version number in the format `library_name==version`.

# Usage

To install the dependencies specified in the `requirements.txt` file, use the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

This command reads the file line by line, installing each specified package at the defined version. This ensures that your project has the correct environment and dependencies required for its execution.# Overview

The `utilities.py` module provides utilities for terminal output enhancement, specifically through styled text and progress bars. It utilizes the `colorama` library for coloring text in the terminal, allowing users to create visually appealing command-line interfaces. 

# Features

- **Text Styling**: The module can generate colored text and background styles for terminal outputs.
- **Progress Bar**: A progress bar implementation that updates in real-time to show the completion percentage of tasks.
- **Time Management**: A decorator to measure and display the execution time of functions.

# Structure

The `utilities.py` file consists of two main classes:

1. **TextStyle**: Handles styling text with different colors and backgrounds.
2. **ProgressBar**: Provides functionality to display and update a progress bar in the terminal. 

Additionally, there are utility functions to start the progress bar and to time function execution.

# Usage

### TextStyle Class

- **`TextStyle()`**: Initializes the TextStyle instance and sets up colorama.

- **`get_text(self, text: str, color: any = "", back: any = "") -> str`**: 
  - **Parameters**:
    - `text`: The text string to be styled.
    - `color`: (optional) A color style from the `colorama` library.
    - `back`: (optional) A background color style from the `colorama` library.
  - **Returns**: A styled text string.

### ProgressBar Class

- **`ProgressBar(part)`**: 
  - **Parameters**:
    - `part`: An integer representing the number of parts for progress calculation.
  - Initializes the progress bar state.

- **`progress(self, name)`**: 
  - **Parameters**:
    - `name`: A string indicating the name of the task being tracked.
  - Updates the progress bar in the terminal.

### Functions

- **`start(part)`**: 
   - **Parameters**:
     - `part`: Number of parts for the progress bar.
   - Initializes the global `ProgressBar` instance.

- **`time_manager(func)`**: 
   - A decorator that wraps a function to track its execution time:
     - Displays the start and end of the function's execution, along with the elapsed time in seconds. 
   - **Parameters**: 
     - `func`: The function to be decorated.
   - **Returns**: The result of the wrapped function. 

### Example Usage

```python
from utilities import start, time_manager

@time_manager
def example_task():
    # Simulate some work
    for _ in range(5):
        time.sleep(1)  # simulate a task taking some time

if __name__ == "__main__":
    start(part=5)
    example_task()
```

In this example, the progress of `example_task` is displayed on the terminal with styled text and a progress bar.