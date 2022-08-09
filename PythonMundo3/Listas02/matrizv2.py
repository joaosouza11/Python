'''Aprimore o desafio da aula anterior, mostrando no final:
A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna.      
C) O maior valor da segunda linha.
'''
pares = tercoluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f"Digite um número para a posição [{l}][{c}]: "))
    #Somando valores pares
    if matriz[l][c] % 2 == 0:
      pares += matriz[l][c]

print("-=" * 20)

for l in range(0, 3):
  for c in range(0, 3):
    print(f"[{matriz[l][c]:^5}]", end=" ")
  print()

print("-=" * 20)

print(f"A soma dos valores pares foi {pares}")
#Somando a 3° coluna
for l in range(0, 3):
  tercoluna += matriz[l][2]
print(f"A soma dos valores da 3° coluna foi {tercoluna}")
#Maior valor 2° coluna
print(f"O maior valor da 2° coluna foi {max(matriz[1])}")

"""Outra maneira de descobrir o maior valor:

maior = 0
for c in range(0, 3):
  if c == 0 or matriz[1][c] > maior:
    maior = matriz[1][c]
"""