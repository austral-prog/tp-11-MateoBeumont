def string_to_dict(s):
    ventas = {}
    partes = s.strip().split(';')
    for parte in partes:
        if parte:
            producto, valor = parte.split(':')
            valor = float(valor)
            if producto not in ventas:
                ventas[producto] = []
            ventas[producto].append(valor)
    return ventas


def process_dict(diccionario):
    resultados = {}
    for producto, lista in diccionario.items():
        total = sum(lista)
        promedio = total / len(lista)
        resultados[producto] = {
            'total': round(total, 2),
            'promedio': round(promedio, 2)
        }
    return resultados
