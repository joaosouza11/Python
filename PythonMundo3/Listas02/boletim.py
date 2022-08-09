'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

ficha = []

while True:
  nota = str(input("Nome do aluno: "))
  nota1 = float(input("Primeira nota: "))
  nota2 = float(input("Segunda nota: "))
  media = (nota1 + nota2) / 2
  ficha.append([nota, [nota1, nota2], media])
  avancar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
  if avancar == "N":
    break
print("-=" * 21)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-" * 26)
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
  print("-=" * 21)
  opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
  if opc == 999:
    print("Obrigado, volte sempre!")
    break
  if opc <= len(ficha) - 1:
    print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")