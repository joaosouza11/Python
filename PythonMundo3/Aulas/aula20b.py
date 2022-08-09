def double(lst):
  pos = 0
  while pos<len(lst):
    lst[pos] *= 2
    pos += 1


values = [1, 2, 3, 4, 5, 6]
double(values)
print(values)