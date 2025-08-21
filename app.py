import requests
import json


# URL do endpoint
url = "http://localhost:11434/api/generate"

# Dados que serão enviados na solicitação
data = {
    "model": "phi3",
    "prompt": "qual e a capital de angola"
}

# Enviando a solicitação POST
response = requests.post(url, json=data, stream=True)

# Variável para armazenar a resposta final
complete_response = ""

# Processando a resposta linha por linha
for line in response.iter_lines():
    if line:
        try:
            # Decodifica e imprime cada linha JSON
            decoded_line = json.loads(line.decode('utf-8'))
            print(decoded_line['response'])
            # Adiciona o conteúdo ao resultado final, se necessário
            if 'response' in decoded_line:
                complete_response += decoded_line['response']
            if decoded_line.get('done', False):
                break
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON:", line)

print("Resposta Completa:", complete_response)
