m = [[1 , 2], [3 , 5], [9 , 14]]
for raw in m :
	print (raw)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for raw in rez :
	print(raw)