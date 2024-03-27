import random
import helpers

def generateInitialPopulation():
    population = []
    for _ in range(100):
        solution = [random.randint(0, 7) for _ in range(8)]
        random.shuffle(solution)
        population.append(solution)
    return population

def selectParents(population):
    selectedSolutions = helpers.selectSolutionsRandomly(population)
    sortedSolutions = helpers.sortSolutionsByAttacks(selectedSolutions)

    parents = sortedSolutions[:2]
    return parents
    
def generateDescendant(father, mother):
    descendant = []
    for i in range(8):
        choiceFather = random.random() < 0.5
        gene =  father[i] if choiceFather else mother[i]
        descendant.append(gene)

    return descendant

def mutate(solution):
    positionToChange = random.randint(0, 7)
    newValue = random.randint(0, 7)
    solution[positionToChange] = newValue
            