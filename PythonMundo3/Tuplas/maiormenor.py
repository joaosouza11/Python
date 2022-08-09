from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os valores gerados foram ", end="")
for n in numeros:
  print(f"{n}", end=" ")

print(f"\nO maior valor gerado foi {max(numeros)}")

print(f"O menor valor gerado foi {min(numeros)}")