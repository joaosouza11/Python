demaior = mcont = fmenor = 0

while True:
  print("-="*15)
  print("{: ^30}".format("CADASTRE UMA PESSOA"))
  print("-="*15)
  idade = int(input("Idade: "))
  if idade >= 18:
    demaior += 1

  gen = " "
  while gen not in "MF":
    gen = str(input("Sexo: [M/F] ")).strip().upper()[0]
  if gen == "M":
    mcont += 1

  if gen == "F":
    if idade < 20:
      fmenor += 1

  continuar = " "
  while continuar not in "SN":
    print("-"*30)
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if continuar == "N":
    break

print(f"Foram cadastrados {demaior} pessoas com mais de 18 anos")
print(f"Além de {mcont} homens no total")
print(f"E {fmenor} mulheres com menos de 20 anos")