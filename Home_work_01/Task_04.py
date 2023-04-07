m = int(input("\n\nInput length of chocolate: "))
n = int(input("Input width of chocolate: "))
k = int(input("Input assumption of section: "))

def chocolate (m, n, k):
    if m <= 0 or n <= 0:
        return False
    elif m == 1 and n == 1:
        return False
    elif m == k or n == k or m * n - m == k or m * n - n == k:
        return True
    else:
        return False

print(f"Can be? - {chocolate(m, n, k)}\n\n")
