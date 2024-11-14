VALOR_DEL_DOLAR = 4484
VALOR_DEL_EURO = 4738
VALOR_DEL_YEN = 28.8

def convertir_pesos_a_dolares(pesos):
    return pesos / VALOR_DEL_DOLAR

def convertir_pesos_a_euros(pesos):
    return pesos / VALOR_DEL_EURO

def convertir_pesos_a_yenes(pesos):
    return pesos / VALOR_DEL_YEN

def convertir_dolares_a_pesos(dolares):
    return dolares * VALOR_DEL_DOLAR

def convertir_euros_a_pesos(euros):
    return euros * VALOR_DEL_EURO

def convertir_yenes_a_pesos(yenes):
    return yenes * VALOR_DEL_YEN

def convertidor_de_monedas(valor, moneda_origen, moneda_destino):
    if moneda_origen == "COP":
        if moneda_destino == "USD":
            return convertir_pesos_a_dolares(valor)
        if moneda_destino == "EUR":
            return convertir_pesos_a_euros(valor)
        if moneda_destino == "YEN":
            return convertir_pesos_a_yenes(valor)
    else:
        if moneda_origen == "USD":
            return convertir_dolares_a_pesos(valor)
        if moneda_origen == "EUR":
            return convertir_euros_a_pesos(valor)
        if moneda_origen == "YEN":
            return convertir_yenes_a_pesos(valor)

if __name__ == "__main__":
    print("¡Bienvenido al conversor de monedas!")
    print("Pesos colombianos = COP")
    print("Dólares = USD")
    print("Euros = EUR")
    print("Yenes = YEN")
    moneda_origen = input("¿Moneda origen? ")
    moneda_destino = input("¿Moneda destino? ")
    try:
        valor = float(input("¿Cantidad de monedas a convertir? "))
        resultado = convertidor_de_monedas(valor, moneda_origen, moneda_destino)
        print(f"Tienes {resultado:.2f} {moneda_destino}")
    except ValueError:
        print("Debes ingresar un valor numérico, no una cadena de texto. Intenta de nuevo.")