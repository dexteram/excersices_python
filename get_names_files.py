import os
contenido = os.listdir('C:/Users/jomvega/Downloads/ids')
# print(contenido)

file = open('C:/Users/jomvega/Downloads/ids/list_ids.txt', 'w')

for file_id in contenido:
    file.write('linea' + file_id + os.linesep)
file.close()
    # print(file_id)