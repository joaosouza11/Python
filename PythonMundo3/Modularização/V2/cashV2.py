import coinV2

p = float(input("Type the price: R$"))
print(f"The half of {coinV2.coin(p)} is {coinV2.coin(coinV2.half(p))}")
print(f"The double of {coinV2.coin(p)} is {coinV2.coin(coinV2.double(p))}")
print(f"Increasing 10%, we have {coinV2.coin(coinV2.increase(p, 10))}")
print(f"Discouting 13%, we have {coinV2.coin(coinV2.discount(p, 13))}")