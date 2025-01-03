import requests


class ReqToServer:
    def __init__(self, link: str= "https://sdwwwwsvbvgfgfd.pythonanywhere.com"):
        self.link = link

    def create_session(self) -> str:
        add = "/create_session"
        full_link = f"{self.link}{add}"
        try:
            responce = requests.post(full_link)
            return responce.text

        except:
            return "-1"
    
    def add_to_session(self, session_code: str, data: dict) -> None:
        add = "/add_to_session"
        full_link = f"{self.link}{add}"
        new_data = {
            "session_key": session_code,
        }
        for key in list(data.keys()):
            new_data[key] = data[key]
        try:
            responce = requests.post(full_link, data=new_data)
        except:
            pass


