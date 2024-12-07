LANGUAGE_TYPE = {
    "en": 0, 
    "ru": 1,
    "ua": 2,
    "chs": 3, #китайский 
    "es": 4, #испанский
    "pl": 5 #польский
}

DEFAULT_IGNORED_FILES = ["*README.md", "*__pycache__", "*dist"]
GIT_IGNORED_FILES = ["*.github", "*.git", "*.venv", "*.gitignore"]

GPT_MODELS = ["gpt-4", "gpt-3.5-turbo"]

class GenerateLanguagePrompt:
    def __init__(self, languages: dict[str, int]) -> None:
        self.languages = list(languages.keys())

    def generate(self) -> dict:
        language_prompt = {}
        for language_index in range(len(self.languages)):
            language_prompt[language_index] = self.gen_prompt(language=self.languages[language_index])

        return language_prompt
    
    def gen_prompt(self, language: str) -> list[str]:
        BASE_PROMPT = [f"""Write general idea of code in Markdown (use Google Style) in {language} language write only about Overview, 
                        Features, Structure, Usage. Dont add ```markdown""", 

                       f"projects name is", 

                       f"""Write documentation for this file in Markdown (use Google Style) in {language} language. 
                       Write only about usage and discribe every methods. 
                       Remember that it is not full documantation it is just addition. Dont add ```markdown"""]
        return BASE_PROMPT

GLP = GenerateLanguagePrompt(LANGUAGE_TYPE)
language_prompt = GLP.generate()

print(list(LANGUAGE_TYPE.keys()))