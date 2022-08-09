from lib.interface import *
from lib.file import *
from time import sleep

fl = "dataPeople.txt"

if not existFile(fl):
  createFile(fl)

while True:
  answer = menu(["List People", "New Register", "Leave"])
  if answer == 1:
    #Option: Listing file contents
    readFile(fl)
  elif answer == 2:
    #Option: Registering a new person
    title("New Register")
    name = str(input("Name: "))
    age = readInt("Age: ")
    register(fl, name, age)
  elif answer == 3:
    #Option: Leaving the system
    break
  else:
    print(f"ERROR. Type a valid option")
  sleep(2)