   # Auto Dock Documentation

## Overview
Auto Dock is a CLI tool that generates documentation for a given Python project. It uses OpenAI's API (currently supporting GPT-3.5 Turbo and Dark AI) to interact with users and generate documentation based on their prompts. It allows users to focus on their coding tasks while Auto Dock generates comprehensive documentation for their project.

## Operating Principle
1. Users need to provide project details such as project name, root directory, ignore files, and language.
2. Auto Dock scans the specified directory and retrieves all files, except for those specified in `ignore_file`.
3. Auto Dock generates prompts based on language and project details.
4. Auto Dock sends the prompt to the chosen AI model to get responses.
5. Auto Dock will save the final documentation based on the user's input in the specified output file.

## Get Started
To use Auto Dock, make sure you have installed the required package:

```
$ pip install g4f==0.3.8.0
```

Users must specify the project's details through the command line:

```
$ python ./normal_main.py --name_project "Project Name" --root_dir "/path/to/procect/" --ignore '[ "ignore1.py", "ignore2.py"]' --language "en"
$ python ./normal_main.py --name_project "Project Name" --root_dir "/path/to/procect/" --ignore '[ "ignore1.py", "ignore2.py"]' --language "en" --parts 10
```

You can replace "Project Name", "/path/to/procect/", and '[ "ignore1.py", "ignore2.py"]' with your actual project information.

## Auto Dock Step by Step

### Initialize Auto Dock
```python
from auto_dock import AutoDock

auto_dock = AutoDock(
    root_dir="/path/to/procect/", 
    ignore_file=['ignore1.py', 'ignore2.py'],
    project_name="Project Name",
    language="en",
)
```

### Generate Response
```python
response_handler = auto_dock.get_response(parts=10)
```

### Save Dock
```python
response_handler.save_dock(name="README.md")
```

## Classes
### ReqHendler
The ReqHendler class is responsible for scanning the project directories, retrieving files, and filtering out ignored files.

#### Parameters:

- `root_dir`: The root directory of the project.
- `language`: The language type, default is "en".
- `ignore_file`: The list of files to ignore, default is None.
- `project_name`: The project name, default is "Python Project".

### GptHandler
The GptHandler class is responsible for setting the AI model to be used.

#### Parameters:
- `provider`: The AI model provider, default is "ChatGptEs".

### AnswerHandler
The AnswerHandler class is responsible for handling the response from the AI model and saving the final documentation.

#### Parameters:
- `answer`: The response content.
- `prompt`: The prompt used for this response.

### ProgressBar
The ProgressBar class is a utility class for tracking the progress of tasks.

#### Parameters:
- `part`: The number of parts for the task.

## Examples of Use

### Complete Example
Here's an example of how to use Auto Dock with command line arguments:

```python
import argparse
import ast
import os
import sys
import utilities
import g4f
import g4f.Provider
import config

sys.stdout.reconfigure(encoding='utf-8')

parser = argparse.ArgumentParser(description="Пример обработки параметров.")
parser.add_argument("--name_project", type=str, help="name of project", required=True)
parser.add_argument("--root_dir", type=str, help="root dir", required=True)
parser.add_argument("--ignore", type=str, help="ignor files", required=True)
parser.add_argument("--language", type=str, help="language", required=True)
parser.add_argument("--parts", type=int, help="parts", required=True)
args = parser.parse_args()

project_name = args.name_project
root_dir = args.root_dir
language = args.language
ignore_file = ast.literal_eval(args.ignore)
parts = args.parts

utilities.start(parts)

auto_dock = AutoDock(
    root_dir=root_dir,
    ignore_file=ignore_file,
    project_name=project_name,
    language=language
)

response_handler = auto_dock.get_response(parts=parts)
auto_dock.save_dock(answer_handler=response_handler, name="README.md")
```

## License
The license for the underlying `g4f` library is MIT License. The code for Auto Dock is also released under the MIT License. 

