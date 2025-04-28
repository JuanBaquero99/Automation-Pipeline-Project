def calculate_materials(form_data): #Calcula los materiales requeridos con base en el área y tipo de piso
    
    floor_area = form_data.get('floor_area_sqft', 0) #Área del piso en pies cuadrados
    
    #Suponiendo que cada caja de piso cubre 20 pies cuadrados
    
    sqft_per_box = 20
    number_of_boxes = floor_area / sqft_per_box #Número de cajas requeridas
    
    # Adhesivo: 1 galón cubre 220 sqft
    adhesive_coverage = 200
    number_of_adhesive_gallons = floor_area / adhesive_coverage #Número de galones de adhesivo requeridos
    
    # Zócalos: perimetro aproximado, asumiendo de forma cuadrada
    perimeter = (floor_area ** 0.5) * 4 #Perímetro en pies
    baseboard_length = perimeter #Longitud de zócalo en pies
    
    return {
        "boxes_of_flooring": round(number_of_boxes),
        "gallons_of_adhesive": round(number_of_adhesive_gallons),
        "baseboard_length_ft": round(baseboard_length)
    }

def estimate_freight_cost(form_data, total_weight_lbs): #Calcula el costo de envío basado en el peso total y la distancia
    
    #Para simular, 0.5 USD por libra + 50 USD de base por distancia promedio
    base_cost = 50
    cost_per_lb = 0.5
    estimated_cost = base_cost + (cost_per_lb * total_weight_lbs) #Costo estimado
    
    return round(estimated_cost, 2) #Redondear a 2 decimales
