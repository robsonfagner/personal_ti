#Crie um programa que peça para o usuário digitar dois números (podem ser decimais, ou seja, float). 
# O programa deve comparar os dois valores e exibir na tela qual deles é o maior. 
# Caso os números sejam iguais, exiba uma mensagem informando que eles são idênticos.


numero1=float(input("Digite aqui o numero 1:"))
numero2=float(input("Digite aqui o numero 2:"))

if numero1 > numero2:
    print("O numero 2", numero1,"e maior!")
elif numero1==numero2:
    print("Os numeros sao iguais !!!!")
else:
    print("O numero 2", numero2,"e maior!")
