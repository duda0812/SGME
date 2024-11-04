from abc import ABC, abstractmethod
from datetime import datetime, timedelta

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

    def consultarMateriais(self):
        pass

# As classes Professor e Aluno se relacionam com a classe Usuário por meio de herança.
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

    def solicitarMaterial(self):
        pass

class Material:
    def __init__(self):
        self.__nomeMaterial = None
        self.__quantidadeTotal = None
        self.__quantidadeEmprestada = None
        self.__quantidadeDisponivel = None

    def getNomeMaterial(self):
        return self.__nomeMaterial

    def cadastrarNovoMaterial(self):
        self.__nomeMaterial = input("Insira o nome do material: ")
        self.__quantidadeTotal = int(input("Insira a quantidade total desse material: "))

    def registrarQtdTotal(self):
        novaQuantidade = input("Insira a nova quantidade total: ")
        self.__quantidadeTotal = novaQuantidade

    def exibirMaterial(self):
        print(f"{self.__nomeMaterial}\nTotal = {self.__quantidadeTotal}\n")

class MaterialEmprestado:
    def __init__(self):
        self.__quantidadeItens = None
        self.__relacao = []

    def getQuantidadeItens(self):
        return self.__quantidadeItens
    
    def emprestar(self, lista):
        quant = int(input("Quantos itens deseja pegar emprestado? "))
        self.__quantidadeItens = quant
        for c in range(quant):
            descricao = input("O que deseja? ")
            for item in lista:
                if item.getNomeMaterial() == descricao:
                    self.__relacao.append(item)

class Emprestimo:
    def __init__(self, aluno, professor, materialEmprestado):
        self.__aluno = aluno 
        self.__professor = professor
        self.__dataEmprestimo = datetime.now()
        self.__dataLimiteDevolucao = self.__dataEmprestimo + timedelta(days = 7) 
        self.__dataDevolucao = None
        self.__material = materialEmprestado

    def registrarEmprestimo(self): 
        if self.validarEmprestimo():
            print("Empréstimo autorizado.")
            self.__material.emprestar()

        else:
            print("Empréstimo não autorizado")

    def validarEmprestimo(self):
        if self.__material.quantidadeDisponivel() > 0:
            print("Material disponível para empréstimo.")
            return True
        else:
            print("Material indisponível para empréstimo.")
            return False

    def exibirResumo(self):
        print("Resumo do Empréstimo")
        print(f"Aluno: {self.__aluno.getNome()}")
        print(f"Professor: {self.__professor.getNome()}")
        print(f"Data do empréstimo: {self.__dataEmprestimo}")
        print(f"Data de devolução: {self.__dataDevolucao}")
        print(f"Material: {self.__material.getNomeMaterial()}")

    def finalizarEmprestimo(self):
        self.__dataDevolucao = datetime.now()
        print(f"Empréstimo finalizado.\nMaterial devolvido em {self.__dataDevolucao}")
