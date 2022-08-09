nums = []
while True:
  v = int(input("Digite um valor: "))
  if v not in nums:
    nums.append(v)
    print("Valor adicionado") 
  else:
    print("Este número já está na lista. Não irei adicioná-lo")
  cont = str(input("Você quer continuar: [S/N] ")).strip().upper()[0]
  if cont == "N":
    break

print(f"Você digitou os valores {sorted(nums)}")