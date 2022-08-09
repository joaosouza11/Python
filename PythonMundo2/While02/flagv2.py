cont = soma = 0

print("Caso queira cancelar, digite 999")

while True:
  n = int (input("Digite um número: "))
  if n == 999:
    break
  soma += n
  cont +=1
print(f"Você digitou {cont} valores e a soma foi {soma}.")