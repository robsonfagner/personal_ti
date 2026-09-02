
def soma(a:float, b:float, *args)-> float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)-> float:
    return soma (a,b, *args) / (len( args)+2)

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

print("Media: ", media(a,b,c))