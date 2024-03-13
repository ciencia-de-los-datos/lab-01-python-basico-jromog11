"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    with open("data.csv", "r") as archivo:
        lineas = archivo.readlines()

    numeros = list()

    for linea in lineas:
        segunda_col = linea.split()
        numeros.append(int(segunda_col[1]))

    suma = sum(numeros)

    return suma


def pregunta_02():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

    secuencia = list()

    for line in contenido:
        element = line.split()
        secuencia.append((element[0], 1))

    diccionario = dict()

    for k, v in secuencia:
        if k not in diccionario:
            diccionario[k] = []
        diccionario[k].append(v)

    conteo = list()

    for k, v in diccionario.items():
        conteo.append((k, sum(v)))

    lista_ordenada = sorted(conteo, key=lambda x: x[0])

    return lista_ordenada


def pregunta_03():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

    secuencia = list()
    for line in contenido:
        columna = line.split()
        secuencia.append((columna[0], int(columna[1])))

    diccionario = dict()

    for k, v in secuencia:
        if k not in diccionario:
            diccionario[k] = []
        diccionario[k].append(v)

    resultado = list()

    for k, v in diccionario.items():
        resultado.append((k, sum(v)))

    lista_ordenada = sorted(resultado, key=lambda x: x[0])

    return lista_ordenada


def pregunta_04():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

    fecha = list()

    for line in contenido:
        linea = line.split()
        fecha.append(linea[2])

    meses = list()

    for dato in fecha:
        mes = dato.split("-")
        meses.append((mes[1], 1))

    conteo = dict()

    for k, v in meses:
        if k not in conteo:
            conteo[k] = []
        conteo[k].append(v)

    final = list()

    for k, v in conteo.items():
        final.append((k, sum(v)))

    listaOrdenada = sorted(final, key=lambda x: x[0])

    return listaOrdenada


def pregunta_05():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

        secuencia = list()

        for line in contenido:
            linea = line.split()
            secuencia.append((linea[0], int(linea[1])))

        letra_numeros = dict()

        for k, v in secuencia:
            if k not in letra_numeros:
                letra_numeros[k] = []
            letra_numeros[k].append(v)

        conteo = list()

        for k, v in letra_numeros.items():
            conteo.append((k, max(v), min(v)))

        conteo = sorted(conteo, key=lambda x: x[0])

        return conteo


def pregunta_06():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

    secuencia = list()

    for line in contenido:
        linea = line.split()[4]
        secuencia.append(linea)  # Aqui tengo todo el renglon

    listas_anidadas = list()

    for l in secuencia:
        ls = l.split(",")
        listas_anidadas.append(ls)

    lista_combinada = list()

    for sublist in listas_anidadas:
        for element in sublist:
            lista_combinada.append(element)

    lista_final = list()

    for e in lista_combinada:
        f = e.split(":")
        lista_final.append((f[0], int(f[1])))

    diccionario = dict()

    for k, v in lista_final:
        if k not in diccionario:
            diccionario[k] = []
        diccionario[k].append(v)

    conteo = list()

    for k, v in diccionario.items():
        conteo.append((k, min(v), max(v)))
    conteo = sorted(conteo, key=lambda x: x[0])

    return conteo


def pregunta_07():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

    secuencia = list()

    for line in contenido:
        linea = line.split()
        secuencia.append((int(linea[1]), linea[0]))

    diccionario = dict()

    for k, v in secuencia:
        if k not in diccionario:
            diccionario[k] = []
        diccionario[k].append(v)

    conteo = list()

    for k, v in diccionario.items():
        conteo.append((k, v))

    conteo = sorted(conteo, key=lambda x: x[0])

    return conteo


def pregunta_08():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

    secuencia = list()

    for line in contenido:
        linea = line.split()
        secuencia.append((int(linea[1]), linea[0]))

    diccionario = dict()

    for k, v in secuencia:
        if k not in diccionario:
            diccionario[k] = []
        if v not in diccionario[k]:
            diccionario[k].append(v)

    conteo = list()

    for k, v in diccionario.items():
        conteo.append((k, sorted(v, key=lambda x:x[0])))
    conteo = sorted(conteo, key=lambda x:x[0])
    
    return conteo


def pregunta_09():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()
    
    secuencia = list()

    for line in contenido:
        linea = line.split()[4]
        secuencia.append(linea)

    letras = list()

    for dato in secuencia:
        letra = dato.split(",")
        for par in letra:
            solo_letras = par.split(":")[0]
            letras.append((solo_letras, 1))
    
    diccionario = dict()

    for k,v in letras:
        if k not in diccionario:
            diccionario[k] = []
        diccionario[k].append(v)
    
    conteo_final = dict()

    for k,v in diccionario.items():
        conteo_final[k] = sum(v)
    
    valores_ord = dict(sorted(conteo_final.items()))

    return valores_ord


def pregunta_10():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()
    
    col1 = list()
    col4 = list ()
    col5 = list()

    for line in contenido:
        linea = line.split()
        col1.append(linea[0])
        col4.append(linea[3])
        col5.append(linea[4])
    
    items_col5 = list()

    for sublist in col5:
        item = sublist.split(",")
        items_col5.append(len(item))

    items_col4 = list()

    for dato in col4:
        dato_individual = dato.split(",")
        items_col4.append(len(dato_individual))
    
    lista_final = zip(col1, items_col4, items_col5)

    resultado = list()
    for item in lista_final:
        resultado.append(item)

    return resultado


def pregunta_11():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()
    
    secuencia = list()

    for line in contenido:
        linea = line.split()
        letras = linea[3].split(",")
        for dato in letras:
            secuencia.append((dato, linea[1]))
    
    diccionario = dict()

    for k,v in secuencia:
        if k not in diccionario:
            diccionario[k] = []
        diccionario[k].append(int(v))
    
    resultado = dict()

    for k,v in diccionario.items():
        resultado[k] = sum(v)
    
    valores_ord = dict(sorted(resultado.items()))

    return valores_ord


def pregunta_12():
    with open("data.csv", "r") as archivo:
        contenido = archivo.readlines()

    secuencia = list()

    for line in contenido:
        line = line.split()
        letra = line[0]
        letras_numero = line[4].split(",")
        for item in letras_numero:
            numero = int(item.split(":")[1])
            secuencia.append((letra, numero))

    diccionario = dict()

    for k,v in secuencia:
        if k not in diccionario:
            diccionario[k] = []
        diccionario[k].append(v)
    
    conteo = dict()

    for k,v in diccionario.items():
        conteo[k] = sum(v)
    
    resultado = dict(sorted(conteo.items()))

    return resultado