crew = list()
people = dict()
sum = average = 0

while True:
  people.clear()
  people["name"] = str(input("Name: "))

  while True:
    people["gender"] = str(input("Gender: [M/F] ")).strip().upper()[0]
    if people["gender"] in "MF":
      break
    print("ERROR! Please type only M or F")
  people["age"] = int(input("Age: "))
  sum += people["age"]
  crew.append(people.copy())

  while True:
    next = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]
    if next in "YN":
      break
    print("ERROR! Please type only Y or N")
  if next == "N":
    break

print("-=" * 20)
print(f"A) A total of {len(crew)} people were registred")
average = sum / len(crew)
print(f"B) The average age is {average:.2f} years old")
print(f"C) The registered woman were ", end="")
for p in crew:
  if p["gender"] == "F":
    print(p["name"], end=" ")
print()
print(f"D) List of people who are above of average: ")
for p in crew:
  if p["age"] >= average:
    print(p["name"], end=";")
    print()