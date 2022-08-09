def area(width, length):
  print(f"The area of a {w} x {l} plot is equal to {w * l}m².")


print("Plot Control")
print("-=" * 7)

w = float(input("Width: "))
l = float(input("Length: "))
area(w, l)