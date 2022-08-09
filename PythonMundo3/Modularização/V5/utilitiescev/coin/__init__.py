def half(n=0, formata=False):
  ans = n / 2
  return ans if formata == False else coin(ans)


def double(n=0, formata=False):
  ans = n * 2
  return ans if formata == False else coin(ans)


def increase(n=0, tax=0, formata=False):
  ans = n + (n * tax / 100)
  return ans if formata == False else coin(ans)


def discount(n=0, tax=0, formata=False):
  ans = n - (n * tax / 100)
  return ans if formata == False else coin(ans)


def coin(n=0, currency="R$"):
  return f"{currency}{n:.2f}".replace('.', ',')


def overview(n=0, itax=10, dtax=5):
  print("~" * 35)
  print("Price Overview".center(35))
  print("~" * 35)
  print(f"Analyzed Price: \t{coin(n)}")
  print(f"Half Price: \t\t{half(n, True)}")
  print(f"Double Price: \t\t{double(n, True)}")
  print(f"Increasing {itax}%: \t{increase(n, itax, True)}")
  print(f"Discounting {dtax}%: \t{discount(n, dtax, True)}")
  print("~" * 35)