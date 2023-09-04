import random

#definir lista
lista = [9557,5987,1279,7318,3803,6539,2013,3728,5328,3267]
numero_mayor = max(lista)
numero_menor = min(lista)

# Definir el rango de números
rango_inferior = numero_menor
rango_superior = numero_mayor

# Generar un número aleatorio dentro del rango definido
numero_aleatorio = random.randint(rango_inferior, rango_superior)

print(f"Número aleatorio generado: {numero_aleatorio}")
print(f"El número mayor es: {numero_mayor}")
print(f"El número menor es: {numero_menor}")
