#Considera o primeiro | Ignora o último
#for c in range(10, 0, -1):
#  print(c)

s = 0
for i in range (0, 4):
  n = int(input("Digite um número: "))
  s += n
print("A somatória dos números foi: {}".format(s))