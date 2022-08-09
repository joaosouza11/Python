dados = ["Pedro", 25]
pessoas = []
pessoas.append(dados[:])

pessoas = [["Pedro", 25], ["João", 32], ["Maria", 19]]
print(pessoas[0][0]) #Output: Pedro
#Mostrar idades
for i in pessoas:
  print(i[1])