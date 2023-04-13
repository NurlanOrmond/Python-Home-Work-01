sum = int(input("Input sum of two numbers: "))
product = int(input("Input the product of that numbers: "))
limit = 1000
for i in range(limit):
    for j in range(limit):
        if sum == i + j and product == i * j:
            print(f"The one of numbers is: {i}")
            print(f"Another one is: {j}")