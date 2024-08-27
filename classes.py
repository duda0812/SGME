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
        global listaMatricula
        listaMatricula = []
        global listaSenha 
        listaSenha = []
        print("Faça seu cadastro")
        nome = input("Digite seu nome: ")
        matricula = input("Digite sua matricula: ")
        listaMatricula.append(matricula)
        senha = input("Digite sua senha: ")
        listaSenha.append(senha)
        print("Cadastro realizado com sucesso!!!")

    def login(self):
        print("Faça seu login")
        matricula = input("Insira sua matrícula: ")
        senha = input("Insira sua senha: ")
        if matricula in listaMatricula and senha in listaSenha:
            print("Login realizado com sucesso")
        else:
            print("deu M")

    def exibirUsuario(self):
        print(f"Nome: {self.__nome}\nMatrícula: {self.__matricula}\nSenha: {self.senha}\n")

class Professor(Usuario):
    def __init__(self):
        super().__init__()


class Aluno(Usuario):
    def __init__(self):
        super().__init__()
