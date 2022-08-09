from random import randint
from time import sleep

#Diálogo
print("Olá, sou o seu computador")
sleep(1)
print("Estou pensando em um número de 0 a 10")
sleep(1)
print("...")
sleep(2)

computador = randint(0, 10)
acertou = False
user = int(input("Pronto, tente adivinhar o número: "))

#Se o usuário acertar de primeira
if user == computador:
    acertou = True
    print("Wow, você acertou de primeira!")
    exit()
tentativas = 1

#Outras tentativas
while not acertou:
  user = int(input("Tente novamente: "))
  tentativas += 1
  if user == computador:
    acertou = True
  #Dicas para o usuário
  else:
    if user > computador:
      print("Menos...")
    elif user < computador:
      print("Mais...")
print("Parabéns, você acertou em {} tentativas!".format(tentativas))