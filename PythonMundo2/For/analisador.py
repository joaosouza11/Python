tot_idade = 0
media = 0
maior_idade = 0
nmv = "" #Nome do Mais Velho
tma20 = 0 #Total de Mulheres Abaixo dos 20 anos

for p in range(1,5):
  print("{}° Pessoa".format(p))
  nome = str(input("Nome: ")).strip()

  idade = int(input("Idade: "))
  tot_idade += idade

  sexo = str(input("Sexo [M/F]: ")).strip().upper()
  if p == 1 and sexo == "M":
    maior_idade = idade
    nmv = nome
  if idade > maior_idade and sexo == "M":
    maior_idade = idade
    nmv = nome
  
  if idade < 20 and sexo == "F":
    tma20 += 1

media = tot_idade / 4
print("A média de idade é {:.1f} anos;".format(media))
print("O homem mais velho tem {} anos e se chama {};".format(maior_idade, nmv))

#Para corrigir erro de plural
if tma20 == 1:
  print("Foi citada apenas {} mulher com menos de 20 anos.".format(tma20))
else:
  print("Foram citadas {} mulheres com menos de 20 anos.".format(tma20))