print ("Input how many origami was made by Petya and Sergey together:")
s = int(input())
petyaCraft = s // 2
sergeyCraft = petyaCraft
katyaCraft = 2*(petyaCraft + sergeyCraft) 
print (f"Petya made {petyaCraft} origami, Sergey - {sergeyCraft}, Katya - {katyaCraft}")
print (f"Total origami: {petyaCraft + sergeyCraft +katyaCraft}")