Check out the full source code on [GitHub](https://github.com/gy4gjr/Auto-Dock).   ## How to Use Auto Dock

Auto Dock is designed to be easy to use. To use Auto Dock, you need to follow these steps:

1. **Install the Required Package**:

   Install the g4f package using pip:

   ```
   $ pip install g4f==0.3.8.0
   ```

2. **Initialize Auto Dock**:

   Create an instance of the AutoDock class with the following parameters:

   - `root_dir`: The root directory of the project.
   - `ignore_file`: The list of files to ignore.
   - `project_name`: The project name.
   - `language`: The language type.

   ```python
   from auto_dock import AutoDock

   auto_dock = AutoDock(
       root_dir="/path/to/project/",
       ignore_file=['ignore1.py', 'ignore2.py'],
       project_name="Project Name",
       language="en",
   )
   ```

3. **Generate Response**:

   Generate a response using the `get_response` method of the AutoDock class. This will create a response handler that contains the response and prompt information.

   ```python
   response_handler = auto_dock.get_response(parts=10)
   ```

4. **Save Dock**:

   Save the generated documentation using the `save_dock` method of the response handler. This method will save the final documentation to the specified output file.

   ```python
   response_handler.save_dock(name="README.md")
   ```

That's it! Auto Dock automatically handles the rest of the process using OpenAI's API. The generated documentation will contain all the necessary information for your project.

## Conclusion

Auto Dock makes it easy for Python developers to generate documentation for their projects. With its powerful and flexible features, it saves time and effort while ensuring comprehensive content.

Want to learn more about how to use Auto Dock? Check out the full source code on [GitHub](https://github.com/gy4gjr/Auto-Dock), and feel free to ask any questions you have in the comments below.

This project is released under the MIT License. The underlying `g4f` library is also licensed under MIT License. If you have any questions or suggestions, please feel free to reach out to us. Happy coding!   ## Troubleshooting and Frequently Asked Questions

Here are some common questions and issues you might encounter when using Auto Dock:

### Q: What happens if I don't have the required package installed?

A: Auto Dock will fail to import the necessary module. You need to install the g4f package using pip before running the script:

```
$ pip install g4f==0.3.8.0
```

### Q: What if I encounter an API rate limit issue?

A: Auto Dock uses OpenAI's API, which has a rate limit of 2500 tokens per month for the free tier. If you exceed this limit, you will need to upgrade to a paid plan. Alternatively, you can choose Dark AI as your provider, which has more affordable and customizable options.

### Q: What are the benefits of using Auto Dock?

A: Auto Dock provides several benefits:

- It saves time and effort by automatically generating documentation for your Python projects.
- It allows you to focus on coding while Auto Dock handles the documentation process.
- It supports different AI models, including the popular GPT-3.5 Turbo and Dark AI.
- It supports multiple languages, allowing you to use Auto Dock in various development environments.
- It's easy to use, with clear documentation and step-by-step instructions.

### Q: Can I contribute to the development of Auto Dock?

A: Yes, you are welcome to contribute to the development of Auto Dock. You can submit pull requests to the [GitHub repository](https://github.com/gy4gjr/Auto-Dock) or create issues if you find any bugs or have feature requests. We appreciate all contributions to make Auto Dock even better.

### Q: Is there a community I can join to discuss Auto Dock?

A: Yes, you can join the [Auto Dock Discord community](https://discord.gg/kwvD kinda) to ask questions, share tips, or get help with any issues related to Auto Dock.

If you follow these guidelines, you'll have a smooth experience using Auto Dock. Happy coding with Auto Dock!   ## Extending Auto Dock

While Auto Dock is designed to be a powerful standalone tool for generating project documentation, it's also highly customizable. Here are some ways you can extend Auto Dock to better suit your development workflow:

1. **Customizing Prompts**: You can modify the prompts used by Auto Dock to fit your specific project needs. The prompts are defined in the `language_prompt` dictionary in the `config.py` file:

   ```python
   language_prompt = {
       0: ["Write documentation for this code in English using Markdown format.", "Project Name is:", "    "]
   }
   ```

   Feel free to modify these prompts as needed.

2. **Customizing the AI Model**: Auto Dock currently supports multiple AI models, such as GPT-3.5 Turbo and Dark AI. You can customize which model to use by setting the `provider` parameter when creating the `GptHandler` class:

   ```python
   GptHandler(provider="DarkAI")
   ```

   Dark AI is known for its superior speed and cost-effectiveness.

3. **Customizing the Response Handling**: Auto Dock's response handling is implemented in the `AnswerHandler` class. You can customize it according to your specific needs. For example:

   - You can save the result to a different file format, such as HTML or PDF.
   - You can add more information to the response before saving it.
   - You can validate the content before saving it, such as confirming the content meets your project's needs.

You can also explore additional ways to extend Auto Dock by checking the source code on [GitHub](https://github.com/gy4gjr/Auto-Dock). It's open-source, so you can modify and customize it as needed.

With these extensions, Auto Dock can become even more powerful and tailored to your specific project needs.

---

By following these guidelines, you'll have a better experience using Auto Dock. We hope this documentation helps you effectively use Auto Dock to streamline your development workflow. If you have any further questions, feel free to ask in the comments below. Happy coding with Auto Dock!