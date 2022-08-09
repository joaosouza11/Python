from random import randint
from time import sleep
from operator import itemgetter

game = {"player01": randint(1, 6), 
        "player02": randint(0, 6), 
        "player03": randint(0, 6), 
        "player04": randint(0, 6)}
ranking = list()

#Sort
print("Sorted values: ")
for k, v in game.items():
  print(f"{k} rolled {v} on the dice")
  sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True) #Main line
print("-=" * 18)

#Showing ranking
print("RANKING")
for i, v in enumerate(ranking):
  print(f"{i+1}° place: {v[0]} with {v[1]}")
  sleep(1)