name1=""
name2=""
name3=""
name4=""
event = {
  "userid": "jomar arley vega cardona"
}
user_split = "userid: " + event["userid"]
user_split = user_split[8:]
new_user_split = user_split.split()
# print(new_user_split)
for user in new_user_split:
      name1 = user
      print(name1)

      # print("nombre :" + name1)
      # print("apellido :" + name1)
      # name2= new_user_split[user]
      # name3= new_user_split[user]
      # name4= new_user_split[user]
      # if name3 == "":
#       print("el valor " + name3 +"esta vacio")
# else:
#       name3= new_user_split[2]
# name4= new_user_split[3]
# if name4 == "":
#       print("el valor " + name4 +"esta vacio")
# else:
#       name4= new_user_split[3]


# name3= new_user_split[2]



# print(name1 +" "+ name2 +" "+ name3 +" "+ name4)
# print(name3 +" "+ name4)