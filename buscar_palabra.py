from cgitb import text


texto = ['Hola, este en el equipo de robotica!, de la evc de evolción digital',
'y este es un ejercicio de practica',
'para aprender mucho mas y mas de python pero ya no para robotica']
#forma larga de codigo
# def encontrar_palabra(texto):
#     lista = []
#     for linea in texto:
#         if 'robotica' in linea:
#             lista.append((True, linea))
#         else:
#             lista.append((False,linea))
#     return lista
#print(encontrar_palabra(texto))

#forma corta
print(list(map(lambda txt:(True,txt) if 'robotica' in txt else (False,txt),texto)))


