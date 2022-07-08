def somma(n, sum = 0):
    if n == 0:
        return sum
    else:
        return somma(n - 1, sum + n)

print(somma(10))