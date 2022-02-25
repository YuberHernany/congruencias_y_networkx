from functools import reduce
import numpy as np
import sympy.ntheory as nt
from sympy import igcd

def bin_vec(k):
    """ input: k is int.
        output: ndarray binary representation of k"""
    return [int(digit) for digit in np.binary_repr(k)]

def squares_mod(b, u, m):
    """ input: b int, base. m int, mod. u int, exponent
        output: ndarray sequence of squares mod m"""
    squares_mod_m = [b%m]
    u_bin_vec = bin_vec(u)
    for n in range(1, len(u_bin_vec)):
        squares_mod_m.append((squares_mod_m[-1] ** 2) % m)
    selected = [square for square, d in zip(squares_mod_m, u_bin_vec) if d == 1]
    return np.flip(np.array(selected))

def pow_mod(b, u, m):
    """ input: b int, base. m int, mod. u int, exponent
        output: int. result of b ** u (mod m)"""
    return reduce(lambda Ai, Aj: Ai * Aj, squares_mod(b, u, m)) % m

print(pow_mod(112, 7, 187))
