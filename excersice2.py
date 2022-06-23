nombres = ['fabiola', 'carlos','Juan']
#codigo en una sola linea
n = list(map(lambda nombre: nombre[0].upper() + nombre[1::],nombres))

#codigo en varias lineas
# def capital(nombre):
#     return nombre[0].upper() + nombre[1::]
# map(capital,nombres)
# n = list(map(capital,nombres))
print(n)


