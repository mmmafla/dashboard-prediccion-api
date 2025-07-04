from collections import defaultdict

def predecir_motivo(datos):
    """
    Predice el número aproximado de motivos para el próximo mes.
    """
    motivos_totales = defaultdict(int)
    
    for registro in datos:
        for motivo, cantidad in registro["motivo"].items():
            motivos_totales[motivo] += cantidad

    # Promedio entre todos los meses
    meses = len(datos)
    prediccion = {k: round(v / meses) for k, v in motivos_totales.items()}

    return prediccion