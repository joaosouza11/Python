lista = []
while True:
  n = int(input("Digite um valor: "))
  lista.append(n)
  continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
  if continuar == "N":
    break
print("-=" * 10)

#Tamanho da lista
print(f"Você digitou {len(lista)} valores")

#Ordem decrescente
lista.sort(reverse=True)
print(f"Em ordem decrescente: {lista}")

#Verificando o 5
if 5 in lista:
  print("O número 5 ESTÁ na lista")
else:
  print("O número 5 NÃO ESTÁ na lista")