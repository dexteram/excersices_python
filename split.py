# userid=""
# user_split=""
# name=""
# lastname=""
# listname = 0
event = { "body": {
  "profile_id": "44719_SMS2_3217",
  "domain_name": "testy.mpki.co",
  "vetting_level": "OV",
  "vetting_type": "DNS",
  "userid": "juan diego cubillos",
  "phone": "3116111240",
  "email": "jomvega@bancolombia.com.co"
}
}


user_split = event["body"]["userid"]
new_user_split = user_split.split()
email = event["body"]["email"]
print(email)
longitud =(len(new_user_split))

if longitud == 2:
      name = new_user_split[0]
      get_lastname = new_user_split[1]

      print("nombres: "+ name +" "+ get_lastname)

elif longitud >= 3:
      name = new_user_split[0]
      get_lastname = new_user_split[2]

      print("nombres: "+ name +" "+ get_lastname)

else:
      message = "Error: !Debe indicar nombres y apellidos!"
      print(message)



   
# for i in range(len(new_user_split)):
#     name = new_user_split[0]
#     lastname1 = new_user_split[2]
#     if lastname1





