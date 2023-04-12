# Você foi contratado para desenvolver um sistema de login para um aplicativo da web. Sua primeira tarefa é criar uma tela de login para autenticar os usuários. Para isso, você precisa escrever um programa em Python que solicita ao usuário um nome de usuário e uma senha. Em seguida, o programa verifica se o nome de usuário e a senha correspondem a um par de login válido.
# Se o login for bem-sucedido, o programa deve exibir uma mensagem de boas-vindas com o nome de usuário. Caso contrário, o programa deve exibir uma mensagem de erro informando que o nome de usuário ou senha são inválidos.

usuario = input('Digite seu nome usuário: ')
senha = input('Digite sua senha: ')

usuario_correto = 'leonid'
senha_correta = '123'

if usuario == usuario_correto and senha == senha_correta:
    print(f'Bem-vindo, {usuario}!')
else:
    print(f'Usuário ou senha incorreta!!!')
