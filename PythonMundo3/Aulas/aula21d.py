#Retorno de valores

def somar(a=0, b=0, c=0):
  s = a + b + c
  return s

r1 = somar(3, 5, 6)
r2 = somar(3, 3)
r3 = somar(1)

print(f"As somas valem {r1}, {r2} e {r3}")