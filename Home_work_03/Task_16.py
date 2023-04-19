import random

n = int(input('\n\nDefine number of elements: '))
print(f"Size of array is {n}\n")
arr = [random.randint(0,11) for _ in range(n)]
print(arr)   
x = int(input('\nWhat is number to check on entry: '))
print(f"X = {x}")
result = arr.count(x)
print(f"X ({x}) met in array {result} times\n\n")

