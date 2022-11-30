

def phone_call(numero_completo):
    """Función que comprueba el número de teléfono
...
... Parámetros:
...     - numero_completo: Una cadena con el número de teléfono completo.
... Salida:
...     Una cadena con dos opciones: Si el número es correcto o el número es incorrecto.
... """

    numeroSeparado = numero_completo.split("-")
    prefijo = numeroSeparado[0]
    numeroTelefono = numeroSeparado[1]
    esCorrecto = check_phone_number(numeroTelefono)
    mostrarPais = check_phone_country(prefijo)

    if esCorrecto == True and mostrarPais != "":
        print("Llamando a",str(numeroTelefono) , str(mostrarPais))
    else:
        print("Teléfono incorrecto o código de país no encontrado")
    return;

def check_phone_number(numTelefono:str):
    """Función que comprueba si el número es correcto
...
... Parámetros:
...     - numTelefono: Un string con el número de teléfono.
... Salida:
...     Un booleano con valor True si es correcto o False si es incorrecto.
... """
    esCorrecto = False;
    if len(numTelefono) == 9 and numTelefono[0] == "6":
        esCorrecto = True
    else:
        esCorrecto = False
    return esCorrecto;

def check_phone_country(prefijoTelefono: str):
    """Función que muestra el nombre del pais a través de un prefijo
...
... Parámetros:
...     - prefijoTelefono: Un string con el prefijo del número de teléfono.
... Salida:
...     Un string con el nombre del pais asociado.
... """
    pais = ""

    for diccPrefijo,diccPais in diccPrefijos.items():
        if diccPrefijo == prefijoTelefono:
            pais = diccPais
    return pais;

diccPrefijos = {"+30":"Grecia" , "+33":"Francia" , "+34":"España" , "+351":"Portugal" , "+380":"Ucrania" , "+39":"Italia" , "+41":"Suiza" , "+44":"Reino Unido" , "+49":"Alemania" , "+7":"Rusia"}

print(phone_call("+34-611641851"))
#help(phone_call)
#help(check_phone_number)
#help(check_phone_country)
