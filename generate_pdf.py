import pdfkit
import json

# Carga los datos del JSON generado
with open('results/materials.json') as f:
    materials = json.load(f)

with open('results/freight.json') as f:
    freight = json.load(f)

# Crea contenido HTML para el PDF
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Project Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        h2 {{ color: #666; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ padding: 10px; border: 1px solid #ccc; text-align: left; }}
    </style>
</head>
<body>
    <h1>Materials Required</h1>
    <table>
        <tr><th>Material</th><th>Quantity</th></tr>
        <tr><td>Boxes of Flooring</td><td>{materials["boxes_of_flooring"]}</td></tr>
        <tr><td>Gallons of Adhesive</td><td>{materials["gallons_of_adhesive"]}</td></tr>
        <tr><td>Baseboard Length (ft)</td><td>{materials["baseboard_length_ft"]}</td></tr>
    </table>

    <h2>Estimated Freight Cost</h2>
    <p><strong>${freight["estimated_freight_cost"]} USD</strong></p>
</body>
</html>
"""

# Opcional: si wkhtmltopdf no está en el PATH, debes especificarlo:
# Configura la ruta a tu wkhtmltopdf.exe
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # <- Ajusta si está en otra carpeta
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Generar PDF
pdfkit.from_string(html_content, 'results/project_report.pdf', configuration=config)

print('PDF generado exitosamente en results/project_report.pdf')
