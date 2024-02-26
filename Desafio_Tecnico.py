def singular(palabra):
  palabra = palabra.lower()
  vocales = ["a", "e", "i", "o", "u"]
  ultima = palabra[len(palabra) - 1]
  # CASO 1
  for vocal in vocales:
    if ultima == vocal:
      return (palabra + "s")
  # CASO 2
  if ultima == "x" or ultima == "s":
    return (palabra)
  # CASO 3
  if ultima == "z":
    palabra = palabra.replace("z", "ces")
    return (palabra)
  # CASO 4
  else:
    return (palabra + "es")

palabra = "paréntesis"

nuevaPalabra = singular(palabra)
print (nuevaPalabra)