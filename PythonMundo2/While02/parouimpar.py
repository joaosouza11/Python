from random import randint

v = 0

print("-="*13)
print("Vamos jogar Par ou Ímpar")
print("-="*13)

while True:
  user = int(input("Digite um valor: "))
  pc = randint(0, 10)
  soma = user + pc

  escolha = " " #Tem que estar dentro do laço para zerar em todas as rodadas
  while escolha not in "PI":
    escolha = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]

  print(f"Você jogou {user} e o computador {pc}, total de {soma}", end=" ")
  print("deu PAR" if soma % 2 == 0 else "deu ÍMPAR")
  #Par
  if escolha == "P":
    if soma % 2 == 0: 
      print("Você venceu!")
      v += 1
    else:
      print("Você perdeu!")
      break
  #Ímpar
  if escolha == "I":
    if soma % 2 == 1:
      print("Você venceu!")
      v += 1
    else:
      print("Você perdeu!")
      break
  print("Vamos jogar de novo")

print(f"O total foi {soma}")
print("GAME OVER")
print(f"Você conseguiu {v} vitórias!")