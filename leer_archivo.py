import pandas as pd
#forma larga codigo
#archivo = open('C:\examples\excersices_python\\archivo_leer.txt','r')
# lineas = []
# for linea in archivo:
#     lineas.append(linea.strip())
# print(lineas)

#forma corta
print([linea.strip()for linea in open('C:\examples\excersices_python\\database.xlsx','r')])
# print([linea.strip()for linea in open('C:\examples\excersices_python\\archivo_leer.txt','r')])