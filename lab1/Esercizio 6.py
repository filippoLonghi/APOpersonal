N = int(input("Inserire dimensione matrice: "))

matrice = []
for i in range(N):
    space = []
    for n in range(N):
        space.append(" ")
    matrice.append(space)

for rig in range(N):
    for col in range(N):
        if rig == 0 and col == 0:
            matrice[rig][col] = 1
        elif rig-1 < 0:
            matrice[rig][col] = matrice[rig][col-1]
        elif col-1 < 0:
            matrice[rig][col] = matrice[rig-1][col]
        else:
            matrice[rig][col] = matrice[rig-1][col] + matrice[rig][col-1]
        print(matrice[rig][col], "  ", end="")
    print()