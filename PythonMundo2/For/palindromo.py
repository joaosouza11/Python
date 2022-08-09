frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)

reverso = "".join(reversed(junto))

print("""
Normal: {}
Reverso: {}
""".format(frase, reverso))

#Verificando a frase toda junta é igual a revertida
if junto == reverso:
  print("Esta frase é um POLÍDROMO!")
else:
  print("Esta frase NÃO é um POLÍDROMO!")