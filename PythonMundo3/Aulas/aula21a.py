#docstrings

def contador(i, f, p):
  '''
  -> Contando do início até o fim de acordo com o passo.
  i = início
  f = fim
  p = passo
  '''
  c = i
  while c <= f:
    print(c, end = "...")
    c += p


help(contador)