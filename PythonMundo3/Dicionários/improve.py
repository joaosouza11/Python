team = list()
matches = list()
player = dict()


while True:
  player.clear()
  player["name"] = str(input("Player's name: "))
  tot = int(input(f"Number of matches played by {player['name']}: "))
  matches.clear()
  for c in range(0 , tot):
    matches.append(int(input(f"   How many gols at {c+1}° match: ")))
  player["gols"] = matches[:]
  player["total"] = sum(matches)
  team.append(player.copy())
  while True:
    next = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]
    if next in "YN":
      break
    print("ERROR! Please type only Y or N.")
  if next == "N":
    break

#Showing team data
print("-" * 45)
print("cod ", end="")
for i in player.keys():
  print(f"{i:<15}", end="")
print()
print("-" * 45)
for k, v in enumerate(team):
  print(f"{k:>3} ", end="")
  for d in v.values():
    print(f"{str(d):<15}", end="")
  print()
print("-" * 45)

#Showing player data
while True:
  search = int(input("Show data of which player? (999 to stop) "))
  if search == 999:
    break
  if search >= len(team):
    print(f"ERROR! There is no player with code {search}")
  else:
    print(F"  --{team[search]['name']}'s data:")
    for i, g in enumerate(team[search]["gols"]):
      print(f"   At game {i+1} scored {g} gols.")
  print("-" * 45)