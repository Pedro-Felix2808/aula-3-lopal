numero = int(input("Digite o número que você quer a tabuada:  "))

cont = 1

while cont <= 10:
    resultado = numero * cont
    print(f"{numero} X {cont} = {resultado}")
    cont += 1