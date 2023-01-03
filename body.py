import json
body={}
res = {
  "statusCode": 200,
  "body": "{\"OrderResponseHeader\": {\"SuccessCode\": \"0\", \"Errors\": null, \"Timestamp\": \"2022-12-20T00:38:03.113-05:00\"}, \"MSSLDomainID\": \"DSMS20002924149\", \"MetaTag\": \"<meta name=\\\"_globalsign-domain-verification\\\" content=\\\"evn55wa1_HGq7B2JBNgxYuozzPH-M-Rq0DO7xvQDci\\\" />\", \"DnsTXT\": \"_globalsign-domain-verification=evn55wa1_HGq7B2JBNgxYuozzPH-M-Rq0DO7xvQDci\"}"
}
y = json.loads(res["body"])
print(y["MSSLDomainID"])
print(y["DnsTXT"])


# a= (res["body"][108:141])
# b= (res["body"][262:348])
# # b= (body["OrderResponseHeader"])
# print(a)
# print(b)
# print(b)

# for clave, valor in res.items():
#     print("el valor de la clave %s es %s" % (clave, valor))

# list(res)
# print(list(res))
# for k in res:
#     print(k)
#     for i in k:
#         print(i)

# new_res= res["body"]
# print(new_res)
# DnsTXT = "DnsTXT" + res["DnsTXT"]
# print(DnsTXT)

# for key in res:
#     new_res = (key, ":", res[key])
#     # print(key, ":", res[key])
# print(new_res)


# DnsTXT = "DnsTXT" + new_res["DnsTXT"]
# print(DnsTXT)

# user_split = "userid: " + event["userid"]

