n = 123
# n = 100
helper = 0
third = n % 10
helper = n // 10
second = helper % 10
helper //=  10
first = helper % 10

print(f"First: {first}  Second: {second} Third: {third} Sum: {first + second + third}")