from numpy import exp
from src.algoritmos.greedy import greedy_mochila
from src.algoritmos.busqueda_local import busqueda_local
import time
import src.auxiliares.read_data as aux

def N(T):
    """Criterio de parada basado en el número de iteraciones que ha realizado el algoritmo."""
    T=123
    return T

def C(data):
    """Función de coste asociada al problema de la mochila."""
    return -sum(data)

def temple_simulado(sort_data,peso_tot,data):
    start = time.time()
    solucion = greedy_mochila(sort_data, data, peso_tot)
    solucion_start = solucion
    t = 12345
    u = 0
    while t > 0:
        n = 0
        print(n)
        while n <= N(t):
            print(n)
            solucion_bus, peso_busqueda_local = busqueda_local(sort_data, peso_tot)
            print(solucion_bus)
            print(solucion_start)
            delta = C(solucion_bus) - C(solucion_start)
            print(delta)
            if delta < 0:
                solucion_start = solucion_bus
                if C(solucion) < C(solucion_start):
                    solucion_start = solucion
            else:
                if u < exp(-delta/t):
                    solucion = solucion_bus
            n = n + 1
        t = t - 1
    end = time.time()
    print("Usando un algoritmo de tempe simulado con el critero de parada establecido."
          " \n" + " Solución: " + str(solucion) + "\n Número de elementos: "
          + str(n) + " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return solucion

path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file="00Uncorrelated/n00050/R01000/s001.kp"

peso_tot, num_obj, data = aux.read_data(path_data, file)
data, sort_data = aux.prop_data(num_obj, data)
solucion_temp = temple_simulado(sort_data, peso_tot, data)
print(f"Solucion_tempe: {solucion_temp}")
