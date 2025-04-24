from .gpt import gpt, prompt_handler
from .reader import read_folder
from py_progress.progress import ProgressBar
import argparse
import asyncio

class DocWriter:
    def __init__(self, root_dir, ignore_files: list = [], language="en"):
        self.root_dir = root_dir
        self.ignore_files = ignore_files
        self.language = language

    def read_folder(self):
        folder_reader = read_folder.Reader(self.root_dir, self.ignore_files)
        self.read_data: read_folder.FilesReader = folder_reader.read_folder()
        self.prompt_generator = prompt_handler.PromptGenerator(self.read_data.get_all_prompt(), language=self.language)

        return self.read_data.get_all_prompt()
    
    def write_main_doc(self):
        main_prompt = self.prompt_generator.get_main_prompt()
        gpt_response = gpt.GPT().get_answer([{"role": "user", "content": main_prompt}])
        return gpt_response
    
    async def write_main_doc_async(self, prompts):
        tasks = [gpt.GPT().get_answer(prompt) for prompt in prompts]
        result = await asyncio.gather(*tasks)

        return result


    def write_deep_doc(self):
        deep_prompts = self.prompt_generator.get_prompts_for_files()

        full_response = ""
        pb = ProgressBar(len(deep_prompts))
        
        for deep_prompt in deep_prompts:

            gpt_response = gpt.GPT().get_answer([{"role": "user", "content": deep_prompt}])
            full_response += gpt_response + "\n\n"
            pb.progress(f"Writing documentation...")

        return full_response
    

    def write_doc(self):
        main_doc = self.write_main_doc()
        deep_doc = self.write_deep_doc()

        full_doc = f"{main_doc}\n\n{deep_doc}"

        return full_doc
    
    def save_doc(self, doc: str, file_name: str):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(doc)


def write_doc():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_dir", help="Path to the root directory")
    parser.add_argument("--ignore", help="Ignore files")
    parser.add_argument("--lang", help="Language for documentation", default="en")

    args = parser.parse_args()
    root_dir = args.root_dir
    if args.ignore is not None:
        ignore_files = args.ignore.split(",")
    else:
        ignore_files = []

    print(ignore_files)

    lang = args.lang
    doc_writer = DocWriter(root_dir, ignore_files, lang)
    doc_writer.read_folder()
    full_doc = doc_writer.write_doc()
    doc_writer.save_doc(full_doc, f"{root_dir}/documentation.md")


if __name__ == "__main__":
    write_doc()
    # dw = DocWriter(r"C:\Users\huina\Python Projects\Impotant projects\Libs\Quick Documentation\quick_doc_py", ["*__init__.py", "*__pycache__",])
    # dw.read_folder()
    # full_doc = dw.write_doc()
    # dw.save_doc(full_doc, "full_doc.md")
