def msg(txt):
  l = len(txt) + 4
  print("~" * l)
  print(f"  {txt}")
  print("~" * l)

text = str(input("Type a message: "))
msg(text)