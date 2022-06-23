empleados = {'Ana':1000,
'adriana':900,
'jose':400,
'Nity':2000,
'Marcos':1100,
'Mariam':1450}

gana_mil_o_mas = []

#forma lineal de programacion
gana_mil_o_mas = [(key,values)for key, values in empleados.items()if values >=1000]


#forma larga
# for key,values in empleados.items():
#     if values >= 1000:
#         gana_mil_o_mas.append((key,values))

print(gana_mil_o_mas)