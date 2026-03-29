import sys
from rich.console import Console  # Importamos Console de la librería rich

def analizar_sam(ruta):
    total = 0
    mapq_60 = 0

    with open(ruta, 'r') as fichero:
        for linea in fichero:
            # Ignoramos cabeceras o líneas en blanco
            if linea.startswith('@') or not linea.strip():
                continue

            columnas = linea.split('\t')

            # Comprobación de seguridad para evitar errores si la línea está mal formada
            if len(columnas) > 4:
                total = total + 1
                valor_mapq = int(columnas[4])

                if valor_mapq == 60:
                    mapq_60 = mapq_60 + 1

    # Iniciamos la consola de rich para la salida
    console = Console()

    if total > 0:
        porcentaje = (mapq_60 / total) * 100
        # Usamos console.print y ajustamos los textos exactos y a 1 decimal
        console.print(f"Total de lecturas alineadas: {total}")
        console.print(f"Lecturas con MAPQ = 60: {mapq_60}")
        console.print(f"Porcentaje: {porcentaje:.1f}%")
    else:
        console.print("El archivo estaba vacío o solo tenía cabeceras.")

# --- CUERPO PRINCIPAL ---
# Llamada directa al argumento de la línea de comandos
analizar_sam(sys.argv[1])
