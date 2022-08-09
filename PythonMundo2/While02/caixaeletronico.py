print("-=" * 25)
print("{: ^50}".format("BANCO PYTHON"))
print("-=" * 25)

valor = int(input("Qual valor você quer sacar? R$"))
total = valor
totced = 0
ced = 200


while True:
  if total >= ced:
    total -= ced
    totced += 1
  else:
    if totced > 0:
      print(f"{totced} cédulas de R${ced}")
    if ced == 200:
      ced = 100
    elif ced == 100:
      ced = 50
    elif ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 5
    elif ced == 5:
      ced = 1
    totced = 0
    if total == 0:
      break

print("-=" * 25)
print("{: ^50}".format("Agradecemos sua visita, volte sempre!"))
print("-=" * 25)