# Você precisa criar cinco novas listas 
# a partir de uma lista original de números inteiros. 
# As novas listas devem ser as seguintes:
# 1 - Uma lista contendo apenas os números pares da lista original.
# 2 - Uma lista contendo apenas os números ímpares da lista original.
# 3 - Uma lista contendo apenas os múltiplos de 3 da lista original.
# 4 - Uma lista contendo apenas os múltiplos de 3 e 4 da lista original.
# 5 - Uma lista contendo apenas os múltiplos de 3 ou 4 da lista original.
# Resolva o problema utilizando a estrutura de repetição while.

numeros = [11, 12, 3, 41, 15, 6, 17, 8, 91, 10]

pares = []
impares = []
multiplos_de_3 = []
multiplos_de_3_e_4 = []
multiplos_de_3_ou_4 = []

contador = 0
while contador < len(numeros):
    if numeros[contador] % 2 == 0:
        pares.append(numeros[contador])
    else:
        impares.append(numeros[contador])
    
    if numeros[contador] % 3 == 0:
        multiplos_de_3.append(numeros[contador])

    if numeros[contador] % 3 == 0 and numeros[contador] % 4 == 0:
        multiplos_de_3_e_4.append(numeros[contador])

    if numeros[contador] % 3 == 0 or numeros[contador] % 4 == 0:
        multiplos_de_3_ou_4.append(numeros[contador])
    
    contador += 1

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"números múltiplos de 3: {multiplos_de_3}")
print(f"números múltiplos de 3 e 4: {multiplos_de_3_e_4}")
print(f"números múltiplos de 3 ou 4: {multiplos_de_3_ou_4}")
