mercado = ["arroz", "feijão", "linguiça", "macarrao"]
mercado[2] = "batata"
print(mercado)

#Adicionar
#No final
mercado.append("cookies")
#Em qualquer lugar
mercado.insert(0, "limão")

#Deletar indice
del mercado[3]
mercado.pop() #Normalmente usa no final
mercado.pop(3)
#Deletar valor
mercado.remove("linguiça")

if "linguiça" in mercado:
  mercado.remove("linguiça")


valores = list(range(4, 11)) #Output: 4, 5, 6, 7, 8, 9, 10

valores = [4, 8, 3, 9, 1, 0]
#Organiza em ordem crescente
valores.sort()
#Organiza em ordem descrescente
valores.sort(reverse=True)
#Tamanho da lista
len(valores)