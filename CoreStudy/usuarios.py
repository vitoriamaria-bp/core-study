
def cadastrar_usuario():
    print('------ CADASTRO ------')
    nome = input('Digite seu nome completo: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    confirmacao_senha = input('Digite sua senha novamente: ')
    if senha == confirmacao_senha:
        print('Usuário cadastrado com sucesso!')
    else:
        print('Senhas não são iguais! Tente novamente.')

cadastrar_usuario()

def logar_usuario():
    print('------ LOGIN ------')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    print('Login realizado com sucesso!')

logar_usuario()