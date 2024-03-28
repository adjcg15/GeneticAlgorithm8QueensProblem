import random
import game

# Función auxiliar que toma una muestra de la población total
# de "numberOfSolutions" elementos
def selectSolutionsRandomly(population, numberOfSolutions = 5):
    return random.sample(population, min(numberOfSolutions, len(population)))

# Función auxiliar que ordena una lista de soluciones de
# acuerdo con su número de ataques: de menor a mayor
def sortSolutionsByAttacks(solutions):
    return sorted(solutions, key=game.countAttacks)

# Función auxiliar que toma la representación de una solución
# e imprime el tablero en consola
def printBoard(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[col] == row:
                line += "Q".center(3)
            else:
                line += "-".center(3)
        print(line)
    print("\n")