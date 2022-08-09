player = dict()
matches = list()

player["name"] = str(input("Player's name: "))
tot = int(input(f"Number of matches played by {player['name']}: "))
for c in range(0 , tot):
  matches.append(int(input(f"   How many gols at {c+1} match: ")))
player["gols"] = matches[:]
player["total"] = sum(matches)


#3 different ways to print out
print("-=" * 30)
print(player)

print("-=" * 30)
for k, v in player.items():
  print(f"The key {k} has the value {v}")

print("-=" * 30)
print(f"The player {player['name']} played {tot} matches.")
for i, v in enumerate(player['gols']):
  print(f"   ==> At match {i+1}, scored {v} gols.")
print(f"{player['name']} scored {player['total']} gols in total")