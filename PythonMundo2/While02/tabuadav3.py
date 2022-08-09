while True:
  n = int(input("Você quer saber a tabuada de qual número? "))
  #Valor negativo
  if n < 0:
    break
  for i in range(1, 11):
    print(f"{n} x {i} = {n*i}\n", end="")
  print("-"*42)
  
print("Programa encerrado.")