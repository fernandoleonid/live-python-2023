# - Você é um programador que trabalha em uma loja virtual 
# que vende produtos eletrônicos. A sua tarefa é criar 
# um programa em Python que calcule o preço final 
# de um produto após o acréscimo de impostos e descontos, 
# e exibir na tela o valor final que será cobrado do cliente.

# 1 - Ler dados
preco = float(input('Digite o valor do produto:'))
imposto = float(input('Digite o valor do imposto:'))
desconto = float(input('Digite o valor do desconto:'))

# 2 - Calcular os valores
valor_imposto = imposto / 100 * preco
valor_desconto = desconto / 100 * preco
preco_final = preco + valor_imposto - valor_desconto

# 3 - Exibir os resultados

print (f"O preço final do produto é R$ {preco_final:.3f}")
