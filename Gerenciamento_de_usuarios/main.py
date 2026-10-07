# Sistema de Gerenciamento de Usuários em Python
from Gerenciamento_de_usuarios.funcoes_gerenciar_usuarios import *

usuaris = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L" or opcao == "S":
    if opcao == "I":
        inserir(usuaris)


    elif opcao == "P":
        pesquisar(usuaris)

    elif opcao == "E":
        excluir(usuaris)

    elif opcao == "L":
        listar(usuaris)

    elif opcao == "S":
        salvar(usuaris)

    else:
        break
    opcao = perguntar()
