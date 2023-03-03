def main():
    num = int(input("Digite um numero: "))
    n = 0
    n1 = 1
    n2 = 1
    while(num > n2):
        n = n1
        n1 = n2
        n2 = n + n1
    print(n2)
    if(n2 == num):
        print("O numero pertence a sequencia de fibonacci")
    else: print("O numero nao pertence a sequencia de fibonacci")
main()
