maior = 0
menor = 0
nums = []

for c in range(0, 5):
  nums.append(int(input(f"Digite o valor da posição {c}: ")))
  if c == 0:
    maior = menor = nums[c]
  else:
    if c > maior:
      maior = nums[c]
    if c < menor:
      menor = nums[c]

print(f"O maior número foi o {maior} na posição ", end="")
for i, v in enumerate(nums):
  if v == maior:
    print(f"{i}...", end="")

print(f"\nO menor número foi o {menor} na posição ", end="")
for i, v in enumerate(nums):
  if v == menor:
    print(f"{i}...", end="")