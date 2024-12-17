from usuario import *
from emprestimo import *

class Material:
    def __init__(self):
        self.__nomeMaterial = None
        self.__quantidadeTotal = None

    def getNomeMaterial(self):
        return self.__nomeMaterial
    
    def getQuantidadeTotal(self):
        return self.__quantidadeTotal
    
    def setQuantidadeTotal(self, novaQuantidade):
        if novaQuantidade >= 0:
            novaQuantidade= self.__quantidadeTotal 
        else:
            print("A quantidade não pode ser negativa. Tente novamente.")


    def cadastrarNovoMaterial(self):
        self.__nomeMaterial = input("\nInsira o nome do material: ")
        self.__quantidadeTotal = int(input("Insira a quantidade total desse material: "))

    def registrarQtdTotal(self):
        novaQuantidade = input("Insira a nova quantidade total: ")
        self.__quantidadeTotal = novaQuantidade

    def exibirMaterial(self):
        print(f"\n{self.__nomeMaterial}\nTotal = {self.__quantidadeTotal}")

#Classe MaterialEmprestado se relaciona com Material por agregação.
class MaterialEmprestado:
    def __init__(self):
        self.__quantidadeItens = None
        self.__relacao = []

    def getQuantidadeItens(self):
        return self.__quantidadeItens
    
    def getRelacao(self):
        return self.__relacao
    
    def emprestar(self, lista):
        quant = int(input("\nQuantos itens deseja pegar emprestado? "))
        self.__quantidadeItens = quant
        for c in range(quant):
            descricao = input("O que deseja? ")
            for item in lista:
                if item.getNomeMaterial() == descricao:
                    self.__relacao.append(item)