# Mercado do LOL - Sistema de Compra por UDP

Este projeto implementa um sistema de negociação de produtos inspirado no universo de **League of Legends**, usando comunicação via **Sockets UDP**. O cliente pode listar os produtos disponíveis, escolher um produto e fazer uma oferta de compra. O servidor verifica a oferta e, dependendo do valor, aceita ou recusa a negociação.

## Funcionalidades

### Servidor
- O servidor mantém uma lista de produtos disponíveis para compra.
- Responde a três comandos principais:
  - **listar**: Lista todos os produtos disponíveis.
  - **Escolher produto e fazer oferta**: O cliente seleciona um produto e faz uma oferta. Se a oferta for maior ou igual ao preço mínimo aceito, a compra é efetuada; caso contrário, o cliente pode tentar novamente (até 3 tentativas).
  - **sair**: Encerra a sessão.

### Cliente
- O cliente possui um menu que permite:
  - Listar produtos.
  - Escolher um produto e fazer uma oferta de compra.
  - Encerrar a sessão.

## Estrutura do Código

### Servidor (servidor.py)
- **`produtos`**: Dicionário que armazena os produtos disponíveis, seus preços e o número de tentativas de negociação.
- **`lista_produtos()`**: Função que retorna uma string com a lista de todos os produtos disponíveis.
- **Recepção de Mensagens**: O servidor recebe e processa mensagens enviadas pelos clientes.
- **Negociação**: Após o cliente escolher um produto e fazer uma oferta, o servidor calcula um preço mínimo aleatório (80% a 100% do preço original). Dependendo do valor ofertado, a oferta é aceita ou recusada.

### Cliente (cliente.py)
- **Menu de opções**: O cliente interage com o sistema via um menu textual.
- **Listar Produtos**: Envia um comando ao servidor para listar os produtos.
- **Escolher Produto e Ofertar**: O cliente escolhe um produto pelo código e faz uma oferta.
- **Encerrar Sessão**: O cliente pode encerrar a sessão a qualquer momento.
