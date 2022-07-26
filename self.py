class Pelicula():
    # Constructor
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f"Se ha creado la pelicula {self.titulo}")
    # Destructor
    def __del__(self):
        print(f"Se ha borrado la pelicula {self.titulo}")

    # Redefinimos el metodo __str__
    def __str__(self):
        return f"Pelicula : {self.titulo} de duracion {self.duracion} minutos, lanzada en {self.lanzamiento}"

    # Redefinimos el metodo __len__
    def __len__(self):
        return self.duracion

    length = property(lambda self: self.duracion)

p = Pelicula("El padrino", 175, "1972")
print(p)
print(len(p))
# class Auto():
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         print(f"Se ha creado el auto {self.marca} {self.modelo} {self.color}")
#     def __del__(self):
#         print(f"Se ha borrado el auto {self.marca} {self.modelo}")

# A = Auto("Ford", "Mustang", "Rojo")