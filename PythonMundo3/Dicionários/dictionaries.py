
repcard = dict()
print("Report Card in 0-10 format")
repcard["name"] = str(input("Student's name: "))
repcard["average"] = float(input(f"{repcard['name']}'s average: "))
if repcard["average"] < 5:
  repcard["situation"] = "flunk"
elif 5 <= repcard["average"] <= 7:
  repcard["situation"] = "recovery"
else:
  repcard["situation"] = "approved"
print("-=" * 21)

for k, v in repcard.items():
  print(f"- {k} it's {v}")