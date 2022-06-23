from argparse import Namespace
import uuid

#forma larga de codigo
# namespace = uuid.NAMESPACE_DNS
# def generador_id(lista_usernames):
#     temp_dic = {}
#     for nombre in lista_usernames:
#         temp_dic.update({nombre:uuid.uuid5(namespace,nombre).hex})
#     return temp_dic

# usernames = ['Felipe_45', 'venito3','rafael6','rafaela9','Yesika97','Angelae20']
# usernames_id = generador_id(usernames)

#forma corta
namespace = uuid.NAMESPACE_DNS
usernames = ['Felipe_45', 'venito3','rafael6','rafaela9','Yesika97','Angelae20']
usernames_id = {nombre:uuid.uuid5(namespace,nombre).hex for nombre in usernames}

print(usernames_id)
