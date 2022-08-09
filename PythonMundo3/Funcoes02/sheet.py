def sheet(name="<Unknown>", goals=0):
  print(f"The player {name} scored {goals} goal(s) at the championship")


n = str(input("Player's name: ")).strip()
g = str(input("Number of goals: ")).strip()
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n == "":
  sheet(goals=g)
else:
  sheet(name=n, goals=g)