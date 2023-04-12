# Exercício: Média de notas
# O programa deve solicitar ao usuário que digite 
# a quantidade de notas que serão informadas.
# Em seguida, o programa deve solicitar que o 
# usuário digite cada nota.
# Ao final, o programa deve exibir a média das notas informadas

qtd_notas = int(input("Digite a quantidade de notas: "))
notas = []

while len(notas) < qtd_notas:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / qtd_notas

print(f"A média das notas é: {media}")