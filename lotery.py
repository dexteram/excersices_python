# import random

# # ¿Quién comienza?

# # comienza = random.randint(0000, 9999)
# # if comienza == 0:
# #     print('Comienza el jugador')
# # else:
# #     print('Comienza el PC')

# # Número aleatorio del parchís
# numero = random.randint(0000, 9999)
# print(numero)


#codigo 2

import random

# Simulación de ingreso de números aleatorios de 4 cifras
numeros_ingresados = [random.randint(1000, 9999) for _ in range(10)]
ultimos_10_resultados = [9557,5987,1279,7318,3803,6539,2013,3728,5328,3267]

# Simulación de ejecución semanal
for semana in range(1, 53):
    # Entrenamiento del "modelo" (en este caso, simplemente tomar el promedio de los números ingresados)
    promedio = sum(numeros_ingresados) / len(numeros_ingresados)
    promedio = sum(ultimos_10_resultados) / len(ultimos_10_resultados)

    # Predicción del siguiente número sumando 1 al promedio (simplificación)
    siguiente_numero = int(promedio) + 1
    
    print(f"Semana {semana}: Siguiente número predicho: {siguiente_numero}")
    
    # Actualización de los números ingresados con el nuevo número predicho
    # numeros_ingresados.append(siguiente_numero)
    # if len(numeros_ingresados) > 10:
    #     numeros_ingresados.pop(0)

    ultimos_10_resultados.append(siguiente_numero)
    if len(ultimos_10_resultados) > 10:
        ultimos_10_resultados.pop(0)
