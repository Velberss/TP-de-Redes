# -*- coding: utf-8 -*-
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

try:
    while True:
        print("\n====== Bem vindo Ao Mercado do LOL ======")
        print("=========================================")
        print("\nMenu:")
        print("1. Listar produtos")
        print("2. Escolher um produto e fazer uma oferta")
        print("3. Sair")
        print("=========================================")
        opcao = input("\nDigite uma opção: ").strip()

        if opcao == "1":
            clientSocket.sendto("listar".encode('utf-8'), (serverName, serverPort))
            modifiedMessage, _ = clientSocket.recvfrom(2048)
            print(modifiedMessage.decode('utf-8'))
        elif opcao == "2":
            codigo_produto = input("Digite o código do produto que deseja comprar: ").strip()
            clientSocket.sendto(codigo_produto.encode('utf-8'), (serverName, serverPort))
            modifiedMessage, _ = clientSocket.recvfrom(2048)
            resposta = modifiedMessage.decode('utf-8')
            print(resposta)
            if "escolheu" in resposta.lower():
                oferta = input("Digite o valor da sua oferta: ").strip()
                clientSocket.sendto(oferta.encode('utf-8'), (serverName, serverPort))
                modifiedMessage, _ = clientSocket.recvfrom(2048)
                print(modifiedMessage.decode('utf-8'))
        elif opcao == "3":
            clientSocket.sendto("sair".encode('utf-8'), (serverName, serverPort))
            modifiedMessage, _ = clientSocket.recvfrom(2048)
            print(modifiedMessage.decode('utf-8'))
            break
        else:
            print("Opção inválida. Tente novamente.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    clientSocket.close()
