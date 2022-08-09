def readMoney(msg):
  valid = False
  while not valid:
    entrancy = str(input(msg)).replace(',', '.').strip()
    if entrancy.isalpha():
      print(f"\033[0;31mERROR: '{entrancy}' is an invalid price\033[m")
    #For empty input
    elif entrancy == "":
      print(f"\033[0;31mERROR: 'empty' is an invalid price\033[m")
    else:
      valid = True
      return float(entrancy)