#Escreva um programa que receba um número inteiro do usuário. 
# Utilize o operador de resto da divisão % para descobrir se o número é par ou ímpar e exiba uma mensagem personalizada para cada caso usando if e else.
# Dica: Um número é par se o resto da divisão dele por 2 for igual a zero (numero % 2 == 0).

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