print("Gerador de Progressão Aritmética")
t = int(input("Primeiro termo: "))
r = int(input("Razão: "))

cont = 1

while cont <= 10:
  print("{} ➙  ".format(t), end="")
  t += r
  cont += 1
print("Fim")