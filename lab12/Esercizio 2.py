def binary(l, num = ""):
    if l == 0:
        print(num)
    else:
        for i in range(0,l*2):
            if i == 0 or i == 1:
                binary(l-1, num+str(i))

binary(4)