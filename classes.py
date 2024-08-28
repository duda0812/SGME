class Usuario:
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

    def cadastro(self):
        print("Faça seu cadastro")
        self.__nome = input("Digite seu nome: ")
        self.__matricula = input("Digite sua matricula: ")
        self.__senha = input("Digite sua senha: ")

        print("Cadastro realizado com sucesso!!!")

    def login(self,lista):
        print("Faça seu login")
        matricula = input("Insira sua matrícula: ")
        senha = input("Insira sua senha: ")
        if len(lista) > 0:
            for c in lista: 
                if c.getMatricula() == matricula and c.getSenha() == senha:
                    print(f"login realizado com sucesso, seja bem vindo/a {self.__nome}!")
                else:
                    print("senha ou matrícula incorretas")
        

    def exibirUsuario(self):
        print(f"Nome: {self.__nome}\nMatrícula: {self.__matricula}")

class Professor(Usuario):
    def __init__(self):
        super().__init__()


class Aluno(Usuario):
    def __init__(self):
        super().__init__()
