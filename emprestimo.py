
from datetime import datetime, timedelta

from usuario import *
from material import *

#A classe Emprestimo se relaciona com MaterialEmprestado por composição.
class Emprestimo:
    def __init__(self, aluno, materialEmprestado):
        self.__aluno = aluno
        self.__dataEmprestimo = datetime.now()
        self.__dataLimiteDevolucao = self.__dataEmprestimo + timedelta(days = 7) 
        self.__dataDevolucao = None
        self.__material = materialEmprestado

    def getAluno(self):
        return self.__aluno
    
    def registrarEmprestimo(self): 
        if self.validarEmprestimo() == True:
            print("Empréstimo autorizado.")
            print(f"Aluno: {self.__aluno.getNome()}")
            print(f"Data do empréstimo: {self.__dataEmprestimo}")
            print(f"Data limite para a devolução: {self.__dataLimiteDevolucao}")
            print(f"Material: ") 
            for material in self.__material.getRelacao():
                print(f"{material.getNomeMaterial()}")
            print(f"{self.__material.getQuantidadeItens()} itens emprestados.")

        else:
            print("Empréstimo não autorizado")

    def validarEmprestimo(self):
        if self.__material.getQuantidadeItens() > 0:
            print("Material disponível para empréstimo.")
            return True
        
        else:
            print("Material indisponível para empréstimo.")
            return False

    def exibirResumo(self, lista,usuario):
        if lista != []:
            for i in lista:
                if usuario == i.getAluno():
                    print("\nResumo do Empréstimo")
                    print(f"Aluno: {self.__aluno.getNome()}")
                    print(f"Data do empréstimo: {self.__dataEmprestimo}")

                    if self.__dataDevolucao == None:
                        self.__dataDevolucao = "Ainda não foi devolvido"
                    else:
                        self.__dataDevolucao

                    print(f"Data de devolução: {self.__dataDevolucao}")
                    print(f"Material: ") 
                    for material in self.__material.getRelacao():
                        print(f"{material.getNomeMaterial()}")
                    print(f"{self.__material.getQuantidadeItens()} itens emprestados.")
        
        else:
            print("\nNenhum empréstimo realizado.")

    def finalizarEmprestimo(self, lista, usuario):
        if lista != None:
            for i in lista:
                if usuario == i.getAluno():
                    self.__dataDevolucao = datetime.now()
                    print(f"Empréstimo finalizado.\nMaterial devolvido em {self.__dataDevolucao}")
             
        else:
            print("\nNenhum empréstimo realizado.")