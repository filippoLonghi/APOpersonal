def factorial(number):
    result = 1
    for i in range(1, number+1):
        result = i * result
    return result

def coeffBinomiale(n, k):
    coefficiente_binomiale = factorial(n)/(factorial(k)*factorial(n-k))
    return coefficiente_binomiale

def main():
    done = False
    while not done:
        paramInput = input(
            'Inserire una coppia di numeri positivi nel formato (a,b), oppure (-1,-1) per arrestare il programma: ').strip("()").split(",")
        if int(paramInput[0]) == -1 and int(paramInput[1]) == -1:
            done = True
        elif int(paramInput[0]) <= int(paramInput[1]) and int(paramInput[0])>0 and int(paramInput[1])>0:
            param_k = int(paramInput[0])
            param_n = int(paramInput[1])
            print(int(coeffBinomiale(param_n, param_k)))
        elif int(paramInput[0]) > int(paramInput[1]) and int(paramInput[0])>0 and int(paramInput[1])>0:
            param_k = int(paramInput[1])
            param_n = int(paramInput[0])
            print(int(coeffBinomiale(param_n, param_k)))
        else:
            print("invalid input")

main()