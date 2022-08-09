def vote(year):
  from datetime import date
  current = date.today().year
  age = current - year

  if 16 <= age < 18 or age > 65:
    return f"Your vote is OPCIONAL"
  elif age < 16:
    return f"You CAN'T vote yet"
  else:
    return f"Your vote is OBLIGATORY"


#Main program
yearBirth = int(input("Year of birth: "))
print(vote(yearBirth))