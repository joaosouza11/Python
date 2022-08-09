import coin

p = float(input("Type the price: R$"))
print(f"The half of {p} is {coin.half(p)}")
print(f"The double of {p} is {coin.double(p)}")
print(f"Increasing 10%, we have {coin.increase(p, 10)}")
print(f"Discouting 13%, we have {coin.discount(p, 13)}")