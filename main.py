
numVecees = {}

def ocurrencia():
    archivo = open('The Prisoner of Azkaban.txt', encoding='utf8')
    linea = archivo.readline()
    while linea:
        arreglo = []
        arreglo = linea.split()
        for w in arreglo:
            if w in numVecees:
                numVecees[w] += 1
            else:
                numVecees[w] = 1
        linea = archivo.readline()

    for palabras in numVecees:
        print('[{},{}]'.format(palabras, numVecees[palabras]))

    archivo.close()

ocurrencia()