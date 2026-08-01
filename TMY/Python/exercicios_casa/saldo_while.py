#Crie um programa que receba de forma repetida vários valores de "saldo em conta" do usuário. 
# No entanto, o programa não tem um limite fixo de repetições: no momento em que o usuário apenas apertar "ENTER" sem digitar nenhum valor,
# o programa deve parar de receber dados (usando o comando break) e exibir a soma acumulada de todos os saldos digitados até ali.
# %%
acum = 0

while True:
    saldo = input("Digite aqui o seu saldo: ")
    if saldo == "":
        break

    acum += float(saldo)

print("A soma de todos os saldos é:", acum)

