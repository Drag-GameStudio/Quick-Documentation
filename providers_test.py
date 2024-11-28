import g4f
import time 
providers = [p for p in dir(g4f.Provider) if not p.startswith("__")]
print("Доступные провайдеры:", providers)
for el in providers[3:]:

    try:
        
        provider = getattr(g4f.Provider, el, None)
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": "Hello"}
            ],
            provider=provider
        )
        print(response)
        print(el)

    except:
        print(f'{el} is not passed')


