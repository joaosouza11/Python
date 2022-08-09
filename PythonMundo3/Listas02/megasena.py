'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint

lista = list()
jogos = list()

print("-=" * 10)
print(f"PALPITES MEGA SENA")
print("-=" * 10)

quant = int(input("Quantos jogos vão ser gerados: "))
tot = 1
while tot <= quant:
  #Gerar números que não se repetem
  cont = 0
  while True:
    num = randint(1, 60)
    if num not in lista:
      lista.append(num)
      cont += 1
    if cont >= 6:
      break
  lista.sort()
  jogos.append(lista[:])
  lista.clear()
  tot += 1

for i, l in enumerate(jogos):
  print(f"Jogo {i+1}: {l}")

print("-=" * 6)
print(f"BOA SORTE!")
print("-=" * 6)