import random
import helpers

# Función auxiliar que genera una población inicial de 100 soluciones
def generateInitialPopulation():
    population = []
    for _ in range(100):
        solution = [random.randint(0, 7) for _ in range(8)]
        random.shuffle(solution)
        population.append(solution)
    return population

# Función auxiliar que selecciona 2 padres de la población.
def selectParents(population):
    # Selecciona 5 soluciones de forma aleatoria
    selectedSolutions = helpers.selectSolutionsRandomly(population)
    # Después los ordena de la mejor a la peor
    sortedSolutions = helpers.sortSolutionsByAttacks(selectedSolutions)

    # Retorna la lista de las dos mejores soluciones
    parents = sortedSolutions[:2]
    return parents

# Función auxiliar que genera un descendiente a partir de dos padres
def generateDescendant(father, mother):
    descendant = []
    # Para cada gen del descendiente se hace lo siguiente
    for i in range(8):
        # Genera un número aleatorio menor a 1
        choiceFather = random.random() < 0.5
        # Si el número es mejor a 0.5, se toma el gen del padre,
        # caso contrario, se toma el gen de la madre en la posición
        # del gen que se está generando
        gene =  father[i] if choiceFather else mother[i]
        # Se agrega el gen al descendiente
        descendant.append(gene)

    return descendant

# Función auxiliar que muta una solución
def mutate(solution):
    # Se selecciona aleatoriamente la posición del gen a mutar
    positionToChange = random.randint(0, 7)
    # Se decide aleatoriamente si se moverá una casilla arrivba o
    # una hacia abajo
    movement = 1 if random.random() < 0.5 else -1
    # Se calcula la siguiente posición después de la mutación
    newGene = (solution[positionToChange] + movement) % 8
    # Se mueve la pieza a la nueva posición
    solution[positionToChange] = newGene
            