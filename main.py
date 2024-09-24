#Alunas: Ádiles Naiandra, Alice Néry, Ana Andrade, Jamily Emanuelle
#Turma: 2º ano informática vespertino
 
import time
from catraca import *

time.sleep(0.1)
print("*=*" * 16)
print("Olá,Seja bem-vindo(a) ao nosso Sistema IDCotrol.")
print("*=*"*16)
time.sleep(0.5)
while True:
    adicionar=input("\nVocê vai ser cadastrar na área aluno ou servidor?\n\n[A]Aluno\n[B]Servidor\n[C]Visitante\n\nResposta=")
    if adicionar.upper() == "A":
      print("*=*"*12)
      print("Você vai se cadastrar na área aluno")
      print("*=*"*12)
      aluno=Aluno(nome="", cpf="", matricula="", senha="", turma="")
      aluno.cadastrar_aluno()
      aluno.atualizar_turma()
      aluno.exibirDados_aluno()
      print("."*15)
      print("\nCadastrado na área aluno com sucesso")
      print("Agora você tem acesso a todos os serviços da catraca")
      print("."*15)
      break
    elif adicionar.upper()=="B":
      print("*=*"*12)
      print("Você vai se cadastra na área do servidor")
      print("*=*"*12)
      servidor=Servidor(nome="", cpf="", matricula="", senha="",departamento="")
      servidor.cadastrar_servidor()
      servidor.atualizar_departamento()
      servidor.exibirDados_servidor()
      print("\nCadastro realizado com sucesso:)\n")
      print("Agora você tem acesso a todos os serviços da catraca.")
      break
    elif adicionar.upper()=="C":
      print("*=*"*12)
      visitante= Visitante(nome="", cpf="",idade="", documento="")
      visitante.cadastrar_visitante()
      visitante.exibirDados_Visitante()
    
      break
      
# Caso a pessoa escolher a opção errada
      
    if adicionar.upper() not in ["A", "B", "C"]:
      print("Resposta inválida, tente novamente")
      continue