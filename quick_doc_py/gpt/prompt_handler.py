class PromptGenerator:
    def __init__(self, prompt_data, language="en"):
        self.prompt_data = prompt_data
        self.language = language

    def get_prompts_for_files(self):
        all_prompts = []
        for file_path in self.prompt_data:
            all_prompts.append(f"{str(self.prompt_data)} from this code write documentation in {self.language} for the file {file_path}")

        return all_prompts
    
    def get_main_prompt(self):
        return f"Write main idea and easy exaple of usage in {self.language} for the following code: {str(self.prompt_data)}"
    
