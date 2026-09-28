# Sistema de Gerenciamento de Usuários em Python
def perguntar():
    return str(input("<I> - Para inserir um usuário\n" +
              "<P> - Para pesquisar o usuário\n" +
              "<E> - Para excluir um usuário\n" +
              "<L> - Para listar um usuário\n" +
              "<S> - Para salvar o usuário\n" +
              "(APERTA ENTER PARA SAIR!)\n" 
                'O que deseja realizar?\n' )).upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input('Digite o nome: ').upper(),
                                                  input('Digite a última data de acesso: '),
                                                  input('Qual a última estação acessada: ').upper()]

def pesquisar(dicionario):
    visu = input("Digite o login: ").upper()
    if visu in dicionario:
        print(dicionario[visu])


def excluir(dicionario):
    while True:
        achar = input("Digite o login: ").upper()

        if achar in dicionario:
            del dicionario[achar]
            print('Login excluído!')
            break
        else:
            print('Você colocou o login errado! Coloque certo!')


def listar(dicionario):
    for n, d in dicionario.items():
        print(f'{n} {d}')


def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(f'{chave}: {str(valor)}\n')
