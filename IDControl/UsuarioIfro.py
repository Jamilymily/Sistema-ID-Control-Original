import time
from abc import ABC

class Usuarioifro(ABC):
    def __init__(self, nome ,cpf,matricula, senha):
        self.__nome=nome
        self.__cpf=cpf
        self._matricula=matricula
        self.__senha=senha

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_matricula(self):
        return self.__matricula
    
    def get_senha(self):
        return self.__senha
    
    def criar_senha(self):
        self._senha= int(input("Digite sua senha:"))
        return self.__senha
    
    def set_senha(self, novasenha):
        self.__novasenha=("Digite sua nova senha:")
        self.__novasenha=self.__senhaprint("Senha alterada com sucesso")
    
