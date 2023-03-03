import json

def main():
    f = open("dados.json", "r")
    arr = f.read()
    f.close()
    arr = json.loads(arr)
    menor = {"dia": 0, "valor": 99999999 }
    maior = {"dia": 0, "valor": 0 }
    media = 0
    numdiasvalidos = 0
    for i in range(len(arr)):
        if(arr[i]["valor"] > 0):
            numdiasvalidos += 1
            media += arr[i]["valor"]
            if(arr[i]["valor"] < menor["valor"]):
                menor = arr[i]
            elif(arr[i]["valor"] > maior["valor"]):
                maior = arr[i]
    media = media/numdiasvalidos
    numdiassuperior = 0
    for i in range(len(arr)):
        if(arr[i]["valor"] > 0 and arr[i]["valor"] > media):
            numdiassuperior += 1
    print("O menor valor de faturamento ocorreu no dia {} e foi de {}".format(menor["dia"],menor["valor"]))
    print("O maior valor de faturamento ocorreu no dia {} e foi de {}".format(maior["dia"],maior["valor"]))
    print("O numero de dias no mes em que o valor de faturamento diario foi superior a media mensal foi de {} dias".format(numdiassuperior))
main()