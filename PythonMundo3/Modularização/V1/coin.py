def half(n):
  return n / 2

def double(n):
  return n * 2

def increase(n, tax):
  ans = n + (n * tax / 100)
  return ans

def discount(n, tax):
  ans = n - (n * tax / 100)
  return ans