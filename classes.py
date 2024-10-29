from abc import ABC, abstractmethod

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
        self.__nome = input("Digite seu nome: ")
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
                        status=False
                        break
                    else:
                        print("Senha ou matrícula incorretas, tente novamente.")
    
        


    def exibirUsuario(self):
        print(f"\nNome: {self.__nome}\nMatrícula: {self.__matricula}")

    def verificarInfos(self):
        print(f"\nMeu usuário: {self.__nome}\nMatrícula: {self.__matricula}\nSenha: {self.__senha}")

# As classes Professor e Aluno se relacionam com a classe Usuário por meio de herança.
class Professor(Usuario):
    def __init__(self):
        super().__init__()

    
    



class Aluno(Usuario):
    def __init__(self):
        super().__init__()
        self.__turma= None

    def getTurma(self):
        return self.__turma

    def cadastro(self):
        super().cadastro()
        self.__turma = input("Digite sua turma: ")

    def exibirUsuario(self):
        super().exibirUsuario()
        print(f"Turma: {self.__turma} ")

    def verificarInfos(self):
        super().verificarInfos()
        print(f"Turma: {self.__turma} ")



class Material:
    def __init__(self):
        self.__nomeMaterial = None
        self.__quantidadeTotal = None
        self.__quantidadeEmprestada = None
        self.__quantidadeDisponivel = None


    def cadastrarNovoMaterial(self):
        self.__nomeMaterial = input("Insira o nome do material: ")
        self.__quantidadeTotal = int(input("Insira a quantidade total desse material: "))

    
        

    def registrarQtdTotal(self):
        pass

    def exibirMaterial(self):
        print(f"{self.__nomeMaterial} Total = {self.__quantidadeTotal}")


class MaterialEmprestado:
    def __init__(self):
        self.__quantidadeItens = None
        self.__relacao = None


    def Emprestar(self):
        pass


class Emprestimo:
    def __init__(self, aluno, professor, materialEmprestado):
        self.__aluno = aluno 
        self.__professor = professor
        self.__dataEmprestimo = None
        self.__dataLimiteDevolucao = None
        self.__dataDevolucao = None
        self.__material = materialEmprestado


    def registrarEmprestimo(self): 
        pass

    def validarEmprestimo(self):
        pass

    def exibirResumo(self):
        pass

    def finalizarEmprestimo(self):
        pass
