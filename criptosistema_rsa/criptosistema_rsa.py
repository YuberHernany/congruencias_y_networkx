import numpy as np
import sympy.ntheory as nt

letras = "abcdefghijklmnñopqrstuvwxyz ".upper()
lista_letras = [letra for letra in letras]
lista_nums = [num for num in range(11, 38)] + [99]
letras_a_num = {letra:num for letra, num in zip(lista_letras, lista_nums)}

# I. Elegir dos números primos grandes
# II. Calcular el producto m=pq, como módulo
# III. Se calcula phi(m) = phi(p) phi(q) = (p-1)(q-1)
# IV. Se escoge un exponente entero e, coprimo con phi(m)

# Públicos m y e. Secretos p, q y phi(m).

# Encriptar usa m y e.
# 1) Convierte mensaje en dígitos
# 2) Separar la secuencia de dígitos en grupos de números
# a_1, ..., a_r (con a_i < m) y ningun a_i comenzando con dígito cero.
# 3) Calcular b_i := a_i ** e (mod m). Mensaje encriptado b_1, b_2, ... b_r

# Desencriptar usa p y q. Es decir m=pq y phi(m)=(p-1)(q-1)
# 1) Halle u tal que eu \quiv 1 (mod phi(m))
# 2) Calcular x_i := b_i ** u (mod m). Mensaje desencriptado x_1, x_2, ... x_r

# Evidentemente se necesita un buen algoritmo de cálculo de potencias
