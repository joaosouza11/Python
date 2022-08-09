def readInt(msg):
  while True:
    try:
      n = int(input("Type an integer number: "))
    except (ValueError, TypeError):
      print("\033[31mERROR: Please type an valid number.\033[m")
      continue
    except KeyboardInterrupt:
      print("\033[31mUser didn't type any option.\033[m")
      return 0
    else:
      return n


def line(l=42):
  return "-" * l


def title(txt):
  print(line())
  print(txt.center(42))
  print(line())


def menu(list):
  title("Main Menu")
  c = 1
  for item in list:
    print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
    c += 1
  print(line())
  opt = readInt("\033[32mYour option: /033[")
  return opt