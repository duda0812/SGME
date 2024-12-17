from abc import ABC
from excecao import ExcecaoContemNumero, ExcecaoContemLetras

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
        while True: 
            try:
                novasenha = input("Insira sua nova senha: ")
                if len(novasenha) < 6:
                    raise ValueError("A senha deve ter pelo menos 6 caracteres. Tente novamente.\n")
                
            except ValueError as ve:
                print(f"Erro: {ve}")
                continue
            
            else:
                self.__senha = novasenha 
                print("Senha alterada com sucesso!!!")
                
            break

    def cadastro(self):
        while True:
            try:
                self.__nome = input("Digite seu nome: ")
                if not self.__nome.isalpha():
                    raise ExcecaoContemNumero
                
                self.__matricula = input("Digite sua matricula: ")
                if not self.__matricula.isdigit():
                    raise ExcecaoContemLetras
                
                self.__senha = input("Digite sua senha (mínimo 6 caracteres): ")
                if len(self.__senha) < 6:
                    raise ValueError("A senha deve ter pelo menos 6 caracteres. Tente novamente.\n")
                
            except ExcecaoContemNumero:
                print("Contém números, deve ser digitado somente letras no 'Nome'.\n")
                continue
                
            except ExcecaoContemLetras:
                print("Contém letras, deve ser digitado somente número na 'Matrícula'.\n")
                continue
                
            except ValueError as ve:
                print(f"Erro: {ve}")
                continue
                
            break
        
    def login(self,lista):
        status = True
        while status:
            print("Faça seu login")
            matricula = input("Insira sua matrícula: ")
            senha = input("Insira sua senha: ")
            if len(lista) > 0:
                for c in lista: 
                    if c.getMatricula() == matricula and c.getSenha() == senha:
                        print(f"Login realizado com sucesso, seja bem vindo/a {self.__nome}!")
                        status = False
                        break
                    else:
                        print("Senha ou matrícula incorretas, tente novamente.\n")
                
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
