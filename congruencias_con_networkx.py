import numpy as np
import networkx as nx
import sympy.ntheory as nt
import matplotlib.pyplot as plt
from sympy import igcd, ilcm
plt.style.use("dark_background")

def star_Z_m(m):
    """ m: int, modulo"""
    G = nx.Graph()
    centro = ' . '
    G.add_node(centro)
    for k in range(m):
        G.add_edge(k, centro)
    for k in range(m, 2 * m):
        G.add_edge(k, k%m)
    for j in range(2, 7):
        for k in range(m * j, m * (j+1)):
            G.add_edge(k, k%m + (j-1) * m)
    return G


def suma_clases(a, b, m):
    """ m: int, modulo
        a: int, sumando. a: int, sumando"""
    G = star_Z_m(m)
    color_map = {}
    for node in G:
        color_map[node] = 'gray'
    for node in G:
        if node in [a, b]:
            color_map[node] = "green"
    for node in G:
        if node in [a+b, (a+b)%m]:
            color_map[node] = 'yellow'
    nx.draw(G, node_color=color_map.values(), with_labels=True)



def multiplica_clases(a, b, m):
    """ m: int, modulo
        a: int, sumando. a: int, sumando"""
    G = star_Z_m(m)
    color_map = {}
    for node in G:
        color_map[node] = 'gray'
    for node in G:
        if node in [a, b]:
            color_map[node] = "green"
    for node in G:
        if node in [a*b, (a*b)%m]:
            color_map[node] = 'yellow'
    nx.draw(G, node_color=color_map.values(), with_labels=True)


def unidades(m):
    """ m: int, modulo"""
    G = star_Z_m(m)
    color_map = {' . ':"gray"}
    for node in G:
        if node != ' . ': # nodo que no representa un numero
            color_map[node] = 'gray'
    for node in G:
        if (node != ' . ') and (igcd(node, m) == 1):
            color_map[node] = 'yellow'
    nx.draw(G, node_color=color_map.values(), with_labels=True)

def divisores_de_cero(m):
    """ m: int, modulo"""
    G = star_Z_m(m)
    color_map = {' . ':"gray"}
    for node in G:
        color_map[node] = "gray"
    divisor = nt.divisors(m)[1]
    color_map[divisor] = "yellow"
    color_map[m // divisor] = "yellow"

    nx.draw(G, node_color=color_map.values(), with_labels=True)

# multiplica_clases(17,7,8)
# multiplica_clases(7, 8, 17)

# unidades(101)
# divisores_de_cero(16)

plt.show()
