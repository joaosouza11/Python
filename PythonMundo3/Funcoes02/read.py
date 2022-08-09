def readInt(msg):
  ok = False
  value = 0
  while True:
    n = str(input(msg))
    if n.isnumeric():
      value = int(n)
      ok = True
    else:
      print("\033[0;31mError. Type an integer valid number.\033[m")
    if ok:
      break
  return value

#Main program
n = readInt("Type a number: ")
print(f"You typed the number {n}")