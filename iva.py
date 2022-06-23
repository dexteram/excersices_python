iva = int(input("Descuento : "))
costo = int(input('¿Cual es el monto a calcular?: '))
calculo = costo * iva / 100
print ("El calculo de IVA es: " + str(calculo) + "\n")
print("El monto total es: " + str(costo - calculo))