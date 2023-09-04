import boto3
import csv

# Configura el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cambia 'us-east-1' por tu región

# Nombre de la tabla en DynamoDB
table_name = 'NombreDeTuTabla'

# Abre el archivo CSV
csv_file = 'archivo.csv'

# Itera sobre cada línea del archivo CSV y agrega los datos a la tabla de DynamoDB
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Reemplaza 'Columna1', 'Columna2', etc., con los nombres de las columnas en tu CSV
        item = {
            'Columna1': row['Columna1'],
            'Columna2': row['Columna2'],
            # Agrega más columnas según sea necesario
        }

        # Nombre de la clave primaria de tu tabla en DynamoDB
        primary_key = 'Columna1'

        # Nombre de la clave de clasificación de tu tabla en DynamoDB (si la tienes)
        # Si no tienes una clave de clasificación, puedes eliminar esta línea
        sort_key = 'Columna2'

        # Nombre de la clave primaria de tu tabla en DynamoDB (si tienes una clave de clasificación)
        # Si no tienes una clave de clasificación, puedes eliminar esta línea
        primary_key_value = row[primary_key]

        # Nombre de la clave de clasificación de tu tabla en DynamoDB (si la tienes)
        # Si no tienes una clave de clasificación, puedes eliminar esta línea
        sort_key_value = row[sort_key]

        # Obtiene la tabla en DynamoDB
        table = dynamodb.Table(table_name)

        # Inserta el elemento en la tabla DynamoDB
        table.put_item(
            Item=item,
            ConditionExpression=f"attribute_not_exists({primary_key})"  # Opcional: Evita duplicados
        )

        print(f"Insertado: {item}")
