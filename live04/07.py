class Carro:
    def __init__ (self, modelo, marca, ano, cor, preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.preco = preco

    def __str__(self):
        return f"{self.modelo} | {self.marca} | {self.cor}"
    
    def acelerar(self):
        print(f"{self.modelo} acelerando...")

    def frear(self):
         print(f"{self.modelo} freando...")

    def informar(self):
        print(f"{self.modelo} | {self.marca} | {self.cor}")


carro1 = Carro("Fiesta", "FIAT", 2000, "Azul", 50000.00 )
carro2 = Carro("Civic", "Honda", 2020, "Preto", 100000.00)

carro1.frear()
carro2.acelerar()
carro1.informar()
print(carro2)
