"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem
from random import choice
from time import time


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val == max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    # COMPLETAR


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    def criterio_parada():
        pass

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con busqueda tabu.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        tabu = []

        while not self.criterio_parada():
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            #Filtro las acciones no tabu
            no_tabues = {act : val for act, val in diff.items() if act not in tabu}

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in no_tabues.items() if val == max(no_tabues.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            #Almacenamos el sucesor de aplicar la accion elegida
            sucesor = problem.result(actual, act)

            #Almacenamos el valor objetivo del sucesor
            sucesor_value = problem.obj_val(sucesor)

            #Si el valor objetivo del sucesor es mejor que el mejor valor objetivo actual,
            #actualizamos el mejor objetivo actual con el mismo 
            if sucesor_value > value:
                value = sucesor_value

            #Nos movemos al sucesor
            actual = sucesor
            value = value + diff[act]
            self.niters += 1

        #Retornamos la mejor solucion encontrada o #Retornamos si se cumple el criterio de parada
        self.tour = actual
        self.value = value
        end = time()
        self.time = end-start
        return

#Notas: lo que faltaria
#Implementacion de lista tabu voy a usar el criterio 1 de teria
    #1)Limitar la capacidad de la lista tabu

#Preguntar si prefieren otro

#Para el criterio de parada voy a combinar los criterios 2 y 3 de teoria
    #2)Numero de iteraciones sin mejoras
    #3)Valor de umbral