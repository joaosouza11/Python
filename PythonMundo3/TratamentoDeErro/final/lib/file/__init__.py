from lib.interface import *

def existFile(name):
  try:
    a = open(name, "rt") #Read Text
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True


def createFile(name):
  try:
    a = open(name, "wt+") #Write Text and Create a file if doesn't exist
    a.close()
  except:
    print("There was an error creating the file!")
  else:
    print(f"Thel file '{name}' was successfully created")


def readFile(name):
  try:
    a = open(name, "rt") #Read Text
  except:
    print("Failed to create file!")
  else:
    title("Registered People")
    for line in a:
      data = line.split(";")
      data[1] = data[1].replace("\n", "")
      print(f"{data[0]:<30}{data[1]:>3}")
  finally:
    a.close()


def register(fl, name="unknown", age="0"):
  try:
    a = open(fl, "at") #Append Text
  except:
    print("There was an error creating the file")
  else:
    try:
      a.write(f"{name};{age}\n")
    except:
      print("There was an error writing the data!")
    else:
      print(f"\033[1;32mNew record of {name} added\033[m")
      a.close()