def factorial(n, show=False):
  """
  -> Calculate a factorial of a number
  :param num: The number to be calculated
  :param show:(optional) Show or not the calculation
  :return: The factorial value of a number n
  """
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(c, end="")
      if c > 1:
        print(" x ", end="")
      else:
        print(" = ", end="")
    f *= c
  return f


#Main program
help(factorial)
print(factorial(5))
print(factorial(6, show=True))