from abc import ABC
from exceçoes import *
from exceçoes import defNome
class Usuario(ABC):
    def __init__(self):
        self.__nome = None
        self.__matricula = None
        self.__senha = None

    def getNome(self):
        return self.__nome
    
    def getMatricula(self):
        return self.__matricula
    
    def getSenha(self):
        return self.__senha
    
    def setSenha(self):
        novasenha = input("\nInsira sua nova senha: ")
        self.__senha = novasenha 
        print("Senha alterada com sucesso!!!")

    def cadastro(self):
        # Raise lançando a exceção ValueError caso a pessoa digite algum caracter que não seja letra
        while True:
            try:
                nome = str(input("Digite seu nome: "))
                if all(n.isalpha() for n in nome.split(" ")):
                    print("nome válido")
                    self.__nome = nome
                else:
                    raise ValueError
                break
            except ValueError:
                print('O nome inserido contém caracteres que não são letras, tente novamente.') 
                           
        self.__matricula = input("Digite sua matricula: ")
        self.__senha = input("Digite sua senha: ")
        
    def login(self,lista):
        status = True
        while status:
            print("\nFaça seu login")
            matricula = input("Insira sua matrícula: ")
            senha = input("Insira sua senha: ")
            if len(lista) > 0:
                for c in lista: 
                    if c.getMatricula() == matricula and c.getSenha() == senha:
                        print(f"Login realizado com sucesso, seja bem vindo/a {self.__nome}!")
                        status = False
                        break
                    else:
                        print("Senha ou matrícula incorretas, tente novamente.")
                
    def exibirUsuario(self):
        print(f"\nNome: {self.__nome}\nMatrícula: {self.__matricula}")

    def verificarInfos(self):
        print(f"\nMeu usuário: {self.__nome}\nMatrícula: {self.__matricula}\nSenha: {self.__senha}")

#As classes Professor e Aluno se relacionam com a classe Usuário por meio de herança e com Empréstimo por associação.
class Professor(Usuario):
    def __init__(self):
        super().__init__()

class Aluno(Usuario):
    def __init__(self):
        super().__init__()
        self.__turma = None

    def getTurma(self):
        return self.__turma

    def cadastro(self):
        super().cadastro()
        self.__turma = input("Digite sua turma: ")

    def exibirUsuario(self):
        super().exibirUsuario()
        print(f"Turma: {self.__turma}")

    def verificarInfos(self):
        super().verificarInfos()
        print(f"Turma: {self.__turma}")
