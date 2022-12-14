########### Funcion para sumar #################

#Se recibira una cantidad de parametros indefinidos con *args
def sumar_valores(*args):
    #pass es palabra reservada para agregar solo funcion y no el detalle.
    #esto es util si se quiere seguir escribiendo sin que el codigo genere error.
    #pass
    resultado = 0
    #iterar cada elemento:
    #donde, resultado + valor
    for valor in args:
        resultado += valor

    return resultado


#llamada a funcion
print(sumar_valores(3,5,9,2))

########### Funcion para multiplicar #################
def multiplica_valores(*args):
    resultado = 1
    for valor in args:
        resultado *= valor

    return resultado

print(multiplica_valores(5,5))

########### Funcion para trabajar con diccionarios #################
#kwargs = keywords arguments // En este caso se utilizaran diccionarios
def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE = 'Integrated Development Environment', PK = 'Primary Key')


########### Funcion para trabajar con arrays #################

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['John','Jenny','Diana','Isabel']
desplegarNombres(nombres)

#para pasar valores diferentes como numeros, sera necesario parasarlos como tupla
desplegarNombres((10,11))


########### Funcion RECURSIVA - FACTORIAL #################

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

resultado = factorial(5)
print(f'El factorial de 5 es: {resultado}')


