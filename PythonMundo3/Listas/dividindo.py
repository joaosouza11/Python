lista = []
par = []
impar = []
while True:
  n = int(input("Digite um valor: "))
  lista.append(n)
  continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
  if continuar == "N":
    break
  
print("-=" * 10)
print(f"A lista completa é {lista}")

for e in lista:
  if e % 2 == 0:
    par.append(e)
  else:
    impar.append(e)
print(f"Os números pares são {par}")
print(f"Os números ímpares são {impar}")