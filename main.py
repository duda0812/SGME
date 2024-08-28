'''Disciplina: Programação Orientada a Objetos
   Turma: 2B Informática Vespertino
   Nomes: Geovana Evangelista Barros de Freitas
          Gilvan Felipe Fagundes dos Santos
          Larissa Nascimento Rodrigues
          Maria Eduarda Araújo Frota Saraiva s2'''

from classes import *

listaObjetos = []
while True:
    print("Sistema de Gerenciamento de Materiais Esportivos")
    print("Menu:")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    opcao = int(input("Digite a sua opção: "))

    #Cadastrar
    if opcao == 1:
        print("Menu:")
        print("1 - Professor")
        print("2 - Aluno")
        print("3 - Sair")
        opcao = int(input("Digite a sua opção: "))

        #Cadastrar Professor
        if opcao == 1:
            usuario = Professor()
            usuario.cadastro()
            listaObjetos.append(usuario)
            print(listaObjetos)
            print("Menu:")
            print("1 - Login")
            print("2 - Sair")
            opcao = int(input("Digite sua opção: "))

            if opcao == 1:
                usuario.login(listaObjetos)

                print("Menu:")
                print("1 - Verificar usuários")
                print("2 - Sair")
                opcao = int(input("Digite sua opção: "))

                if opcao == 1:
                    for item in listaObjetos:
                        item.exibirUsuario()

                elif opcao == 2:
                    print("Encerrando o sistema...")
                    break

                else: 
                    print("\nOpção inválida")


            elif opcao == 2:
                print("Encerrando o sistema...")
                break

            else: 
                print("\nOpção inválida")
                continue


        #Cadastrar aluno
        elif opcao == 2:
            usuario = Aluno()
            usuario.cadastro()
            listaObjetos.append(usuario)
            print("Menu:")
            print("1 - Login")
            print("2 - Sair")
            opcao = int(input("Digite sua opção: "))
            
            if opcao == 1:
                usuario.login(listaObjetos)
    
            elif opcao == 2:
                print("Encerrando o sistema...")
                break
    
            else: 
                print("\nOpção inválida")
                continue

        #Sair
        elif opcao == 3:
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida")
            continue

    #Login
    elif opcao == 2:
        pass

    #Sair
    elif opcao == 3:
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida")
        continue
