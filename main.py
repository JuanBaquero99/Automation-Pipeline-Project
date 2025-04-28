import json
import os
from processor.order_processor import calculate_materials, estimate_freight_cost


def load_form_data(file_path): # Función que carga la data del formulario desde un archivo JSON
    with open(file_path, 'r') as file: # Comandos para abrir el archivo en modo lectura
        data = json.load(file) # Cargar el contenido del archivo JSON en un diccionario de Python
    return data 

def main():
    form_data = load_form_data('input/form_data.json') # Llamar a la función para cargar los datos del formulario desde el archivo JSON
    print("Form Data Loaded:") # Imprimir un mensaje indicando que los datos del formulario han sido cargados
    print(json.dumps(form_data, indent=4)) # Imprimir los datos del formulario en formato JSON con una indentación de 4 espacios

    # Procesamiemto de datos
    print("\nProcessing Data...") # Imprimir un mensaje indicando que se están procesando los datos
    materials = calculate_materials(form_data) # Llamar a la función para calcular los materiales requeridos

    # Peso simulado: 30 lb por caja de piso
    total_weight = materials["boxes_of_flooring"] * 30 # Calcular el peso total basado en el número de cajas de piso
    freight = estimate_freight_cost(form_data, total_weight) # Llamar a la función para estimar el costo de envío
    
    # Imprimir los resultados
    print("\nMaterials Required:") # Imprimir un mensaje indicando que se están mostrando los materiales requeridos
    print(json.dumps(materials, indent=4)) # Imprimir los materiales requeridos en formato JSON con una indentación de 4 espacios
    
    print("\nEstimated Freight Cost:") # Imprimir un mensaje indicando que se está mostrando el costo estimado de envío
    print(f"${freight} USD") # Imprimir el costo estimado de envío en formato de moneda

    # Guardar los resultados en un archivo JSON
    output_data = {
        'project_id': form_data['project_id'],
        'client_name': form_data['client_name'],
        'materials_required': materials,
        "estimated_freight_cost": freight
    }
    output_file_path = os.path.join('output', 'quotation.json') # Definir la ruta del archivo de salida

    with open(output_file_path, 'w') as outfile:
        json.dump(output_data, outfile, indent=4) # Abrir el archivo de salida en modo escritura

    # Crear la carpeta de resultados si no existe
    os.makedirs('results', exist_ok=True)

    with open('results/materials.json', 'w') as f:
        json.dump(materials, f, indent=4)

    # Corregido: Usar el valor calculado 'freight' en lugar de la función
    with open('results/freight.json', 'w') as f:
        json.dump({'estimated_freight_cost': freight}, f, indent=4)

    print("\nResults saved to 'results/' folder.")

if __name__ == "__main__":
    main()