import g4f
import g4f.Provider
import os
import sys
import argparse
import ast
import time

try:
    from . import config
    from . import utilities
    from .log_logic import req
except:
    import config
    import utilities
    from log_logic import req


sys.stdout.reconfigure(encoding='utf-8')


class ReqHendler:
    def __init__(self, 
                 root_dir: str, 
                 language: str = "en", 
                 ignore_file: list[str] = None,
                 project_name: str = "Python Project") -> None:
        

        self.root_dir = root_dir
        self.language: int = config.LANGUAGE_TYPE[language];
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
                if i_element[0] == "*":
                    path_datiles = path.split("/")
                    if path_datiles[len(path_datiles) - 1] == i_element[1:]:
                        return True
                else:
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
    def __init__(self, provider: str, model: str) -> None:
        self.provider = getattr(g4f.Provider, provider, None)
        self.model = model


    @utilities.time_manager
    def get_answer(self, prompt: str) -> str:
        response = g4f.ChatCompletion.create(
            model=self.model,
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
        with open(name, "w") as file:
            file.write(self.get_full_answer())
    

    def combine_response(self, new_response: str) -> None:
        self.answer.append(new_response)

    def get_full_answer(self) -> str:
        ex: str = """## Thanks for using [quick-doc-py](https://pypi.org/project/quick-doc-py). If you like this project, you can support it on [ko-fi](https://ko-fi.com/draggamestudio). Your support helps improve the project and add new features. Thank you!\n"""
        for el in self.answer:
            ex += el
            ex += "\n"
        ex += """### Created by [quick-doc-py](https://pypi.org/project/quick-doc-py)"""
        return ex
    


    
    @classmethod
    def make_start_req_form(cls, prompt: str) -> list:
        return [{"role": "user", "content": prompt}]
    
class AutoDock:
    def __init__(self, 
                 root_dir: str, 
                 language: str = "en", 
                 ignore_file: list[str] = None,
                 project_name: str = "Python Project",
                 provider: str = "Mhystical",
                 gpt_model: str = "gpt-4",
                 general_prompt: str = "",
                 default_prompt: str = "") -> None:
        
        self.req2server = req.ReqToServer()
        self.session_code = self.req2server.create_session()
        

        self.language: int = config.LANGUAGE_TYPE[language]
        self.language_name: str = language

        self.general_prompt = general_prompt
        self.default_prompt = default_prompt

        self.root_dir = os.path.normpath(root_dir).replace("\\", "/")
        if self.root_dir[len(self.root_dir) - 1] != "/":
            self.root_dir += "/"


        req_hendler = ReqHendler(root_dir=self.root_dir, ignore_file=ignore_file, language=language, project_name=project_name)
        req_hendler.get_files_from_directory()
        req_hendler.get_code_from_file()

        self.prompt = req_hendler.make_prompt()
        self.req_hendler = req_hendler

        reqData = {
            "project_name": project_name,
            "language": language,
            "gpt_model": gpt_model
        }
        self.req2server.add_to_session(session_code=self.session_code, data=reqData)

        self.GPT = GptHandler(provider=provider, model=gpt_model)
        
        
    @utilities.time_manager
    def get_response(self, codes: dict) -> AnswerHandler:
        answer_handler: AnswerHandler
        answer_handler = self.get_part_of_response(prompt=f'{self.prompt} Additional wishes: {self.general_prompt}')
        self.answer_handler = answer_handler
        for key in list(codes.keys()):
            
            prompt = f"""{config.language_prompt[self.language][2]} Additional wishes: {self.default_prompt}. name of file is {key} content of this file is {codes[key]}"""
            answer_handler = self.get_part_of_response(prompt=prompt, answer_handler=answer_handler)
            time.sleep(20)


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
            print("st again")
            time.sleep(120)
            print("end again")
            return self.get_part_of_response(prompt=prompt, answer_handler=answer_handler)
            


    @utilities.time_manager
    def save_dock(self, answer_handler: AnswerHandler, name: str = "README") -> None:
        new_name = f"{self.root_dir}{name}.{self.language_name}.md"
        
        answer_handler.save_documentation(name=new_name)

    def get_doc(self):
        self.answer_handler.answer
        pass


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--name_project", type=str, help="name of project", required=True)
    parser.add_argument("--root_dir", type=str, help="root dir", required=True)
    parser.add_argument("--ignore", type=str, help="ignor files", required=True)
    parser.add_argument("--languages", type=str, help="language", required=True)

    parser.add_argument("--gpt_version", type=str, help="gpt version", required=False)
    parser.add_argument("--provider", type=str, help="provider", required=False)

    parser.add_argument("--general_prompt", type=str, help="general prompt", required=False)
    parser.add_argument("--default_prompt", type=str, help="default prompt", required=False)

    parser.add_argument("--with_git", type=bool, help="Is git used", required=False)

    args = parser.parse_args()

    docs = worker(args)
    for doc in docs:
        doc.save_dock(answer_handler=doc.answer_handler)

def worker(args) -> list[AutoDock]:
    project_name = args.name_project
    root_dir = args.root_dir
    languages = ast.literal_eval(args.languages)
    ignore_file: list = ast.literal_eval(args.ignore)

    for ignored in config.DEFAULT_IGNORED_FILES:
        ignore_file.append(ignored)
    
    if args.with_git != None:
        if args.with_git:
            for ignored in config.GIT_IGNORED_FILES:
                ignore_file.append(ignored)

    gpt_version = "gpt-3.5-turbo"
    provider = "GizAI"

    default_prompt = ""
    general_prompt = ""

    if args.gpt_version != None:
        gpt_version = args.gpt_version

    if args.provider != None:
        provider= args.provider

    if args.general_prompt != None:
        general_prompt = args.general_prompt

    if args.default_prompt != None:
        default_prompt = args.default_prompt

        
    all_doc = []
    for language in languages:
        utilities.start(3)
        
        auto_dock = AutoDock(root_dir=root_dir, 
                             ignore_file=ignore_file, 
                             project_name=project_name, 
                             language=language, 
                             gpt_model=gpt_version, 
                             provider=provider)
        
        codes = auto_dock.req_hendler.codes

        utilities.start(len(list(codes.keys())))

        answer_handler = auto_dock.get_response(codes=codes)

        all_answer = answer_handler.get_full_answer()
        reqData = {
            "documentation": all_answer
        }
        auto_dock.req2server.add_to_session(auto_dock.session_code, reqData)

        
        all_doc.append(auto_dock)
        

    return all_doc

def get_gpt_models() -> list[str]:
    return config.GPT_MODELS

if __name__ == "__main__":
    main()