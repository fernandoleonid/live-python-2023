# - Você foi contratado por uma empresa de tecnologia para desenvolver um programa em Python 
# que calcule o ano de nascimento de uma pessoa com base na idade informada. 
# - A empresa precisa desse programa para utilizar em um cadastro de usuários em seu sistema.
# - O programa deve solicitar que o usuário digite o seu nome e a sua idade. 
# - Em seguida, o programa deve calcular o ano em que o usuário nasceu e 
# exibir uma mensagem na tela contendo o nome do usuário e o ano de nascimento.
# - Lembre-se que você não pode utilizar bibliotecas externas neste exercício. 
# O programa deve utilizar apenas variáveis, entrada e saída, e programação sequencial em Python.

# 1 - Ler nome e a idade
nome = input ('Digite seu nome:')
idade = int(input ('Dite sua idade:'))

# 2 - Calcular o ano de nascimento
ano_atual = 2023
ano_nascimento = ano_atual - idade

# 3 - Exibir o resultado
print("#"*50)
print(f"Olá {nome}\n"
      f"Você nasceu em: {ano_nascimento}")
