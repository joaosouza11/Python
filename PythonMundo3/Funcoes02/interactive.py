def PyHelp(cmd):
  help(cmd)

def title(msg, color=0):
  l = len(msg) + 4
  print(c[color], end="")
  print("~" * l)
  print(f"  {msg}  ")
  print("~" * l)
  print(c[0], end="")


c = ('\033[m', #0 - No color
     '\033[0;30;41m', #1 - Red
     '\033[0;39;42m', #2 - Green
     '\033[0;30;43m', #3 - Yellow
     '\033[0;30;44m', #4 - Blue
     '\033[0;30;45m', #5 - Purple
     '\033[7;30m', #6 - White
     )

command = ""
while True:
  title("Help System PyHelp", 4)
  command = str(input("Function or Library > "))
  if command.upper() == "END":
    break
  else:
    PyHelp(command)
title("See you soon!", 2)