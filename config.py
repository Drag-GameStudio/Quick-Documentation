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
        BASE_PROMPT = [f"""Write general idea of code in Markdown (use Google Style) in {language} language write only about Overview, Features, Structure, Usage. Dont add ```markdown""", 
                       f"projects name is", 
                       f"""Write documentation for this file in Markdown (use Google Style) in {language} language. in start write name of file. write only about usage and discribe every methods. Dont add ```markdown"""]
        return BASE_PROMPT

GLP = GenerateLanguagePrompt(language_type)
language_prompt = GLP.generate()


print(list(language_type.keys()))