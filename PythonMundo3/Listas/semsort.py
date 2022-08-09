nums = []
for c in range(0, 5):
  n = int(input("Digite um valor: "))
  if c == 0 or n > nums[-1]:
    nums.append(n)
    print("Adicionando ao final da lista")
  else:
    pos = 0
    while pos < len(nums):
      if n <= nums[pos]:
        nums.insert(pos, n)
        print(f"Adicionando da posição {pos} da lista")
        break
      pos += 1
print("-=" * 10)
print(f"Os valores digitados em ordem foram {nums}")