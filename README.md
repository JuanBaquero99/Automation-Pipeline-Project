
# Automation Pipeline Project

Este proyecto automatiza el proceso de generación de informes en formato PDF a partir de un conjunto de datos de materiales de construcción. Además, el proyecto integra la carga automática de archivos a **AWS S3** y la posible integración con **AWS Lambda** para procesamiento adicional.

## Estructura del Proyecto

```
automation-pipeline/
│
├── input/
│   └── materials_form.json       # Formulario de datos de entrada (ej. materiales de construcción)
│
├── output/
│   └── materials_report.pdf      # Informe generado en PDF
│
├── results/
│   ├── materials.json            # Resultados intermedios de procesamiento (materiales calculados)
│
├── generate_pdf.py               # Script para generar PDF a partir de los datos
├── main.py                       # Script principal para procesar el formulario
├── generate_pdf.py               # Función para generar el PDF y subir a S3
│
└── requirements.txt              # Dependencias del proyecto
```

## Requerimientos

Este proyecto utiliza las siguientes dependencias:

- **Python 3.11** o superior
- **Boto3**: para interactuar con AWS S3
- **WeasyPrint**: para generar archivos PDF desde HTML
- **Cffi**: dependencia para `WeasyPrint`
- **Pandas**: para procesar datos (si es necesario)

### Instalación

1. Clona el repositorio:
    ```bash
    git clone <repo_url>
    cd automation-pipeline
    ```

2. Crea un entorno virtual (opcional, pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate   # En Linux/macOS
    venv\Scriptsctivate      # En Windows
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### **Paso 1: Procesar el Formulario**

Ejecuta el script `main.py` para cargar el formulario de entrada y calcular los materiales requeridos:

```bash
python main.py
```

Este script generará un archivo `results/materials.json` con los resultados intermedios y los cálculos de los materiales.

### **Paso 2: Generar el Informe PDF**

Para generar el PDF con los materiales calculados, ejecuta:

```bash
python generate_pdf.py
```

Este script generará un archivo PDF (`output/materials_report.pdf`) con los detalles del informe de los materiales.

### **Paso 3: Subir el PDF a AWS S3**

Una vez que el PDF ha sido generado, puedes cargarlo a un bucket de S3 de la siguiente forma:

```python
import boto3

def upload_to_s3(file_name, bucket_name, object_name=None):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name or file_name)
        print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Llamada a la función para subir el PDF generado
upload_to_s3('output/materials_report.pdf', 'my-bucket-name', 'generated-reports/materials_report.pdf')
```

Este código sube el archivo PDF generado al bucket de S3.

### **(Opcional) Integración con AWS Lambda**

Puedes configurar un trigger en AWS Lambda para que se ejecute automáticamente cada vez que un archivo sea cargado a tu bucket S3. A continuación se muestra un ejemplo de código para la función Lambda:

```python
import json
import boto3

def lambda_handler(event, context):
    # Extraer la información del archivo subido
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    s3 = boto3.client('s3')
    
    try:
        # Realizar un procesamiento adicional, por ejemplo, enviar el archivo por email
        print(f"File uploaded: {file_name} in bucket {bucket_name}")
        # Aquí iría cualquier otra lógica adicional que quieras implementar

    except Exception as e:
        print(f"Error: {e}")
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps(f"File {file_name} processed successfully!")
    }
```

### **Tecnologías utilizadas**

- **Python 3.x**: Lenguaje principal para el desarrollo del pipeline.
- **Boto3**: SDK de AWS para interactuar con S3.
- **WeasyPrint**: Biblioteca para convertir HTML a PDF.
- **AWS Lambda**: Para el procesamiento automatizado de los archivos subidos a S3.
- **Cffi**: Para las dependencias de `WeasyPrint`.
- **HTML/CSS**: Usados para crear la plantilla de los informes en PDF.

## Licencia

Este proyecto está licenciado bajo la **MIT License**.
