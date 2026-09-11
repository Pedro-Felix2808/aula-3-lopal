quantidade = int(input("Digite a quantidade que você deseja: "))
paridade = input("Diga se quer par ou impar: ")

cont = 1
resultadop = 0
resultadoi = 1

if paridade == "par":
    while cont <= quantidade:
        print(f"Os pares são: {resultadop}")
        resultadop += 2
        cont +=1

else:
    while cont <= quantidade:
        print(f"Os impares são: {resultadoi}")
        resultadoi += 2
        cont +=1
