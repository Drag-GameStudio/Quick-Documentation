from g4f.client import Client
from g4f.Provider import ChatGLM, DDG, GizAI, Liaobots, PollinationsAI, Qwen_QVQ_72B, Yqcloud #DDG, PollinationsAI
import g4f
import time
import asyncio


class GPT:
    def __init__(self, provider=PollinationsAI, gpt_model: str = "gpt-4o"):
        self.client = Client(
            provider=provider,
        )
        self.gpt_model = gpt_model

    def get_answer(self, prompt):

        try:
            response = self.client.chat.completions.create(
                model=self.gpt_model,
                messages=prompt,
            )
        except Exception as e:
            print(e)

            time.sleep(5)
            return self.get_answer(prompt)
    
        answer = response.choices[0].message.content

        return answer

    def get_answer_without_history(self, prompt):

        try:
            response = self.client.chat.completions.create(
                model=self.gpt_model,
                messages=[{"role": "user", "content": prompt}]
            )
        except:
            return None
    
        answer = response.choices[0].message.content

        return answer