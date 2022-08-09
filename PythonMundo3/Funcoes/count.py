from time import sleep

def count(a, b, c):
  if c < 0:
    c *= -1

  if c == 0:
    c = 1
  
  print("-=" * 20)
  print(f"Counting from {a} to {b} step {c} by {c}.")
  sleep(2.5)

  if a < b:
    cont = a
    while cont <= b:
      print(f"{cont} ", end="", flush=True)
      cont += c
      sleep(0.5)
    print("FIM!")
  else:
    cont = a
    while cont >= b:
      print(f"{cont} ", end="", flush=True)
      cont -= c
      sleep(0.5)
    print("FIM!")

count(1, 11, 1)
count(10, 0, 2)

print("-=" * 20)
print("Now it's your time! Choose: ")
start = int(input("Start: "))
end = int(input("End: "))
step = int(input("Step: "))
count(start, end, step)