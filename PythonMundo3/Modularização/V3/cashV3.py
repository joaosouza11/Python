import coinV3

p = float(input("Type the price: R$"))
print(f"The half of {coinV3.coin(p)} is {coinV3.half(p, True)}")
print(f"The double of {coinV3.coin(p)} is {coinV3.double(p, True)}")
print(f"Increasing 10%, we have {coinV3.increase(p, 10, True)}")
print(f"Discouting 13%, we have {coinV3.discount(p, 13, True)}")