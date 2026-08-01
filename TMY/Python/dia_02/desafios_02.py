# %%

# Escreva um programa que receba um número inteiro do usuário. 
# Utilize o operador de resto da divisão % para descobrir se o número é par ou ímpar e 
# exiba uma mensagem personalizada para cada caso usando if e else.

numero = int(input("Digite aqui seu numero: "))

# O operador % calcula o que resta da divisão por 2
if numero % 2 == 0:
    print("Seu numero é Par")
else:
    print("Seu numero é impar !!!")
