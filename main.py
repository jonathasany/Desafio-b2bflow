import os
import requests
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

zapi_url = os.getenv("ZAPI_URL")
zapi_token = "3CD636A4BF7E2B1E24EBEC4B"  # seu token

response = supabase.table("contatos").select("*").execute()
contatos = response.data

headers = {
    "Content-Type": "application/json",
    "Client-Token": zapi_token
}

for contato in contatos[:3]:
    telefone = contato["telefone"]
    nome = contato["nome_contato"]
    mensagem = f"Olá {nome}, tudo bem com você?"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        res = requests.post(zapi_url, json=payload, headers=headers)
        if res.status_code == 200:
            print(f"Mensagem enviada para {nome} ({telefone})")
        else:
            print(f"Erro ao enviar para {nome}: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"Erro ao enviar para {nome}: {e}")
