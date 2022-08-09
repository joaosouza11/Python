#Tuplas são IMUTÁVEIS
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

for cont in range(0, len(lanche)):
  print(f"{lanche[cont]} está na posição {cont}")

print("-="*10)

for pos, comida in enumerate(lanche):
  print(f"{comida} está na posição {pos}")

print(sorted(lanche))

print("Comi muito")