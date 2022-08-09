num = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatoreze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

continuar = "S"

while continuar == "S":
  while True:
    user = int(input("Digite um número entre 0 e 20: "))
    if 0 <= user <= 20:
      break
    print("Tente novamente. ", end="")
  print(f"Você digitou o número {num[user]}")
  continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]