# Disciplina: Programação Orientada a Objetos
# Turma: 2B Informática Vespertino
# Nomes: Geovana Evangelista Barros de Freitas
#        Gilvan Felipe Fagundes dos Santos
#        Larissa Nascimento Rodrigues
#        Maria Eduarda Araújo Frota Saraiva

from material import *
from usuario import *
from emprestimo import *
from excecao import ExcecaoContemNumero, ExcecaoContemLetras

listaProfessores = []
listaAlunos = []
listaObjetos= []
listaMateriais = []
listaEmprestimo = []

while True:
    print("\n-----Sistema de Gerenciamento de Materiais Esportivos-----")
    print("Olá! O que você deseja?")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    
    try:
        opcao = int(input("Digite a sua opção: "))
        
    except ValueError:
        print("Opção inválida, digite uma das opções apresentadas.")
        continue
    
    finally:
        print("A opção foi inserida")

    #Cadastrar
    if opcao == 1:
        print("\nMenu:")
        print("1 - Professor")
        print("2 - Aluno")
        print("3 - Sair")
        
        while True:
            try:
                opcao = int(input("Digite a sua opção: "))
        
            except ValueError:
                print("Opção inválida, digite uma das opções apresentadas.")
                continue
            
            finally:
                print("A opção foi inserida.\n")
                
            break

        #Cadastrar Professor
        if opcao == 1:
            print("-----Realize o seu cadastro como professor-----")
            usuario = Professor()
            usuario.cadastro()
            listaProfessores.append(usuario)
            listaObjetos.append(usuario)

            print("\nMenu:")
            print("1 - Login")
            print("2 - Sair")
            
            while True:
                try:
                    opcao = int(input("Digite a sua opção: "))
            
                except ValueError:
                    print("Opção inválida, digite uma das opções apresentadas.")
                    continue
                
                finally:
                    print("A opção foi inserida.\n")
                    
                break

            #Login
            if opcao == 1:
                usuario.login(listaProfessores)
                while True:
                    print("\nMenu:")
                    print("1 - Mudar senha")
                    print("2 - Verificar usuários")
                    print("3 - Exibir minhas informações")
                    print("4 - Exibir materiais")
                    print("5 - Cadastrar material")
                    print("6 - Editar informações sobre o material(Quantidade total)")
                    print("7 - Sair")
                    
                    while True:
                        try:
                            opcao = int(input("Digite a sua opção: "))
                    
                        except ValueError:
                            print("Opção inválida, digite uma das opções apresentadas.")
                            continue
                        
                        finally:
                            print("A opção foi inserida.\n")                       
                        
                        break
                    
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

                    #Exibir a lista de materiais já cadastrados no sistema
                    elif opcao == 4:
                        print("\nLista de materiais:")
                        for item in listaMateriais:
                            item.exibirMaterial()  

                    #Cadastrar um novo material e adicioná-lo na lista
                    elif opcao == 5:
                        item = Material()
                        item.cadastrarNovoMaterial()
                        listaMateriais.append(item)   

                    #Alterar quantidade total
                    elif opcao == 6:
                        for item in listaMateriais:
                            item.exibirMaterial()
                        itemEscolhido = input("Qual item deseja editar?")
                        for item in listaMateriais:
                            if item.getNomeMaterial() == itemEscolhido:
                                item.registrarQtdTotal()

                    elif opcao == 7:
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
            
            while True:
                try:
                    opcao = int(input("Digite a sua opção: "))
            
                except ValueError:
                    print("Opção inválida, digite uma das opções apresentadas.")
                    continue
                
                finally:
                    print("A opção foi inserida.\n")
                
                break
            
            if opcao == 1:
                usuario.login(listaAlunos)
                while True:
                    print("\nMenu:")
                    print("1 - Mudar senha")
                    print("2 - Exibir minhas informações")
                    print("3 - Exibir materiais")
                    print("4 - Solicitar materiais")
                    print("5 - Finalizar empréstimo")
                    print("6 - Exibir resumo do empréstimo")
                    print("7 - Sair")
                    
                    while True:
                        try:
                            opcao = int(input("Digite a sua opção: "))
                    
                        except ValueError:
                            print("Opção inválida, digite uma das opções apresentadas.")
                            continue
                        
                        finally:
                            print("A opção foi inserida.\n")
                
                        break
                    
                    #Mudar senha
                    if opcao == 1:
                        usuario.setSenha()

                    #Exibir as próprias informações
                    elif opcao == 2:
                        usuario.verificarInfos()

                    #Exibir a lista de materiais já cadastrados no sistema
                    elif opcao == 3:
                        print("\nLista de materiais:")
                        for item in listaMateriais:
                            item.exibirMaterial()

                    #Solicitar materiais
                    elif opcao == 4:
                        m1 = MaterialEmprestado()
                        emprestimo01 = Emprestimo(usuario, m1)
                        m1.emprestar(listaMateriais)
                        emprestimo01.registrarEmprestimo()
                        listaEmprestimo.append(emprestimo01)
 
                    #Finalizar empréstimo
                    elif opcao == 5:
                        if listaEmprestimo == []:
                            print("\nNenhum empréstimo realizado.")
                        else:
                        
                             if usuario == emprestimo01.getAluno():
                                emprestimo01.finalizarEmprestimo(listaEmprestimo, usuario)

                             else:
                                print("\nNenhum empréstimo realizado.")
                            

                    #Exibir resumo do empréstimo
                    elif opcao == 6:
                        if listaEmprestimo == []:
                           print("\nNenhum empréstimo realizado.")
                        else:
                            for emprestimo in listaEmprestimo:
                                if usuario == emprestimo01.getAluno():
                                    emprestimo01.exibirResumo(listaEmprestimo,usuario)
                                    break
                                
                                else:
                                    print("\nNenhum empréstimo realizado.")

                    elif opcao == 7:
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