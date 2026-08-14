

p1 = int(input("Por favor digite a sua primeira nota: "))

p2 = int(input("Por favor digite a sua segunda nota nota: "))

media = (p1+p2)/2

if media >= 7:
    print(f"A sua média foi de : {media} e você está aprovado")
else:
    PF = int(input("Entre com a sua nota da PF:"))
    media2 = (media+PF)/2
    if media2 >=5:
        print("Aprovado com média:",media2)
    else:
        print("Está reprovado com médica:", media2)

