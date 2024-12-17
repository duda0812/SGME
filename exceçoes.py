from material import *
from usuario import *
from emprestimo import *


# criando exceção que permite que o usuário digite apenas matrícula com 13 caracteres, sendo eles números.

class ExcecaoMatriculaInvalida(Exception):
    pass
    

def defMatricula(mat):
    if len(mat) > 13 or len(mat) < 13: 
        raise ExcecaoMatriculaInvalida()
        
    elif not mat.isnumeric():
        raise ExcecaoMatriculaInvalida()

    elif len(mat) == 13 and mat.isnumeric():
        print("matrícula válida")
        return True
