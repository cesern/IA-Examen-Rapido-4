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
    #para calcular los promedios regrese mas valores
    return solucion, t_final - t_inicial, algo_genetico.problema.costo(solucion)

def probarVarios():
    tiempoPromedio=0                     
    repeticiones=10
    nreinas=16
    prob_mutacion=[.05]
    npob=100
    gen=150
    for prob in prob_mutacion:
        tiempoPromedio=0
        costo=0
        for _ in range(repeticiones):
            aux1,aux2=probar(nreinas,npob,gen,prob)
            tiempoPromedio+=aux1
            costo+=aux2
        print("\nTiempo Promedio = ",tiempoPromedio/repeticiones)
        print("\nCosto Promedio = ",costo/repeticiones)
    
def probar(nreinas,n_poblacion,generaciones,prob_mutacion):
    """
        Funcion que prueba el algoritmo
        recibe lod parametros a variar 
    """
    alg_gen = genetico.GeneticoPermutaciones(ProblemaNreinas(nreinas),
                                                n_poblacion, prob_mutacion)

    solucion, tiempo, costo = prueba_genetico(alg_gen, generaciones, True)    
    return tiempo, costo

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
    #   Todos los problemas los corri 100 repeticiones y calculando promedios y viendo el max y min
    #   Quizas los tiempos tan elevados se deban a mi computadora porque en el salon de clases los tiempos no eran tan elevados
    #   y el de 100 reinas en mi laptop es demasiado el tiempo
    #
    #               Pob   Gen    Prob   TiempoPromedio CostoPromedio MenorCosto MayorCosto
    #    8  REINAS:  50    50      .1           0.2420             0          0          0
    #   16  REINAS: 100   150     .05           2.7952             0          0          0
    #   32  REINAS: 145   300    .006          15.4775          0.02          0          1
    #   64  REINAS: 170   400    .005          95.1227          0.02          0          1
    #  100  REINAS: 150   500    .004         239.5438           0.4          0          2    
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun
    #       tu experiencia?
    #   Conforme van creciendo las reinas aumentar la poblacion (solo un poco) y generaciones. La probabilidad
    #   reducirla un poco. Al aumentar la poblacion y las generaciones el tiempo aumenta bastante  
    #
    #    PAra el de 10 reinas : (Poblacion:150 generaciones:500 probabilidad:.004
    #                           ,no modifique metodos,239.5438 ,no modifique metodos pero tarde demasiado corriendo el programa para 
    #                           encontrar los valores)
    probarVarios()
