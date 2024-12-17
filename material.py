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
    
    def cadastrarNovoMaterial(self):
        while True:
            try:
                self.__nomeMaterial = input("Insira o nome do material: ")
                if not self.__nomeMaterial.isalpha():
                    raise ExcecaoContemNumero
                
                self.__quantidadeTotal = int(input("Insira a quantidade total desse material: "))
                
            except ExcecaoContemNumero:
                print("Contém números, deve ser digitado somente letras no 'Nome do Material'.\n")
                continue
            
            except ValueError:
                print("Insira um valor correspondente ao que está sendo pedido. Tente novamente.\n")
                continue
                
            else:
                print("Cadastro de novo material realizado com sucesso!!!")
            
            break

    def registrarQtdTotal(self):
        while True:
            try:
                novaQuantidade = int(input("Insira a nova quantidade total: "))
                
            except ValueError:
                print("Insira um valor correspondente ao que está sendo pedido. Tente novamente.\n")
                continue
                
            else:
                self.__quantidadeTotal = novaQuantidade
                print("Quantidade total atualizada!!!")
            
            break

    def exibirMaterial(self):
        print(f"{self.__nomeMaterial}\nTotal = {self.__quantidadeTotal}")

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