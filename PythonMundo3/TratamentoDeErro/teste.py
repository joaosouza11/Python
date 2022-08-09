try:
  a = int(input("Numerador: "))
  b = int(input("Denominador: "))
  r = a / b
except (ValueError, TypeError):
  print("Tivemos um problema com o tipo de dado que você digitou")
except ZeroDivisionError:
  print(f"Não é possível dividir um número por 0")
except Exception as erro:
  print(f"Infelizmente tivemos um erro {erro.__class__}")
else:
  print(f"O resultado é {r:.1f}")
finally:
  print("Volte sempre! Muito obrigado!")