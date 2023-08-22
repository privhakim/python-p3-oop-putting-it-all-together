#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

if __name__ == "__main__":
    stan_smith = Shoe("Adidas", 9)
    print(stan_smith.brand)
    print(stan_smith.size)
    stan_smith.cobble()
    print(stan_smith.condition)
