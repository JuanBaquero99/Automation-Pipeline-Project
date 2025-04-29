import boto3

file_name = 'results/project_report.pdf'
bucket_name = 'automation-pipeline-pdfs'
object_name = 'report.pdf'

# Crear cliente de S3

s3 = boto3.client('s3')

try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"Archivo {file_name} subido a S3 en el bucket {bucket_name} con el nombre {object_name}.")
except Exception as e:
    print(f"Error al subir el archivo: {e}")