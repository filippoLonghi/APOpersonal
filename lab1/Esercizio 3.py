inputFile = open(".\\data\\input.txt", "r")
outputFile = open(".\\data\\output.txt", "w")

lines = []
for line in inputFile:
    line = line.strip()
    lines.append(line)
    print(line)

for i in range(1,len(lines)+1):
    outputFile.write(lines[-i])
    outputFile.write("\n")
# lines = lines[-1::-1]
# for line in lines:
#     file.write(line)

inputFile.close()
outputFile.close()