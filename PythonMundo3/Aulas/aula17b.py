#Ligando listas
a = [2, 4, 7, 9]
b = a
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")

print("-=" * 15)

#Copiando listas
a = [2, 4, 7, 9]
b = a[:]
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")