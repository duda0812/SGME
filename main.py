'''Disciplina: Programação Orientada a Objetos
   Turma: 2B Informática Vespertino
   Nomes: Geovana Evangelista Barros de Freitas
          Gilvan Felipe Fagundes dos Santos
          Larissa Nascimento Rodrigues
          Maria Eduarda Araújo Frota Saraiva s2'''

from classes import *

listaProfessores = []
listaAlunos = []
listaObjetos= []

while True:
    print("\n-----Sistema de Gerenciamento de Materiais Esportivos-----")
    print("Olá! O que você deseja?")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    opcao = int(input("Digite a sua opção: "))

    #Cadastrar
    if opcao == 1:
        print("\nMenu:")
        print("1 - Professor")
        print("2 - Aluno")
        print("3 - Sair")
        opcao = int(input("Digite a sua opção: "))

        #Cadastrar Professor
        if opcao == 1:
            print("\n-----Realize o seu cadastro como professor-----")
            usuario = Professor()
            usuario.cadastro()
            listaProfessores.append(usuario)
            listaObjetos.append(usuario)
            print("Cadastro realizado com sucesso!!!")

            print("\nMenu:")
            print("1 - Login")
            print("2 - Sair")
            opcao = int(input("Digite sua opção: "))

            #Login
            if opcao == 1:
                usuario.login(listaProfessores)
                print("\nMenu:")
                print("1 - Mudar senha")
                print("2 - Verificar usuários")
                print("3 - Exibir minhas informações")
                print("4 - Sair")
                opcao = int(input("Digite sua opção: "))
                
                #Mudar senha
                if opcao == 1:
                    usuario.setSenha()
                
                #Exibir usuários do sistema
                elif opcao == 2:
                    for item in listaObjetos:
                        item.exibirUsuario()

                #Exibir as próprias informações
                elif opcao == 3:
                    usuario.verificarInfos()

                elif opcao == 4:
                    print("\nEncerrando o sistema...")
                    break

                else: 
                    print("\nOpção inválida")


            elif opcao == 2:
                print("\nEncerrando o sistema...")
                break

            else: 
                print("\nOpção inválida")
                continue


        #Cadastrar aluno
        elif opcao == 2:
            print("\n-----Realize o seu cadastro como aluno-----")
            usuario = Aluno()
            usuario.cadastro()
            listaAlunos.append(usuario)
            listaObjetos.append(usuario)
            print("Cadastro realizado com sucesso!!!")

            print("\nMenu:")
            print("1 - Login")
            print("2 - Sair")
            opcao = int(input("Digite sua opção: "))
            
            if opcao == 1:
                usuario.login(listaAlunos)
                print("\nMenu:")
                print("1 - Mudar senha")
                print("2 - Exibir minhas informações")
                print("3 - Sair")
                opcao = int(input("Digite sua opção: "))
                
                #Mudar senha
                if opcao == 1:
                    usuario.setSenha()

                #Exibir as próprias informações
                elif opcao == 2:
                    usuario.verificarInfos()

                elif opcao == 3:
                    print("\nEncerrando o sistema...")
                    break

                else: 
                    print("\nOpção inválida")
                    continue

    
            elif opcao == 2:
                print("\nEncerrando o sistema...")
                break
    
            else: 
                print("\nOpção inválida")
                continue


        elif opcao == 3:
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida")
            continue

    #Login
    elif opcao == 2:
        if len(listaObjetos) == 0:
            print("\nNão há usuários cadastrados no sistema")
            print("Realize o primeiro cadastrado!!!")
        else: 
            usuario.login(listaObjetos)

    #Sair
    elif opcao == 3:
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida")
        continue
