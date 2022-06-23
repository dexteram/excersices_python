edad1 = int(input("Ingrese su edad: "))
edad2 = int(input("Ingresa la edad de tu amigo: "))

if edad1 == edad2:
    print("Tienen la misma edad")
elif edad1 > edad2:
    print("Tienes más edad que tu amigo")
elif edad1 < edad2:
    print("Tu amigo tiene más edad que tú")
else:
    print("Tienen diferente edad")
    