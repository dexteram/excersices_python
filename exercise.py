#forma de juntar dos listas en un diccionario
nombres=['maria','pedro','juan','yulay']
salario=['1000$','400$','500$','0$']
info = {nombre:salario for nombre,salario in zip(nombres,salario)}
print(info)
