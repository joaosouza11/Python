from datetime import date, datetime

worker = dict()

worker["name"] = str(input("Name: ")).strip()
byear = int(input("Year of Birth: "))
worker["age"] = datetime.now().year - byear
worker["cardnum"] = int(input("Card Number (0 if doesnt have): "))
if worker["cardnum"] != 0:
  worker["yhire"] = int(input("Year of hire: "))
  worker["salary"] = float(input("Salary: $"))
  worker["retirement"] = worker["age"] + ((worker["yhire"] + 35) - datetime.now().year)

print("-=" * 20)
for k, v in worker.items():
  print(f" {k} it's {v}")