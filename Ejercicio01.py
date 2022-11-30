
def gas2price(lista_tuplas):
    """Función que muestra un saludo.
...
... Parámetros:
...     - lista_tuplas: Una lista con tuplas de 3 elementos.
... Salida:
...     Lista de precios a pagar por cada cliente.
... """
    listaPrecioCliente = []
    for precioMes in lista_tuplas:
        precioFinal = price(precioMes[0] , precioMes[1] , precioMes[2])
        listaPrecioCliente.append(precioFinal)
    return listaPrecioCliente;

def price(mes1:float,mes2:float,mes3:float):
    """Función que calcula el precio final.
...
... Parámetros:
...     - mes1: Una numero tipo float con el precio del primer mes.
...     - mes2: Una numero tipo float con el precio del segundo mes.
...     - mes3: Una numero tipo float con el precio del tercer mes.
... Salida:
...     Un número con el precio final de tipo float.
... """
    precio:float = (mes1 + mes2 + mes3) * 0.0615
    return precio;

lista_tuplas = [(400,300,100),(500,600,200) , (500,300,900)]
print(gas2price(lista_tuplas))
#help(gas2price)
#help(price)
