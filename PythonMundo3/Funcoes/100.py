from random import randint

def raffle():
  print("The numbers draw were: ", end="")
  for i in range(0, 5):
    numbers.append(randint(1, 10))
  print(numbers)

def sumEven():
  sum = 0
  for e in numbers:
    if e % 2 == 0:
      sum += e
  print(f"The sum of the even numbers in the list was {sum}")


numbers = []
raffle()
sumEven()