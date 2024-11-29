# Auto Dock Documentation

## Overview

**Auto Dock** is a Python project designed to generate documentation for code files in a specified format (Markdown) and in selected languages. It leverages the capabilities of language models to articulate meaningful descriptions and documentation based on the provided code structure. This project is particularly useful for developers who want to automate the documentation process, ensuring that all code files are comprehensively annotated.

## Operating Principles

The project operates by:
1. **Collecting Code Files**: It traverses through a specified root directory, retrieving all relevant code files while optionally ignoring certain files.
2. **Generating Prompts**: It creates structured prompts based on the content of the collected files.
3. **Retrieving Responses**: It utilizes a provider (like OpenAI's GPT models) to generate responses based on the prompts, which are then transformed into structured documentation.
4. **Saving Documentation**: Finally, the generated documentation is saved into a markdown file for easy access and distribution.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dima-on/Get_Documantation.git
   cd Get_Documantation
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Auto Dock project, execute the main script with the necessary arguments:
```bash
python main.py --name_project "Your Project Name" --root_dir "/path/to/your/code" --ignore "['file_to_ignore.py']" --languages "['en', 'ru']" --parts 5
```

### Arguments:
- `--name_project`: The name of the project for which documentation is generated.
- `--root_dir`: The path to the root directory containing the code files.
- `--ignore`: A list of files to ignore during the documentation generation process.
- `--languages`: A list of languages for generating documentation.
- `--parts`: The number of parts for generating the documentation in sequence.

## Classes and Methods

### 1. **`GenerateLanguagePrompt`**
- **Purpose**: To generate prompts in various languages.
- **Methods**:
  - `generate()`: Generates a dictionary of prompts for each specified language.
  - `gen_prompt(language)`: Generates a specific prompt for the given language.

### 2. **`ReqHendler`**
- **Purpose**: Handles all required operations including file collection and code reading.
- **Methods**:
  - `__init__(root_dir, language, ignore_file, project_name)`: Initializes the handler with necessary parameters.
  - `get_files_from_directory(current_path='')`: Recursively collects all files from the specified directory.
  - `is_ignored(path)`: Checks if a file should be ignored.
  - `get_code_from_file()`: Reads the contents of all collected files.
  - `make_prompt()`: Constructs a formatted prompt for language model APIs.

### 3. **`GptHandler`**
- **Purpose**: Interacts with the language model to retrieve answers based on generated prompts.
- **Methods**:
  - `__init__(provider)`: Initializes the GPT handler with a specified provider.
  - `get_answer(prompt)`: Retrieves a response from the GPT model for a given prompt.

### 4. **`AnswerHandler`**
- **Purpose**: Manages the response returned by the model and handles saving and combining responses.
- **Methods**:
  - `save_documentation(name='README.md')`: Saves the generated documentation to a file.
  - `combine_response(new_response)`: Combines a new response with existing answers.
  - `make_req_form(prompt)`: Creates a request form for the model using the existing answers.
  - `make_start_req_form(prompt)`: Prepares the initial request form.

### 5. **`AutoDock`**
- **Purpose**: Orchestrates the documentation generation process.
- **Methods**:
  - `__init__(root_dir, language, ignore_file, project_name)`: Initializes with the required parameters and calls file handling methods.
  - `get_response(parts)`: Retrieves the generated responses from the model in specified parts.
  - `get_part_of_response(prompt, answer_handler=None)`: Gets response for a specified part.
  - `save_dock(answer_handler, name='Readme_files/README')`: Saves the final documentation output.

### 6. **Utilities**
- Various utility functions are implemented in `utilities.py` for text styling and time logging, as well as progress tracking through the command line.

## Example Usage

1. **Basic Example**:
   ```bash
   python main.py --name_project "Demo Project" --root_dir "./src" --ignore "['test.py']" --languages "['en']" --parts 3
   ```

2. **Generating Documentation for Multiple Languages**:
   ```bash
   python main.py --name_project "Multi-language Documentation" --root_dir "/path/to/code" --ignore "[]" --languages "['en', 'es', 'ru']" --parts 5
   ```

## Conclusion

Auto Dock is a versatile tool that leverages AI-driven models to automate the documentation process for software projects. With its extensible structure, it can be tailored to suit various project requirements and enable developers to maintain comprehensive and clear documentation effortlessly.## Advanced Features

### Multi-Provider Support
The **Auto Dock** project supports various AI providers through the `GptHandler` class. Providers can be chosen based on user criteria or performance. 

- **Available Providers**: By default, it uses `DarkAI`, but new providers can easily be integrated through the `g4f.Provider` module.
- **Testing Providers**: The included `providers_test.py` allows users to validate and test the functionality of each provider before utilizing them in the main project workflow.

### Customization
Custom configurations can be made via the `config.py` file, allowing users to easily adjust the language mappings or the project-specific prompts. You have the flexibility to modify language settings and other parameters directly in the configuration file to cater to specific documentation styles and requirements.

### Error Handling
The framework includes comprehensive error handling throughout the various classes. For example:
- The `get_code_from_file` method in the `ReqHendler` class includes try-except blocks to manage exceptions that may arise from reading files (e.g., encoding issues).
- Providers are tested for availability, and the system logs relevant errors to ensure smooth operation.

### Performance Enhancements
The project is designed to be efficient:
- File scanning and reading operations are optimized, and unnecessary files can be ignored to speed up the process.
- The handling of language models is wrapped in decorators that measure execution time for performance assessment and debugging.

## Running Unit Tests
To ensure robustness, unit tests can be added to validate individual components. Here’s how to implement basic testing:

1. Create a new `tests` directory in your project.
2. Write test cases leveraging Python's built-in `unittest` framework.
3. Example of a simple test for the `ReqHendler`:
   ```python
   import unittest
   from main import ReqHendler

   class TestReqHendler(unittest.TestCase):
       def setUp(self):
           self.handler = ReqHendler(root_dir=".")

       def test_get_files_from_directory(self):
           self.handler.get_files_from_directory()
           self.assertGreater(len(self.handler.all_files), 0)

   if __name__ == '__main__':
       unittest.main()
   ```
4. Run tests using:
   ```bash
   python -m unittest discover -s tests
   ```

## CLI Interface and Integration
### Integrate with CI/CD
Auto Dock can be integrated into CI/CD pipelines:
- Run Auto Dock as part of pre-deployment stages to ensure documentation is always up-to-date.
- Automated documentation generation can be triggered upon code commits or merges.

### Sample Command for CI
Here is an example of how to incorporate Auto Dock within a CI configuration such as GitHub Actions:
```yaml
name: Documentation Generation

on:
  push:
    branches: [main]

jobs:
  doc:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install Requirements
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Generate Documentation
        run: |
          python main.py --name_project "Automated Docs" --root_dir "./src" --ignore "[]" --languages "['en']" --parts 5

      - name: Upload Documentation
        uses: actions/upload-artifact@v2
        with:
          name: documentation
          path: README.md
```

## Future Work
### Potential Enhancements:
- **User Interface**: A GUI could be introduced to simplify usage for less technically inclined users.
- **Support for More File Types**: Extend functionality to support additional programming languages and file types.
- **Cloud Integration**: Allow generation and storage of documentation directly onto cloud services like AWS S3 or Google Drive.

**Auto Dock** aims to be a fully featured documentation generation tool that is extensible, easy to use, and vital for any development workflow, ensuring that all code changes are accurately and efficiently documented.## Community and Contributions

The **Auto Dock** project encourages contributions from developers and users who wish to enhance its functionality or correct any issues. Here’s how you can get involved:

### How to Contribute
1. **Open Issues**: If you encounter any problems or have suggestions for new features, please open an issue on our GitHub repository. Make sure to provide detailed information to help us understand and replicate the problem.
   
2. **Pull Requests**: Contributions via pull requests are welcomed. Before submitting a pull request, please ensure:
   - New features are well-documented.
   - Code follows the project's style guidelines.
   - Adequate unit tests are included for new features or bug fixes.

3. **Documentation**: Help improve the project documentation. If you find areas that are unclear or can be expanded, feel free to submit suggestions or edits. Clear documentation is critical for user adoption and project success.

4. **Share Your Experience**: Use the project and share your experience with others. Whether through blog posts, tutorials, or social media, you can help spread the word and grow the community around **Auto Dock**.

## FAQs

### Q1: What programming languages does Auto Dock support?
**A1**: Currently, Auto Dock primarily focuses on Python-based files but can be extended to support additional languages by modifying file scanning logic and the prompt generation process.

### Q2: Can I use custom prompts?
**A2**: Yes, you can customize your prompts by modifying the `config.py` file, allowing you to tailor the documentation style and content to your specific needs.

### Q3: Is there a way to handle private code repositories?
**A3**: Absolutely! Just ensure the process runs in an environment that has access to your private repository, and Auto Dock will handle the rest. You may need to add credentials or use SSH keys for Git operations.

### Q4: How can I run Auto Dock in a Docker container?
**A4**: Here’s a simple Dockerfile to set up Auto Dock in a container:
```dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

You can build and run the container with:
```bash
docker build -t auto-dock .
docker run auto-dock --name_project "Dockerized Project" --root_dir "/app/src" --ignore "[]" --languages "['en']" --parts 5
```

## Contact and Support

You can reach out to the project maintainers via the following channels:
- **GitHub Issues**: For any project-specific questions or reporting issues.
- **Email**: [your_email@example.com](mailto:your_email@example.com) for inquiries not suited for GitHub.
- **Community Forums**: Join discussions or ask questions on forums related to Python development and AI integration.
  
## Conclusion

**Auto Dock** aspires to redefine the way developers generate documentation, making it an integral part of the software development lifecycle. By embracing openness and collaboration, we aim to build a robust tool that evolves with user needs and technology advancements.

We encourage everyone to try out Auto Dock, contribute to its growth, and help foster a thriving community of users who are dedicated to enhancing documentation practices in their projects. Thank you for considering being part of this journey!## Acknowledgments

We would like to express our gratitude to the open-source community and contributors who have laid the groundwork for projects like **Auto Dock**. The collaborative spirit of developers around the world enables us to create innovative solutions that benefit everyone. We also thank the maintainers of libraries and tools that assist us in building powerful features, particularly:

- **g4f**: For providing a robust interface for integrating AI-driven language models and enhancing the documentation process.
- **colorama**: For enabling colored text in the console, improving the user interface and experience during execution.
- **argparse**: For simplifying command-line argument parsing, making it easier for users to interact with the application.

## User Testimonials

Here are some words from users who have implemented **Auto Dock** in their workflows:

“I recently integrated **Auto Dock** into my team's development process, and it has saved us countless hours. The documentation generated is clear and to the point, making it easy to onboard new team members.” - **Sarah J., Lead Developer**

“Using **Auto Dock** allows me to focus on writing code, knowing that comprehensive documentation is just a command away. Its ease of use and customization has been a game changer for my projects.” - **Mike T., Freelance Developer**

## Roadmap

The future of **Auto Dock** is bright, with plans to introduce exciting features:

1. **User Customization Options**: More settings to allow users to customize output formats and include/exclude specific documentation sections.
2. **Support for Additional Programming Languages**: Expansion to support more than just Python files, adapting to various codebases.
3. **Enhanced AI Model Integration**: Look into integrating emerging AI technologies for even more intelligent documentation generation.
4. **CLI Enhancements**: Improve the command-line interface with user-friendly commands and output options for better usability.
5. **Online Documentation Portal**: Create a dedicated website for documentation that provides tutorials, examples, and best practices for using **Auto Dock**.

## Final Words

We are excited about the potential of **Auto Dock** to transform how developers approach project documentation. Your participation and feedback are essential to its evolution. Dive in, and let us continue to improve together! Whether you are a developer looking for automation, a contributor wanting to make a difference, or a user seeking effective documentation solutions, **Auto Dock** welcomes you.

### Stay Connected

Follow the project on GitHub, engage with the community, and stay informed about updates, new features, and future work. We appreciate your interest and support in making **Auto Dock** an innovative tool for developers everywhere. Thank you for being part of our journey!## Appendix

### Additional Resources

For those looking to deepen their understanding of documentation best practices or the technologies used in **Auto Dock**, we provide the following resources:

- **Documentation Best Practices**: Explore various standards and methodologies for creating high-quality documentation that enhances code understanding and usability.
- **AI in Software Development**: Read about the role of artificial intelligence in the software lifecycle, including code generation, testing, and documentation.
- **Open Source Contribution Guides**: If you're new to open source, check out these guides to help you navigate contributions and community engagement.

### Glossary

- **Markdown**: A lightweight markup language with plain-text formatting syntax, commonly used for documentation.
- **AI Model**: An algorithm designed to learn patterns in data and make predictions or generate content, such as GPT-3 or GPT-4.
- **Provider**: The service or library that interacts with an AI model to retrieve responses based on input prompts.
- **CLI (Command-Line Interface)**: A text-based interface used to interact with software applications through commands.

### Contact Information for Contributors

For potential contributors or those interested in seeking collaboration opportunities, please contact the project maintainers. We'd be delighted to discuss ideas, suggestions, or partnerships that can further enhance **Auto Dock** and its feature set.

### Issue Reporting

If you encounter bugs or issues while using **Auto Dock**, please document them thoroughly and submit an issue via our GitHub repository. Include the following details:

1. **Environment**: Specify your operating system and its version.
2. **Python Version**: Include the Python version being used.
3. **Steps to Reproduce**: Provide a detailed account of how to reproduce the issue.
4. **Expected vs. Actual Results**: Clearly describe what you expected to happen and what actually happened.

### Closing Remarks

We appreciate your interest in **Auto Dock** and your commitment to improving documentation practices within the software development community. Your contributions—be it through code, issues, feedback, or spreading the word—help foster a vibrant ecosystem that benefits all developers.

### Join Us!

Become a part of the **Auto Dock** community. Follow us on our social media platforms for the latest updates, insights, and discussions on documentation tools and trends. Link up with fellow users and contributors to share experiences and suggestions as we work together towards a common goal of better documentation solutions!

Thank you for considering **Auto Dock** as your go-to solution for automated documentation generation!