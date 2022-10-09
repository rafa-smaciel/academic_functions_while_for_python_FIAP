print("Tabuada")

tabuada = int(input("Informe a tuabuada desejada: "))

contadora = 1

while contadora <= 10:
    tabuada_calculada = tabuada * contadora
    print(f"{tabuada} x {contadora} = {tabuada_calculada}")
    contadora = contadora + 1