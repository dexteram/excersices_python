import pandas as pd
import openpyxl

archivo_excel = ("C:\examples\excersices_python\query_config_aws.xlsx")
df = pd.read_excel(archivo_excel,sheet_name='Hoja1',header=0)
# print(df.columns)
for valor in df.values:
    cuenta=(valor[0])
    bucket=(valor[1])
    print(cuenta,bucket)

# for data in df:
#     print(data.cell(row=1, column=1).value)

# print(df)
