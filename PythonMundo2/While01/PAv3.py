print("Gerador de Progressão Aritmética")
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

total = 0
cont = 1
mais = 10

while mais != 0:
  total += mais
  while cont <= total:
    print("{} ➙  ".format(termo), end="")
    termo += razao
    cont += 1
  print("Pausa")
  mais = int(input("Quantos termos você quer mostrar a mais? "))

print("Progressão finalizada com {} termos mostrados.".format(total))