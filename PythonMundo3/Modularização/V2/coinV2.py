def half(n=0):
  return n / 2

def double(n=0):
  return n * 2

def increase(n=0, tax=0):
  ans = n + (n * tax / 100)
  return ans

def discount(n=0, tax=0):
  ans = n - (n * tax / 100)
  return ans

def coin(n=0, currency="R$"):
  return f"{currency}{n:.2f}".replace('.', ',')