import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from sobreCesar import desencripta
from sobreCesar import letras_a_nums
# mensaje = """shzgth lth pjhzgylxapylugtajohgkpzjpwspuh""" opcional

mensaje = """jqncbowpfqbncubocvgocvkecubtgswkgtgpbowejcbowejcbfkuekrnkpc"""


respuesta = Counter(mensaje)
datos = pd.Series(respuesta)
datos_dict = dict(respuesta)

letra_mas_frecuente = [key for key, value in datos_dict.items() if value == np.max(datos)][0]

lista_letras = [letra for letra in "abcdefghijklmnopqrstuvwxyz "]
clave_para_descifrar = lista_letras.index(letra_mas_frecuente)
print("clave para descifrar: ", clave_para_descifrar)



datos.plot(kind='bar')
ax = plt.gca()
ax.set_title(f"Clave para descifrar: "+str(clave_para_descifrar))
plt.show()

print(desencripta(mensaje, clave_para_descifrar))
