import random

n = int(input('\n\nDefine number of elements: '))
print(f"Size of array is {n}\n")
arr = [random.randint(0,10) for _ in range(n)]
print(arr) 
x = int(input('\n\nInput number to be checked: '))

difference = (arr[0] - x).__abs__()
min_difference = difference
result = 0
for i in arr:
    if(i - x).__abs__() < min_difference:
        min_difference = (i - x).__abs__()
        result = i

print(f"The closest element to {x} is {result}")        
