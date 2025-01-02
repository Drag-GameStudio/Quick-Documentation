Overview:
The `Quick-doc-py` is a Python library designed to create documentation for your projects quickly using AI models like gpt-3.5-turbo or gpt-4. 

Features:
- Generate documentation using AI models
- Supports multiple languages such as English, Russian, Ukrainian, Chinese, Spanish, and Polish
- Customizable prompts for documentation generation
- Ability to ignore specific files or directories
- Adds ability to work with Git repositories

Structure:
- `./.gitignore`: File that contains all ignored files and directories for Git.
- `./pyproject.toml`: File that defines the project settings and dependencies such as Python version and required packages (colorama, g4f, requests).
- `./quick_doc_py/`: Directory that contains main classes, config, and utility functions for generating documentation.
  - `config.py`: File with language codes, ignored files, and GPT models.
  - `log_logic/req.py`: Contains the `ReqToServer` class responsible for handling requests to the server.
  - `main.py`: File containing the main function and classes responsible for handling the overall documentation process.
  - `providers_test.py`: Script to test g4f model providers for compatibility.
  - `utilities.py`: File with utility functions and classes like `TextStyle`, `ProgressBar`, and `time_manager`.
  
Usage:
To generate documentation for your project, run the following command in your terminal or command prompt:

```
python -m quick_doc_py.main --name_project "Your_project_name" --root_dir /path/to/your/projects --ignore "['*.venv', '*.git', '*.venv', '*.gitignore']" --languages "[ 'en', 'ua']" --gpt_version "gpt-3.5-turbo" --provider "Mhystical" --general_prompt "Additional wishes: " --default_prompt "Write general idea of code in Markdown (use Google Style).
```

You can also create a file called `setup.cfg` in your project root and add commands to `entry_points` like this:

```
[options.entry_points]
console_scripts=[
    'gendoc = quick_doc_py.main:main'
]
```

This will allow you to generate documentation by running the following command:

```
gendoc --name_project "Your_project_name" --root_dir /path/to/your/projects --ignore "['*.venv', '*.git', '*.venv', '*.gitignore']" --languages "[ 'en', 'ua']" --gpt_version "gpt-3.5-turbo" --provider "Mhystical" --general_prompt "Additional wishes: " --default_prompt "Write general idea of code in Markdown (use Google Style).
```

The generated documentation will be saved in the project directory as `README.en.md`, `README.ua.md`, etc., corresponding to the selected language.
# File Documentation

## Usage

This `.gitignore` file is used to specify files and directories that should be ignored by Git version control. By placing specific entries in this file, Git will exclude those items from being tracked or uploaded to the repository.

To customize the `gitignore` file based on your project requirements, simply add the desired file or directory paths to this file. Each entry should be placed on a new line and can include wildcard characters for pattern matching. For example:
- `/__pycache__`: Ignores the `__pycache__` directory.
- `*.pyc`: Ignores all files with the `.pyc` extension.

Once the desired entries are added, execute the following Git commands to apply the changes:
```
$ git add .gitignore
$ git commit -m "Add custom gitignore settings"
$ git push
```

After pushing the changes, files and directories specified in the `.gitignore` file will no longer be committed to the repository.

