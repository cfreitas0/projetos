import requests

try:
    requisicao = requests.get("https://web.whatsapp.com/")
    print(requisicao.text)
except Exception as e:
    print("Erro na ReQ...", e)