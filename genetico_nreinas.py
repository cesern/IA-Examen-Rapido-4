#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prueba de los algoritmos genéticos utilizando el problema
de las n-reinas para aprender a ajustarlos y probarlos.

"""

from time import time
from itertools import combinations
from random import shuffle
import genetico

__author__ = 'Cesar Salazar'


class ProblemaNreinas(genetico.Problema):
    """
    Las N reinas para AG

    """
    def __init__(self, n=8):
        self.n = n

    def estado_aleatorio(self):
        estado = list(range(self.n))
        shuffle(estado)
        return tuple(estado)

    def costo(self, estado):
        """
        Calcula el costo de un estado por el número de conflictos entre reinas

        @param estado: Una tupla que describe un estado

        @return: Un valor numérico, mientras más pequeño, mejor es el estado.

        """
        return sum([1 for (i, j) in combinations(range(self.n), 2)
                    if abs(estado[i] - estado[j]) == abs(i - j)])


def prueba_genetico(algo_genetico, n_generaciones, verbose=False):
    """
    Prueba de los algoritmos genéticos con el problema de las n reinas
    desarrollado para búsquedas locales (tarea 2).

    @param algo_genetico: objeto de la clase genetico.Genetico
    @param n_generaciones: Generaciones (iteraciones) del algortimo
    @param verbose: True si quieres desplegar informacion básica
    @return: Un estado con la solucion (una permutacion de range(n)

    """
    t_inicial = time()
    solucion = algo_genetico.busqueda(n_generaciones)
    t_final = time()
    if verbose:
        print ('Pob:{0:3d} Gen:{1:3d} Prob:{3:5f} Costo:{2:3d}  Tiempo:===>{4:5f}'.format(algo_genetico.n_poblacion,n_generaciones,
                 algo_genetico.problema.costo(solucion),algo_genetico.prob_muta,t_final - t_inicial))
        #print("\nUtilizando el AG: {}".format(algo_genetico.nombre))
        #print("Con poblacion de dimensión {}".format(
        #    algo_genetico.n_poblacion))
        #print("Con {} generaciones".format(n_generaciones))
        #print("Costo de la solución encontrada: {}".format(
        #    algo_genetico.problema.costo(solucion)))
        #print("Tiempo de ejecución en segundos: {}".format(
        #    t_final - t_inicial))
    return solucion

def probarVarios():
    nreinas=100
    n_poblacion=50
    generaciones=200
    #prob_mutacion=[.5,0.1,0.05,.005,.0005,.0005,.00005]
    for i in range(50):
        probar(nreinas,n_poblacion,generaciones,.001)

def probar(nreinas,n_poblacion,generaciones,prob_mutacion):
    alg_gen = genetico.GeneticoPermutaciones(ProblemaNreinas(nreinas),
                                                n_poblacion, prob_mutacion)

    solucion = prueba_genetico(alg_gen, generaciones, True)    

if __name__ == "__main__":

    # Modifica los parámetro del algoritmo genetico que propuso el
    # profesor (el cual se conoce como genetico.GeneticoPermutaciones)
    # buscando que el algoritmo encuentre SIEMPRE una solución óptima,
    # utilizando el menor tiempo posible en promedio. Realiza esto
    # para las 8, 16, 32, 64 y 100 reinas.
    #
    # Lo que puedes modificar es el tamaño de la población, el número
    # de generaciones y/o la probabilidad de mutación.
    #
    # Recuerda que podrias automatizar el problema haciendo una
    # función que genere una tabla con las soluciones, o hazlo a mano
    # si eso ayuda a comprender mejor el algoritmo.
    #
    #   -- ¿Cuales son en cada caso los mejores valores?  (escribelos
    #       abajo de esta linea)
    #
    #               Población   Generaciones    Probabilidad    Tiempo
    #    8  REINAS:        64             50             .5         .4
    #   16  REINAS:       128            200            .05         .5
    #   32  REINAS:
    #   64  REINAS
    #  100  REINAS    
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun
    #       tu experiencia?
    #   ¿¿¿¿¿Conforme van creciendo las reinas aumentar la poblacion? y generaciones?. La probabilidad
    #   reducirla?????   
    #
    #(parametros,metodos,tiempo,tiempo del ajuste)
    probarVarios()
