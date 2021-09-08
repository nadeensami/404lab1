import requests

print(requests.__version__)
requests.get("https://www.google.com/")

script = requests.get("https://raw.githubusercontent.com/nadeensami/404lab1/main/script.py")
print(script.text)
