#Escopo de variáveis

def teste(b):
  #Escopos locais
  a = 8
  b += 4 
  c = 2
  print(f"A dentro vale {a}")
  print(f"B dentro vale {b}")
  print(f"C dentro vale {c}")


a = 5 #Escopo global
teste(a)
print(f"A fora vale {a}")