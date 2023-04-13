number = int(input("Input number: "))
print("Integer powers are: ")
k = 0
while 2**k <= number:
    print(f"{k} => {2**k}")
    k = k + 1
