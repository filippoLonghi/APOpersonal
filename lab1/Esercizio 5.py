num_int = input("Digitare un numero intero: ")

num_int_s = ""
while num_int != "":
    num_int_s += num_int
    num_int_s += " "
    num_int = input("Digitare un numero intero: ")

massimi_locali = ""
num_int_l = num_int_s.split()
for i in range(1, len(num_int_l)):
    if i+1 < len(num_int_l) and num_int_l[i-1] < num_int_l[i] and num_int_l[i+1] < num_int_l[i]:
        massimi_locali += str(i+1)
        massimi_locali += " "

if massimi_locali == "":
    print("Non ci sono massimi locali")
else:
    print("I massimi locali sono nelle posizioni (il primo numero è nella posizione 1): ", massimi_locali)