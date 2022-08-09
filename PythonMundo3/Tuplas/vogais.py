palavras = ("arrroz", "feijao", "batata", "macarrao", "couve", "espinafre", "lentilha", "suco")

for v in palavras:
  print(f"\nNa palavra {v.upper()} temos ", end="")
  for letra in v:
    if letra in "aeiou":
      print(letra.upper(), end=" ")