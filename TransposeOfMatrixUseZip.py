matrix = [(1, 2, 3), (5, 9, 17), (4, 9, 25), (11, 12, 30)]
for raw in matrix:
	print (raw)

print("\n")
t_matrix = zip(*matrix)
for raw in t_matrix:
	print (raw)