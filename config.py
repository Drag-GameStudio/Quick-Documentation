language_type = {
    "en": 0, 
    "ru": 1,
    "ua": 2,
    "chs": 3, #китайский 
    "es": 4, #испанский
    "pl": 5 #польский
}

class GenerateLanguagePrompt:
    def __init__(self, languages: dict[str, int]) -> None:
        self.languages = list(languages.keys())

    def generate(self) -> dict:
        language_prompt = {}
        for language_index in range(len(self.languages)):
            language_prompt[language_index] = self.gen_prompt(language=self.languages[language_index])

        return language_prompt
    
    def gen_prompt(self, language: str) -> list[str]:
        BASE_PROMPT = [f"Write documentation in {language} language for this code in Markdown style (add style) describe the operating principle and examples of use what is this project for and describe the methods and classes. analyze the documentation yourself and add and add how use this project. Talk about all files(code)", f"projects name is", f"(Do not copy what has already been written, but continue from where you left off.)"]
        return BASE_PROMPT

GLP = GenerateLanguagePrompt(language_type)
language_prompt = GLP.generate()


print(list(language_type.keys()))