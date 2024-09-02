# -- coding: utf-8 --
from socket import *
import random

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('O servidor está pronto esperando mensagens')

produtos = {
    1: {"nome": "Espada do Rei Destruído", "preco": 3200.0, "tentativas": 3},
    2: {"nome": "Gume do Infinito", "preco": 3400.0, "tentativas": 3},
    3: {"nome": "Cutelo Negro", "preco": 3100.0, "tentativas": 3},
    4: {"nome": "Cajado do Vazio", "preco": 2800.0, "tentativas": 3},
    5: {"nome": "Ampulheta de Zhonya", "preco": 2600.0, "tentativas": 3},
    6: {"nome": "Capuz da Morte de Rabadon", "preco": 3100.0, "tentativas": 3},
    7: {"nome": "Placa Gargolítica", "preco": 3200.0, "tentativas": 3},
    8: {"nome": "Coração Congelado", "preco": 2700.0, "tentativas": 3},
    9: {"nome": "Semblante Espiritual", "preco": 2900.0, "tentativas": 3},
    10: {"nome": "Redenção", "preco": 2300.0, "tentativas": 3},
    11: {"nome": "Medalhão dos Solari de Ferro", "preco": 2500.0, "tentativas": 3},
    12: {"nome": "Turíbulo Ardente", "preco": 2300.0, "tentativas": 3},
    13: {"nome": "Draktharr", "preco": 2700.0, "tentativas": 3},
    14: {"nome": "Youmuu's", "preco": 2700.0, "tentativas": 3},
}

def lista_produtos():
    lista = "Produtos disponíveis: \n"
    for codigo, produto in produtos.items():
        lista += f"Código: {codigo}, Nome: {produto['nome']}, Preço: {produto['preco']} \n"
    return lista

while True:

    message, clientAddress = serverSocket.recvfrom(2048)
    mensagem_decodificada = message.decode('utf-8').strip()

    if mensagem_decodificada.lower() == "listar":
        serverSocket.sendto(lista_produtos().encode('utf-8'), clientAddress)
    elif mensagem_decodificada.lower() == "listarcompras":
        serverSocket.sendto(lista_produtos().encode('utf-8'), clientAddress)
    elif mensagem_decodificada.lower() == "sair":
        serverSocket.sendto("Sessão encerrada. Obrigado por usar o nosso sistema.".encode('utf-8'), clientAddress)
    else:
        try:
            codigo_produto = int(mensagem_decodificada)
            if codigo_produto in produtos:
                produto = produtos[codigo_produto]
                serverSocket.sendto(
                    f"Você escolheu {produto['nome']} que custa {produto['preco']}R$. Faça sua oferta.".encode('utf-8'),
                    clientAddress)
                oferta_cliente, _ = serverSocket.recvfrom(2048)
                oferta_cliente = float(oferta_cliente.decode('utf-8'))
                minimo_aceito = produto['preco'] * (random.uniform(1.0, 0.8))
                if oferta_cliente >= minimo_aceito:
                    resposta = f"Oferta aceita! Você comprou {produto['nome']} por {oferta_cliente}."
                    produtos.pop(codigo_produto)
                else:
                    produto['tentativas'] -= 1
                    if produto['tentativas'] > 0:
                        resposta = f"Oferta recusada. Você ainda tem {produto['tentativas']} tentativas."
                    else:
                        resposta = f"Negociação cancelada para {produto['nome']} após 3 tentativas."
                        produtos.pop(codigo_produto)
                serverSocket.sendto(resposta.encode('utf-8'), clientAddress)
            else:
                serverSocket.sendto("Código de produto inválido. Tente novamente.".encode('utf-8'), clientAddress)
        except ValueError:
            serverSocket.sendto("Entrada inválida. Por favor, envie um número válido.".encode('utf-8'), clientAddress)