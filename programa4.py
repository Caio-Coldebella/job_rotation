def main():
    estado = input("Digite a sigla do estado: ")
    SP = 67836.43
    RJ = 36678.66
    MG = 29229.88
    ES = 27165.48
    Outros = 19849.53
    sum = SP + RJ + MG + ES + Outros
    if(estado == "SP"):
        print("A participacao do estado de SP foi de {}%".format((SP/sum)*100))
    elif(estado == "RJ"):
        print("A participacao do estado de RJ foi de {}%".format((RJ/sum)*100))
    elif(estado == "MG"):
        print("A participacao do estado de MG foi de {}%".format((MG/sum)*100))
    elif(estado == "ES"):
        print("A participacao do estado de ES foi de {}%".format((ES/sum)*100))
    else:
        print("A participacao dos outros estados foi de {}%".format((Outros/sum)*100))
main()