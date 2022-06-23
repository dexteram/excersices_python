n1 = float(input('Digita el primer número: '))
n2 = float(input('Digita el segundo número: '))
n3 = float(input('Digita el tercer número: '))
n4 = float(input('Digita el cuarto número: '))

maximo=n1
if n2 > maximo:
    maximo = n2
if n3 > maximo:
    maximo = n3 
if n4 > maximo:
    maximo = n4
print('El número más grande es: ', maximo)