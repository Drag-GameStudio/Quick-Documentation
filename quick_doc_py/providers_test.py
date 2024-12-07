import g4f
import time 
import threading
import time
from colorama import Fore, Back, Style, init
import argparse
import math



def timeout_control(timeout):
    def func_control(func):
        def wrapper(*args, **kwargs):
            result_event = threading.Event()
            result = None
            
            def target():
                nonlocal result
                result = func(*args, **kwargs)
                result_event.set()

            proc = threading.Thread(target=target)
            proc.daemon = True
            proc.start()

            result_event.wait(timeout)

            if proc.is_alive():
                return None
            else:
                return result

        return wrapper
    return func_control

class TextStyle:
    def __init__(self) -> None:
        init()

    def get_text(self, text: str, color: any = "", back: any = "") -> str:
        return color + back + str(text) + Style.RESET_ALL

class ProgressBar():
    def __init__(self, part) -> None:
        self.procent = 0
        self.all = part
        self.old = ""
        self.len = 60
    
    def progress(self, name):
        ts = TextStyle()
        print(f"\r {' ' * (self.len + len(self.old) + 10)}", end="")
        self.procent += 1
        procent = math.ceil((self.procent / self.all)  * 100)
        proc = math.ceil(self.len / 100 *  procent)
        bar = ts.get_text(text=" ", back=Back.WHITE) * proc + " " * (self.len - proc)
        procent = ts.get_text(text=str(procent) + "%", color=Fore.GREEN)
        print(f"\r {procent} |{bar}|: {ts.get_text(name, color=Fore.CYAN)}", end="")

        self.old = name

class ProviderTest:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def get_providers(self):
        self.providers = [p for p in dir(g4f.Provider) if not p.startswith("__")]
        self.progress = ProgressBar(part=len(self.providers))

    def test_provioder(self, provider_name: str) -> tuple[bool, str]:
        try:
            provider = getattr(g4f.Provider, provider_name, None)
            responce = self.test_provider_timeout(provider=provider)

            return responce != None, responce
            
            
        except Exception as e:
            return False, None

    @timeout_control(timeout=30)
    def test_provider_timeout(self, provider):
        try:
            response = g4f.ChatCompletion.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": "Hello"}
                ],
                provider=provider
            )
            
            return response
        except Exception as e:
            return None

    def test_providers(self):
        work_providers = {}
        for el in self.providers:
            self.progress.progress(name=el)
            is_work, responce = self.test_provioder(el)
            if is_work:
                work_providers[el] = responce

        print(work_providers)
        return work_providers


def provider_test(model_name: str) -> dict:
    PT = ProviderTest(model_name=model_name)
    PT.get_providers()
    providers = PT.test_providers()
    return providers

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--name_model", type=str, help="name of model", required=True)
    args = parser.parse_args()

    model_name = args.name_model

    providers = provider_test(model_name=model_name)
    print(providers)



if __name__ == "__main__":
    #gpt-4, gpt-3.5-turbo
    main()