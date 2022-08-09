def bigger( * num):
  count = bigger = 0

  print("-=" * 20)
  print("Analyzing the values...")

  for value in num:
    print(value, end=" ")
    if count == 0:
      bigger = value
    else:
      if value > bigger:
        bigger = value
    count += 1
    
  print(f"{count} values were reported in total.")
  print(f"The biggest value reported was {bigger}.")


bigger(2, 3, 5, 4, 7, 9)
bigger(32, 5, 42, 43, 6, 1)
bigger(3, 7, 2)
bigger(6)
bigger()