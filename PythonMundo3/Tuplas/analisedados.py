num = (int(input("Digite o 1° número: ")), 
       int(input("Digite o 2° número: ")), 
       int(input("Digite o 3° número: ")), 
       int(input("Digite o 4° número: ")))

print(f"Você digitou {num}")

print(f"O número 9 apareceu {num.count(9)} vezes")

if 3 in num:
  pos3 = num.index(3)+1
  print(f"O número 3 foi o {pos3}° a ser digitado")
else:
  print("O número 3 não foi digitado")

print("Número pares: ", end="")
for n in num:
  if n % 2 == 0:
    print(n, end=" ")