import json
import boto3
import pandas as pd
import openpyxl
s3 = boto3.client('s3')
s3_client = boto3.client('s3',
aws_access_key_id="",
aws_secret_access_key="",
aws_session_token="",
)

#declaracion_rutas
archivo_excel = ("C:\examples\excersices_python\query_config_aws.xlsx")
archivo_html = (r'C:\\Users\\jomvega\\Documents\\Health-checker.html')
Query_cuenta = ''
Query_buckets= ''
file_validator= 'Health-checker.html'
#consultar si el archivo existe
s3 = boto3.resource('s3')



#abrir excel para consultar Query_cuentas y nombres de buckets
df = pd.read_excel(archivo_excel,sheet_name='Hoja1',header=0)
for valor in df.values:
    Query_cuenta=(valor[0])
    Query_buckets=(valor[1])
    listObjSummary = s3.Bucket(Query_buckets).objects.all()
    for objsum in listObjSummary:
        # print('Item')
        # print(objsum.key)
        # print("Done")
        file = objsum.key
        # print(file)
        # print(file_validator)
        # if file in file_validator:
        if file == file_validator:
            print(True)
            print("el Bucket " + Query_buckets + " ya contiene el archivo Health-checker.html")
        else:
            print(False)
            print("el Bucket " + Query_buckets + " no contiene el archivo Health-checker.html")
            # response = s3.upload_file(archivo_html, Query_buckets, 'Health-checker.html')

    # print(Query_cuenta,Query_buckets)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        archivo = record['s3']['object']['key']
        
        print("BUCKET: "+str(Query_buckets))
        print("CUENTA: "+str(Query_cuenta))

    return {
        'statusCode': 200
    }



