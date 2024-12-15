from material import *
from usuario import *
from emprestimo import *


def defNome(nome):

    if nome.isnumeric:
        print("contém números, digite apenas letras")
        return True
         
    else:
        print("passou")

        return False
        
        