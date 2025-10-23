import random
from datetime import datetime

nomes = ['Rodenilson', 'Valdisney', 'Aristinelson', 'Iomerson', 'Divonaldo']
sobrenomes = ['da Silva Júnior', 'Nogueiraldo', 'Fontenilson', 'Almeirindo', 'Sousalvo']

def gerar_nome_completo():
    return random.choice(nomes) + " " + random.choice(sobrenomes)

def registrar_log(mensagem):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("nomes.log", "a", encoding="utf-8") as f:
        f.write("[" + data_hora + "] " + mensagem + "\n")

def ler_logs():
    try:
        with open("nomes.log", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

print("Inicio:", datetime.now())

while True:
    print("\nMENU:")
    print("S - Sair")
    print("N - Registrar um nome")
    print("M - Mostrar nomes")
    opcao = input("Escolha: ").upper().strip()

    if opcao == "S":
        break
    elif opcao == "N":
        nome = gerar_nome_completo()
        print("Nome gerado:", nome)
        registrar_log("Nome registrado: " + nome)
    elif opcao == "M":
        logs = ler_logs()
        if logs:
            for i, linha in enumerate(logs):
                print(i, "-", linha.strip())
        else:
            print("Nenhum registro encontrado.")
    else:
        print("Opção inválida.")

print("Fim:", datetime.now())

"aaa"