# Faça um programa em Python que solicite ao usuário 
# que digite uma senha. O programa deve continuar 
# pedindo a senha enquanto o usuário 
# não digitar a senha correta. 1234

# Quando o usuário digitar a senha correta, 
# o programa deve imprimir uma mensagem de 
# boas-vindas e encerrar a execução.

senha_correta = "1234"
senha_digitada = ""

while senha_correta != senha_digitada:
    senha_digitada = input("Digite sua senha: ")
    if senha_digitada != senha_correta:
        print("Senha incorreta, tente novamente!")
print("Bem-vindo!")
