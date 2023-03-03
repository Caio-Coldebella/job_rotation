def main():
    word = input("String que sera invertida: ")
    result = ""
    for i in range(len(word)-1,-1, -1):
        result += word[i]
    print("Resultado: {}".format(result))

main()