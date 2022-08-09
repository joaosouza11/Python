def half(n=0, formata=False):
  ans = n / 2
  return ans if formata == False else coin(n)


def double(n=0, formata=False):
  ans = n / 2
  return ans if formata == False else coin(n)


def increase(n=0, tax=0, formata=False):
  ans = n + (n * tax / 100)
  return ans if formata == False else coin(n)


def discount(n=0, tax=0, formata=False):
  ans = n - (n * tax / 100)
  return ans if formata == False else coin(n)


def coin(n=0, currency="R$"):
  return f"{currency}{n:.2f}".replace('.', ',')