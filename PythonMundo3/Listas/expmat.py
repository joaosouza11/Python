exp = str(input("Digite uma expressão: "))
pilha = []

for simb in exp:
  if simb == "(":
    pilha.append(simb)
  elif simb == ")":
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(simb)
      break

if len(pilha) == 0:
  print("Sua expressão está CORRETA")
else:
  print("Sua expressão está INCORRETA")