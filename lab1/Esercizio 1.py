word = input("inserire una parola: ")

for n in range(len(word)):
    q = n
    for i in range(len(word)):
        if n == 0:
            print(word[i])
        elif n + (len(word)-3) >= i and q <= n + (len(word)-2) and len(word[i:q+1]) >= n+1:
            print(word[i:q+1])
            q = q + 1