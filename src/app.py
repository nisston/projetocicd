import os
from datetime import datetime

def gerar_mensagem(nome):
    if not nome:
        raise ValueError("O nome não pode ser vazio!")
    return f"Olá, {nome}! Este site foi construído e publicado automaticamente via CI/CD."

def main():
    mensagem = gerar_mensagem("Turma de Computação")
    data_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pipeline CI/CD em Python</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f6f8; text-align: center; padding: 50px; }}
        .card {{ background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }}
        h1 {{ color: #2ea44f; }}
        p {{ color: #555; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Deploy com Sucesso!</h1>
        <p>{mensagem}</p>
        <p><small>Última atualização: {data_atual}</small></p>
    </div>
</body>
</html>
"""
    # Cria o diretório de publicação (site estático)
    os.makedirs("public", exist_ok=True)
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Site HTML gerado com sucesso na pasta public/!")

if __name__ == "__main__":
    main()