ticket = input() 
list = [int(a) for a in str(ticket)]

if len(list) % 2 != 0:
    print ("Warning: Input value should be even!\n"
           "(press CTRL + F5 to try again)")
elif sum(list [0 : len(list)//2]) == sum(list [len(list)//2 : len(list)]):
    print(f"Lucky ticket {sum(list [0 : len(list)//2])} = {sum(list [len(list)//2 : len(list)])}")
else:
    print(f"Ordinary ticket {sum(list [0 : len(list)//2])} is not as {sum(list [len(list)//2 : len(list)])}")
