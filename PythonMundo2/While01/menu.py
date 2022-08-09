n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")

opcao = int(input("Qual a sua opção: "))

while opcao != 5:

  if opcao == 1:
    print("{} + {} = {}".format(n1, n2, n1 + n2))
    opcao = int(input("\nQual a sua opção: "))

  elif opcao == 2:
    print("{} x {} = {}".format(n1, n2, n1 * n2))
    opcao = int(input("\nQual a sua opção: "))

  elif opcao == 3:
    if n1 > n2:
      print("{} é maior que {}".format(n1, n2))
    elif n2 > n1:
      print("{} é maior que {}".format(n2, n1))
    else:
      print("Os números são iguais")
    opcao = int(input("\nQual a sua opção: "))
  
  elif opcao == 4:
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    opcao = int(input("\nQual a sua opção: "))

  else:
    opcao = int(input("Opção inválida. Qual a sua opção: "))