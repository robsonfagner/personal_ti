


n1 = int(input('Digite a nota 1:'))
n2 = int(input('Digite a nota 2:'))
media = (n1+n2)/2

if media >= 7:
      print('O aluno foi aprovado')
else:
    pf=float(input('Entre com a nota da PF: '))
    segunda_media=(media+pf)/2
    
    if segunda_media >= 5:
        print('Aprovado')
    else:
        print('Barro')


