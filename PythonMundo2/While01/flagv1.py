print("Digite 999 caso queira parar!")

count = total = n = 0

#Para desconsiderar o 999 na soma
n = int(input("Digite um número: "))

while n != 999:
  total += n
  count += 1
  n = int(input("Digite um número: "))
print("Você digitou {} números e o resultado da soma foi {}.".format(count, total))