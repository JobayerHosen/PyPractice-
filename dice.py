import random


class Dice:
    def roll(self):
        return random.randint(1,6), random.randint(1,6)  #returns a tuple


roll1 = Dice()
print(roll1.roll())