inputFile = open("C:\\Users\\Filippo Longhi\\OneDrive - Politecnico di Torino\\Politecnico\\Algoritmi e Programmazione ad Oggetti\\Laboratori\\APOpersonal\\lab1\\data\\input.txt", "r")
outputFile = open("C:\\Users\\Filippo Longhi\\OneDrive - Politecnico di Torino\\Politecnico\\Algoritmi e Programmazione ad Oggetti\\Laboratori\\APOpersonal\\lab1\\data\\output.txt", "w")

lines = []
for line in inputFile:
    line = line.strip()
    lines.append(line)
    print(line)
for i in range(1,len(lines)+1):
    outputFile.write(lines[-i])
    outputFile.write("\n")

inputFile.close()
outputFile.close()