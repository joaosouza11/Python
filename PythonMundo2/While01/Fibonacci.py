print("-=" * 20)
print("Sequência de Fibonacci")
print("-=" * 20)

# 0 ➙ 1 ➙ 1 ➙ 2 ➙ 3 ➙ 5 ➙ 8 ➙ 13
n = int(input("Quantos números da sequência de Fibonacci você quer saber? "))
t1 = 0
t2 = 1

cont = 2

print("{} ➙  {}".format(t1, t2), end="")

while cont < n:
  t3 = t1 + t2
  print(" ➙  {}".format(t3), end="")
  t1 = t2
  t2 = t3
  cont +=1