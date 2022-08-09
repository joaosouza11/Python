def readInt(msg):
  while True:
    try:
      n = int(input("Type an integer number: "))
    except (ValueError, TypeError):
      print("\033[31mERROR: Please type an integer valid number.\033[m")
      continue
    except KeyboardInterrupt:
      print("\033[31mUser didn't type the number.\033[m")
      return 0
    else:
      return n


def readFloat(msg):
  while True:
    try:
      n = float(input("Type a float number: "))
    except (ValueError, TypeError):
      print("\033[31mERROR: Please type an float valid number.\033[m")
      continue
    except KeyboardInterrupt:
      print("\033[31mUser didn't type the number.\033[m")
      return 0
    else:
      return n

#Main
n1 = readInt("Type an integer number: ")
n2 = readFloat("Type an float number: ")
print(f"You typed int({n1}), float({n2})")