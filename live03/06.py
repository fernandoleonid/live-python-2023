# Exercício: Estoque
# Você precise criar um programa para gerenciar 
# o estoque de produtos em uma loja. 
# Cada produto tem um nome, preço e quantidade em estoque. 
# O programa deve permitir ao usuário adicionar novos produtos, 
# atualizar informações de produtos existentes 
# e visualizar o estoque atual.
def obter_preco():
    while True:
        preco = input("Preço do produto: ")
        try:
            return float(preco)
        except ValueError:
            print("Preço inválido! Digite novamente")

def obter_quantidade():
    while True:
        quantidade = input("Quantidade em estoque: ")
        try:
            return int(quantidade)
        except ValueError:
            print("Quantidade inválido! Digite novamente")


def adicionar_produto(estoque):
    nome = input("Nome do produto: ")
    preco = obter_preco()
    quantidade = obter_quantidade()
    estoque[nome] = {"preco": preco,"quantidade": quantidade }
    return estoque

def atualizar_produto(estoque):
    nome = input("Nome do produto para atualizar: ")
    if nome in estoque:
        preco = obter_preco()
        quantidade = obter_quantidade()
        estoque[nome]["preco"] = preco
        estoque[nome]["quantidade"] = quantidade
    else:
        print("Produto não encontrado no estoque!")
    return estoque

def visualizar_estoque(estoque):
    for nome, info in estoque.items():
        preco = info["preco"]
        quantidade = info["quantidade"]
        print (f" => {nome}: R$ {preco:.2f} - {quantidade} unidades")

def sair():
    print(" => Saindo do sistema de estoque...")


estoque = {}

while True:
    print("Selecione uma opção:")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Visualizar estoque")
    print("4 - Sair")

    opcao = input("Opção selecionada: ")

    if opcao == "1":
        estoque = adicionar_produto(estoque)

    elif opcao == "2":
        estoque = atualizar_produto(estoque)
        
    elif opcao == "3":
        visualizar_estoque(estoque)

    elif opcao == "4":
        sair()
        break
    else:
        print("Opção inválida!")