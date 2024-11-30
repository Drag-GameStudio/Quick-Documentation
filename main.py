import g4f
import g4f.Provider
import config
import os
import sys
import utilities
import argparse
import ast
import time

sys.stdout.reconfigure(encoding='utf-8')


class ReqHendler:
    def __init__(self, 
                 root_dir: str, 
                 language: str = "en", 
                 ignore_file: list[str] = None,
                 project_name: str = "Python Project") -> None:
        

        self.root_dir = root_dir
        self.language: int = config.language_type[language];
        self.ignor_file = ignore_file
        self.project_name = project_name


        self.all_files = []
    
    def get_files_from_directory(self, current_path: str = "")  -> None:
        
        files = os.listdir(self.root_dir + current_path)
        for element in files:
            file_path = self.root_dir + current_path + element
            if self.is_ignored(file_path) == False:
                if  os.path.isfile(file_path):
                    self.all_files.append(file_path)
                else:
                    self.get_files_from_directory(current_path=current_path + element + "/")
    
    def is_ignored(self, path:str) -> bool:
        if self.ignor_file:
            for i_element in self.ignor_file:
                if self.root_dir + i_element == path:
                    return True
                
        return False
    
    @utilities.time_manager        
    def get_code_from_file(self) -> None:
        self.codes: dict[str, str] = {}
        for element in self.all_files:
            with open(element, 'r', encoding="utf-8") as file:
                try:
                    code = file.read()
                    self.codes[element] = code
                except:
                    pass
    
    @utilities.time_manager
    def make_prompt(self) -> str:
        start_prompt: str = config.language_prompt[self.language][0]
        name_prompt: str = f'{ config.language_prompt[self.language][1]}: {self.project_name}'

        files_prompt: str = "    "

        for element in list(self.codes.keys()):
            file_prompt: str = f'{element}: {self.codes[element]}'
            files_prompt += file_prompt + "   "

        exit_prompt: str = start_prompt +  name_prompt  + files_prompt

        return exit_prompt

class GptHandler:
    def __init__(self, provider: str = "DarkAI") -> None:
        self.provider = getattr(g4f.Provider, provider, None)

    @utilities.time_manager
    def get_answer(self, prompt: str) -> str:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            provider=self.provider
        )

        return response
 
class AnswerHandler:
    def __init__(self, answer: str) -> None:
        self.answer = [
           answer
        ]
    @utilities.time_manager
    def save_documentation(self, name: str = "README.md") -> None:
        try:
            with open(name, "w", encoding="utf-8") as file:
                    file.write("")
        except:
            pass


        for el in self.answer:
            with open(name, "a", encoding="utf-8") as file:
                file.write(el)
                file.write("\n")
    
    def combine_response(self, new_response: str) -> None:
        self.answer.append(new_response)
    


    
    @classmethod
    def make_start_req_form(cls, prompt: str) -> list:
        return [{"role": "user", "content": prompt}]
    
class AutoDock:
    def __init__(self, 
                 root_dir: str, 
                 language: str = "en", 
                 ignore_file: list[str] = None,
                 project_name: str = "Python Project") -> None:
        

        self.language: int = config.language_type[language]
        self.language_name: str = language

        req_hendler = ReqHendler(root_dir=root_dir, ignore_file=ignore_file, language=language, project_name=project_name)
        req_hendler.get_files_from_directory()
        req_hendler.get_code_from_file()

        self.prompt = req_hendler.make_prompt()
        self.req_hendler = req_hendler

        self.GPT = GptHandler(provider="DarkAI")
        
    @utilities.time_manager
    def get_response(self, codes: dict) -> AnswerHandler:
        answer_handler: AnswerHandler;
        answer_handler = self.get_part_of_response(prompt=self.prompt)
        for key in list(codes.keys()):
            
            prompt = f"""{config.language_prompt[self.language][2]} name of file is {key} content of this file is {codes[key]}"""
            answer_handler = self.get_part_of_response(prompt=prompt, answer_handler=answer_handler)
            time.sleep(5)


        return answer_handler



    @utilities.time_manager
    def get_part_of_response(self, prompt: str, answer_handler: AnswerHandler = None) -> AnswerHandler:
        try:
            if answer_handler:
                response = self.GPT.get_answer(prompt=prompt)
                answer_handler.combine_response(response)
                
                return answer_handler

            else:
                message = prompt
                response = self.GPT.get_answer(prompt=message)
                return AnswerHandler(response)
        except:
            time.sleep(30)
            return self.get_part_of_response(prompt=prompt, answer_handler=answer_handler)
            


    @utilities.time_manager
    def save_dock(self, answer_handler: AnswerHandler, name: str = "Readme_files/README") -> None:
        new_name = f"{name}.{self.language_name}.md"
        answer_handler.save_documentation(name=new_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--name_project", type=str, help="name of project", required=True)
    parser.add_argument("--root_dir", type=str, help="root dir", required=True)
    parser.add_argument("--ignore", type=str, help="ignor files", required=True)
    parser.add_argument("--languages", type=str, help="language", required=True)
    
    
    args = parser.parse_args()
    project_name = args.name_project
    root_dir = args.root_dir
    languages = ast.literal_eval(args.languages)
    ignore_file = ast.literal_eval(args.ignore)

    for language in languages:
        utilities.start(3)
        auto_dock = AutoDock(root_dir=root_dir, ignore_file=ignore_file, project_name=project_name, language=language)
        codes = auto_dock.req_hendler.codes
        utilities.start(len(list(codes.keys())))

        answer_handler = auto_dock.get_response(codes=codes)
        auto_dock.save_dock(answer_handler=answer_handler)

        print(" ")
        print(language)