# Metodo de cifrado de Cesar

# Construya una función en python que reciba un string indicando un mensaje y que
# practique una traslación cíclica de cada letra un determinado múmero de posiciones, usando el
# siguiente diccionario.
#
# {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,
# "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16,
# "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25, " ":26}
#
# Por ejemplo, si se decide trasladar cada letra del mensaje "abandonar la operacion" una sola posición, se tendrá:
#
# "abandonar la operacion"  ENCRIPTADO COMO:  "bcboepobsambapqfsbdjpo"
#
# Note que se practica la traslación "a"---->"b", "b"---->"c", "a"---->"b", "n"---->"o", "d"---->"e", "o"---->"p",
# "n"---->"o", "a"---->"b", "r"---->"s", " "---->"a", etc, de modo que: "abandonar l..."---->"bcboepobsam..."
#
# Procure además construir otra función que se encargue de desencriptar mensajes, dada la clave con la que se
# encriptó el mensaje, es decir, dado el número de veces que se trasladó cada letra al momento de encriptar.


letras_a_nums = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,
                 "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16,
                 "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25, " ":26}

N = len(letras_a_nums)
nums_a_letras = {valor:clave for clave, valor in letras_a_nums.items()}

def de_palabras_a_nums(palabras):
    """palabras: string"""
    return [letras_a_nums[letra] for letra in palabras]

def de_numeros_a_palabras(numeros):
    """numeros: list"""
    return [nums_a_letras[num] for num in numeros]

def cifra_num(num, clave):
    return (num + clave) % N

def descifra_num(num, clave):
    return (num + N - clave) % N

def cifra(lista_nums, clave):
    return [cifra_num(num, clave) for num in lista_nums]

def descifra(lista_nums, clave):
    return [descifra_num(num, clave) for num in lista_nums]

def encripta(mensaje, clave):
    mensaje_numerico = de_palabras_a_nums(mensaje)
    mensaje_cifrado = cifra(mensaje_numerico, clave)
    cifrado_letras = de_numeros_a_palabras(mensaje_cifrado)
    separador = ""
    return separador.join(cifrado_letras)

def desencripta(mensaje, clave):
    mensaje_numerico = de_palabras_a_nums(mensaje)
    mensaje_descifrado = descifra(mensaje_numerico, clave)
    descifrado_letras = de_numeros_a_palabras(mensaje_descifrado)
    separador = ""
    return separador.join(descifrado_letras)


if __name__ =="__main__":
    # clave = 1
    clave = int(input("Dame como clave un número entre 1 y 28: "))

    # mensaje = "abandonar la operacion" # "ha muerto el rey", "es momento de atacar"
    mensaje = input("Escriba en minúscula el mensaje que desea encriptar: ")

    encriptado = encripta(mensaje, clave)


    print(mensaje, " ENCRIPTADO COMO: ", encriptado)
    print("")
    print(encriptado, " DESENCRIPTADO COMO: ", desencripta(encriptado, clave))
