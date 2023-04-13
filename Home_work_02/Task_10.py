from random import randint
import random


n = int(input("Input number of coins: "))
randomCoinSide = list()
eagle = 0
tail = 0

for i in range(n):
    randomCoinSide.append(random.randint(0,1))
    
for i in range(len(randomCoinSide)):
    if randomCoinSide[i] == 0:
        eagle = eagle + 1
    else:
        tail = tail + 1

if eagle > tail:
    print(f"Turn {tail} coins of tail")
else:
    print(f"Turn {eagle} coins of eagle")

