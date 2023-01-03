import json



file_name = 'excersices_python\\validar_json\\validar.json'

with open(file_name, 'r', encoding='utf-8') as f:
    my_data = json.load(f)
        
    for key in my_data.keys():
        print(key)
        # for key2 in body():
        #     print(key2)
# y = json.loads(getdomain["body"])
# # print(y["DomainName"])
    # new_data = my_data['DomainName']
# for domainName in my_data[1]:
#     print(domainName)
    # print(my_data)  # 👉️ {'name': 'Alice', 'age': 30}
    # print(my_data['DomainName'])  # 👉️ 'Alice'
    # print(type(my_data))  # 👉️ <class 'dict'>

