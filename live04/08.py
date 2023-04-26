class Estoque:
    def __init__(self):
        self.estoque = {}
    
    def obter_preco(self):
        while True:
            preco = input("Preço do produto: ")
            try:
                return float(preco)
            except ValueError:
                print("Preço inválido! Digite novamente")

    def obter_quantidade(self):
        while True:
            quantidade = input("Quantidade em estoque: ")
            try:
                return int(quantidade)
            except ValueError:
                print("Quantidade inválido! Digite novamente")

    def adicionar_produto(self):
        nome = input("Nome do produto: ")
        preco = self.obter_preco()
        quantidade = self.obter_quantidade()
        self.estoque[nome] = {"preco": preco,"quantidade": quantidade }
    
    def atualizar_produto(self):
        nome = input("Nome do produto para atualizar: ")
        if nome in self.estoque:
            preco = self.obter_preco()
            quantidade = self.obter_quantidade()
            self.estoque[nome]["preco"] = preco
            self.estoque[nome]["quantidade"] = quantidade
        else:
            print("Produto não encontrado no estoque!")


    def visualizar_estoque(self):
        for nome, info in self.estoque.items():
            preco = info["preco"]
            quantidade = info["quantidade"]
            print (f" => {nome}: R$ {preco:.2f} - {quantidade} unidades")


estoque = Estoque()

while True:
    print("Selecione uma opção:")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Visualizar estoque")
    print("4 - Sair")

    opcao = input("Opção selecionada: ")

    if opcao == "1":
        estoque.adicionar_produto()

    elif opcao == "2":
        estoque.atualizar_produto()
        
    elif opcao == "3":
        estoque.visualizar_estoque()

    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")