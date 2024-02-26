def singular(palabra):
    palabra = palabra.lower()
    vocales = ["a", "e", "i", "o", "u"]
    ultima = palabra[len(palabra) - 1]
    # CASO 1
    for vocal in vocales:
        if ultima == vocal:
            return (1, palabra + "s")
    # CASO 2
    if ultima == "x" or ultima == "s":
        return (2, palabra)
    # CASO 3
    if ultima == "z":
        palabra = palabra.replace("z", "ces")
        return (3, palabra)
    # CASO 4
    else:
        return (4, palabra + "es")

def pluralizador(lasPalabras):
    cantidadesPorRegla = [0, 0, 0, 0]
    nuevasPalabras = []
    
    # Recorremos las Palbras ingresadas
    for laPalabra in lasPalabras:
        regla, nuevaPalabra = singular(laPalabra)
        nuevasPalabras.append(nuevaPalabra)
        cantidadesPorRegla[regla - 1] += 1
      
    print (nuevasPalabras)
    print (cantidadesPorRegla)
    
palabras = ["CASA", "Perro", "limon"]
print (palabras)
pluralizador(palabras)