# Você precisa criar cinco novas listas 
# a partir de uma lista original de números inteiros. 
# As novas listas devem ser as seguintes:
# 1 - Uma lista contendo apenas os números pares da lista original.
# 2 - Uma lista contendo apenas os números ímpares da lista original.
# 3 - Uma lista contendo apenas os múltiplos de 3 da lista original.
# 4 - Uma lista contendo apenas os múltiplos de 3 e 4 da lista original.
# 5 - Uma lista contendo apenas os múltiplos de 3 ou 4 da lista original.
# Resolva o problema utilizando a estrutura de repetição FOR.

numeros = [1, 2, 31, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []
multiplos_de_3 = []
multiplos_de_3_e_4 = []
multiplos_de_3_ou_4 = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    if numero % 3 == 0:
        multiplos_de_3.append(numero)

    if numero % 3 == 0 and numero % 4 == 0:
        multiplos_de_3_e_4.append(numero)

    if numero % 3 == 0 or numero % 4 == 0:
        multiplos_de_3_ou_4.append(numero)


print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"números múltiplos de 3: {multiplos_de_3}")
print(f"números múltiplos de 3 e 4: {multiplos_de_3_e_4}")
print(f"números múltiplos de 3 ou 4: {multiplos_de_3_ou_4}")