For more information about the `.gitignore` file, visit the following link: [Gitignore Documentation](https://git-scm.com/docs/gitignore)

## Methods

#### N/A
(This is an addition to the partial documentation, as the complete documentation is not being requested.)

---

*Note: This documentation is a supplementary addition, and the full documentation was not composed in this response.*
# pyproject.toml Documentation

## Usage

This `pyproject.toml` file is used to manage dependencies and build settings for projects created with Python. It is particularly useful for specifying the required dependencies for your project and handling the build process.

Here's a brief explanation of each section in the file:

## Sections

### [tool.poetry]

This section specifies general settings for your project:

- `name`: The name of the package.
- `version`: The version of the package.
- `description`: A brief description of the package.
- `authors`: The author(s) of the package and their contact information.
- `readme`: The path to the README file.
- `packages`: A list of packages to include in the project.
- `repository`: The repository URL for the project.

### [tool.poetry.scripts]

This section specifies the script names and their corresponding entry points:

- `gen-doc`: Generates documentation for the project.
- `providers-test`: Runs tests for providers implemented in the project.

### [tool.poetry.dependencies]

This section specifies the dependencies required for your project:

- `python`: Default Python version to use when running the project.
- `colorama`: Library for cross-platform color support in terminal applications.
- `g4f`: Library for colored output log formatting.
- `requests`: Library for making HTTP requests in Python.

### [build-system]

This section specifies the build system requirements and settings:

- `requires`: The required build system dependencies.
- `build-backend`: The build backend (Poetry's `poetry.core.masonry.api`) to be used for assembling the project.

By understanding the various sections and settings in this file, you can effectively manage dependencies, generate documentation, and configure your project for an efficient development process.
# config.py

This document describes how to use the `config.py` file, including its methods and parameters.

## Language Type
The `LANGUAGE_TYPE` constant is a dictionary where the keys are language names in string format, and the values are integer codes corresponding to those languages. For example:

```python
LANGUAGE_TYPE = {
    "en": 0,    # English
    "ru": 1,    # Russian
    "ua": 2,    # Ukrainian
    "chs": 3,   # Simplified Chinese
    "es": 4,    # Spanish
    "pl": 5     # Polish
}
```

## Ignored Files
The script provides two lists, `DEFAULT_IGNORED_FILES` and `GIT_IGNORED_FILES`, containing patterns of files to be ignored.

- `DEFAULT_IGNORED_FILES`: Patterns including README files, cache folders, and dist folders.
- `GIT_IGNORED_FILES`: Patterns like GitHub folders, Git folders, virtual environment folders, and `.gitignore` files.

## GPT_MODELS
`GPT_MODELS` is a list consisting of two strings representing GPT model names: "gpt-4" and "gpt-3.5-turbo".

## GenerateLanguagePrompt Class
The `GenerateLanguagePrompt` class is used to generate language-specific prompts. It is initialized with a dictionary of languages and their corresponding integer codes.

### generate() method
```python
def generate(self) -> dict:
```
Generates a dictionary with prompts for different languages, where keys are integer codes representing the languages and values are language-specific prompts.

### gen_prompt() method
```python
def gen_prompt(self, language: str) -> list[str]:
```
Generates a list of prompts corresponding to the given language. The prompts include:

1. A general idea of Markdown code in the mentioned language.
2. The name of the project.
3. A description of how to write documentation for the given file in Markdown, focusing on usage and method descriptions, according to Google Style.

## Example
```python
GLP = GenerateLanguagePrompt(LANGUAGE_TYPE)
language_prompt = GLP.generate()

print(list(LANGUAGE_TYPE.keys()))
```

This example demonstrates how to create an instance of the `GenerateLanguagePrompt` class with the declared `LANGUAGE_TYPE`, generate language-specific prompts, and print available languages. The resulting prompts could be used by other parts of the application to instruct users on writing documentation for files in different languages following conventions like the Google Style.
# ReqToServer
This file contains the `ReqToServer` class which interacts with a server using HTTP requests. The class allows the creation of a new session and adding data to the current session.

## Usage
To start using this class, import it into your Python file:

```python
from quick_doc_py.log_logic.req import ReqToServer
```

Create an instance of the `ReqToServer` class by providing the server's URL (default is "https://sdwwwwsvbvgfgfd.pythonanywhere.com"). You can then use the following methods to interact with the server:

### Methods

#### `__init__(self, link: str = "https://sdwwwwsvbvgfgfd.pythonanywhere.com")`
Initializes the `ReqToServer` class providing the server's URL (default is "https://sdwwwwsvbvgfgfd.pythonanywhere.com").

#### `create_session(self) -> str`
Creates a new session on the server and returns the response text.

#### `add_to_session(self, session_code: str, data: dict) -> None`
Adds data to the current session using the provided session_code. The session_code is typically obtained from the `create_session` method.

Example usage:

```python
req = ReqToServer()

session_code = req.create_session()
data = {"key1": "value1", "key2": "value2"}

req.add_to_session(session_code, data)
```
**quick_doc_py/main.py**

This Python script automatically generates documentation for any project using the information from the source code files. It uses an AI model like ChatGPT to create the documentation with the user's prompts and setting preferences.

To use this script, set the preferences and run the script with the desired parameters.

**Usage**

To use this script, you need to pass a few arguments:

- `--name_project`: The name of your project.
- `--root_dir`: The location of your project.
- `--ignore`: A list of files to ignore during documentation generation (the list should be in the form of a string, where each file is a line, e.g., ["`*.pyc`", "`__pycache__/`"]).
- `--languages`: A list of languages to generate documentation in (the list should be in the form of a string, where each language is a line, e.g., ["`en`", "`es`"]).
- `--gpt_version`: (Optional) Version of the GPT model.
- `--provider`: (Optional) ChatGPT provider.
- `--general_prompt`: (Optional) General prompt for the model to generate documentation.
- `--default_prompt`: (Optional) Default prompt for specific files.
- `--with_git`: (Optional) Help to generate a `.gitignore` file for the project using the script.

To generate documentation for a project, you need to use the `main()` function and provide required arguments. The documentation will be saved in the designated folder with the language-specific file names.

```python
if __name__ == "__main__":
    main()
```

**Methods overview**

- `ReqHendler`: Searches for files in the specified directory, filters out ignored files, and collects the content of each file.
  - `__init__(root_dir, language, ignore_file, project_name)`: initializes a ReqHendler object.
  - `get_files_from_directory(current_path)`: Finds files within the given directory and its sub-directories, excludes ignored files.
  - `is_ignored(path)`: Checks if the given file or directory is in the ignored list.
  - `get_code_from_file()`: Reads the content of each file and stores it in a dictionary.
  - `make_prompt()`: Creates a prompt with the content of files in the project.

- `GptHandler`: Interacts with a ChatGPT model to generate responses using the user's prompts.
  - `__init__(provider, model)`: Initializes GptHandler object.
  - `get_answer(prompt)`: Sends a prompt to ChatGPT and gets the generated response.

- `AnswerHandler`: Receives responses from GptHandler and processes them to generate documentation.
  - `__init__(answer)`: Initializes an AnswerHandler object.
  - `combine_response(new_response)`: Appends a new response to the existing answer.
  - `save_documentation(name)`: Saves the generated documentation in a file.
  - `get_full_answer()`: Returns the final generated documentation.

- `AutoDock`: Main class, combines ReqHendler, GptHandler, and AnswerHandler functionalities to generate project documentation.
  - `__init__(root_dir, language, ignore_file, project, provider, gpt_model, general_prompt, default_prompt)`: Initializes AutoDock object.
  - `get_response(codes)`: Calculates the response for each file in the project using the GptHandler and processes the answers with AnswerHandler.
  - `get_part_of_response(prompt, answer_handler)`: Handling specific prompts for part of the response.
  - `save_dock(answer_handler, name)`: Saves the generated documentation.
  - `get_doc()`: Retrieves the generated documentation.

- `main()`: Main function where the arguments are parsed, and the documentation process starts.

**Example of running the script:**

```bash
python main.py --name_project "MyProject" --root_dir "./MyProject" --ignore "['*.pyc', '__pycache__/', 'venv/']" --languages "['en', 'es']"
```

This will generate documentation in both English and Spanish for the "MyProject" project.

# Providers Test Documentation

This documentation provides an overview of the `providers_test.py` file, focusing on the usage and description of methods.

The purpose of this script is to test various providers in the `g4f` library and check which ones work successfully.

## Classes

### ProgressBar

The `ProgressBar` class is responsible for creating and updating a progress bar for the testing process. It takes a single parameter in its constructor:

- `part` (int): The total parts of the task.

#### Methods

- `progress(name)`: Updates the progress bar with the given name.

### TextStyle

The `TextStyle` class helps in formatting text with colors and backgrounds for the console output.

#### Methods

- `get_text(text, color=None, back=None)`: Returns the input text with specified color and background. If color or background is not given, no formatting is applied.

### ProviderTest

The `ProviderTest` class handles testing of different providers in the `g4f.Provider` module. It takes the following parameters in its constructor:

- `model_name` (str): The name of the model to be used for testing.

#### Methods

- `get_providers()`: Retrieves the list of providers from the `g4f.Provider` module.
- `test_provioder(provider_name)`: Tests a given provider and checks if it works or not.
- `test_provider_timeout(provider)` (timeout_control): Tests the given provider with a timeout of 30 seconds.
- `test_providers()`: Tests all the available providers and returns those that work.

### Functions

#### provider_test(model_name)

This function initializes the `ProviderTest` class and tests all the available providers.

- `model_name` (str): The name of the model to be used for testing.

#### main()

The main function presents an `argparse` interface to allow input of the model name as command-line argument. It calls the `provider_test` function and prints the result.
# utilities.py

This module provides utilities for managing the progress bar, coloring text, and timing function execution. The following functions and classes are now available for usage:

## ProgressBar Class

**Purpose**: Helps create a simple progress bar to visualize operation progress.

### Methods:
- __init__(self, part): Initializes the progress bar with the given part.
- progress(self, name): Updates and prints the progress bar indicating the current operation.

### Usage:
```python
bar = ProgressBar(part=1)  # Initializes a progress bar for part 1

bar.progress('Initialization')  # Prints progress bar
```

## TextStyle Class

**Purpose**: Helps colorize the console output to make it more readable.

### Methods:
- get_text(self, text, color=*, back=*): Returns the input text with specified color and background.

### Usage:
```python
text_color = TextStyle()
colored_text = text_color.get_text('Hello', color=Fore.RED, back=Back.GREEN)  # Colored text
print(colored_text)
```

## Function decorators

### time_manager

**Purpose**: Adds a progress bar and measures the execution time of a given function.

### Usage:
```python
@time_manager
def example_function():
    time.sleep(3)  # Example operation
    return "Operation completed"

print(example_function())  # Returns the result of the operation with progress bar and time information
```

The provided decorators and classes can be modified according to your specific needs. They help you create more appealing and informative console outputs.
