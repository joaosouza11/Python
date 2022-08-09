galera = []
dados = []

for i in range(0, 3):
  dados.append(str(input("Nome: ")))
  dados.append(int(input("Idade: ")))
  galera.append(dados[:])
  dados.clear()

for p in galera:
  print(f"{p[0]} tem {p[1]} anos de idade")