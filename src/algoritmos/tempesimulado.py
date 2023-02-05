import numpy as np
from src.algoritmos.greedy import greedy_mochila
from src.algoritmos.busqueda_local import busqueda_local
import time

def N(T):
    """Criterio de parada basado en el número de iteraciones que ha realizado el algoritmo."""
    T=123
    return T

def C(data):
    """Función de coste asociada al problema de la mochila."""
    return sum(data)

def temple_simulado(sort_data,peso_tot,data):
    start = time.time()
    solucion = greedy_mochila(sort_data, peso_tot, data, False)
    solucion_start = solucion
    t = 12345
    while t > 0:
        n = 0
        while n <= N(t):
            solucion_bus, peso_busqueda_local = busqueda_local(sort_data, peso_tot, False)
            delta = C(solucion_bus) - C(solucion_start)
            if delta < 0:
                solucion_start = solucion_bus
                if C(solucion) < C(solucion_start):
                    solucion_start = solucion
            else:
                u = np.random.uniform(0,1)
                if u < np.exp(-delta/t):
                    solucion = solucion_bus
            n = n + 1
        t = t - 1
    end = time.time()
    print("Usando un algoritmo de tempe simulado con el critero de parada establecido."
          " \n" + " Solución: " + str(solucion) + "\n Número de elementos: "
          + str(n) + " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return solucion

