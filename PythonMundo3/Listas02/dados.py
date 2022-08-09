'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas.  
C) Uma listagem com as pessoas mais leves.'''

main = []
temp = []
maior = menor = 0

while True:
  temp.append(str(input("Nome: ")))
  temp.append(float(input("Peso: ")))
  if len(main) == 0:
    maior = menor = temp[1]
  else:
    if temp[1] > maior:
      maior = temp[1]
    if temp[1] < menor:
      menor = temp[1]
  main.append(temp[:])
  temp.clear() #Limpar dados temporários

  avancar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if avancar == "N":
    break

print("-=" * 15)

#Lista dos maiores
print(f"{len(main)} pessoas foram cadastradas")
print(f"O maior peso foi de {maior}Kg. Peso de ", end="")
for p in main:
  if p[1] == maior:
    print(f"[{p[0]}] ", end="")

#Lista dos menores
print(f"\nO menor peso foi {menor}Kg. Peso de ", end="")
for p in main:
  if p[1] == menor:
    print(f"[{p[0]}] ", end="")