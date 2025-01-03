import requests


class ReqToServer:
    def __init__(self, link: str= "https://sdwwwwsvbvgfgfd.pythonanywhere.com"):
        self.link = link

    def create_session(self) -> str:
        add = "/create_session"
        full_link = f"{self.link}{add}"

        responce = requests.post(full_link)
        return responce.text
    
    def add_to_session(self, session_code: str, data: dict) -> None:
        add = "/add_to_session"
        full_link = f"{self.link}{add}"
        new_data = {
            "session_key": session_code,
        }
        for key in list(data.keys()):
            new_data[key] = data[key]

        responce = requests.post(full_link, data=new_data)


