# Desafio b2bflow - Estágio Python

Script em Python que lê contatos cadastrados no [Supabase](https://supabase.com/) e envia mensagens personalizadas via [Z-API](https://z-api.io/).

## 🗄️ Configuração do Supabase
1. Crie um projeto no Supabase.
2. Crie uma tabela `contatos` com as colunas abaixo:

| Nome       | Tipo       | Primário | Padrão | Descrição                              |
|------------|------------|----------|--------|----------------------------------------|
| id         | int8       | ✅       | auto   | Identificador único                    |
| nome       | text       | ❌       | —      | Nome do contato                        |
| telefone   | text       | ❌       | —      | Número no formato DDI + DDD + número   |
| created_at | timestamp  | ❌       | now()  | Data e hora de criação                 |

3. Ative o **RLS (Row Level Security)**.
4. Crie uma política permitindo leitura de dados com a **chave de serviço**.

---

## 🔑 Variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
SUPABASE_URL=https://SUA-URL.supabase.co
SUPABASE_KEY=SUA-CHAVE-API
ZAPI_URL=https://api.z-api.io/instances/SUA-INSTANCE/token/SUA-TOKEN/send-text


🚀 Como rodar

Clone este repositório:

git clone https://github.com/jonathasany/Desafio-b2bflow
cd Desafio-b2bflow


Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows


Instale as dependências:

pip install -r requirements.txt


Execute o script:

python main.py

📌 O que o script faz

Busca todos os contatos no Supabase.

Envia para cada um a mensagem personalizada:

Olá {{nome_contato}}, tudo bem com você?


Usa a API da Z-API para envio via WhatsApp.