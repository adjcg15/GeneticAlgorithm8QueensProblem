import matplotlib.pyplot as plt
import random
import heapq
import evolution
import game
import helpers

MAXIMUM_ALLOWED_EVALUATIONS = 10000
population = evolution.generateInitialPopulation()

solution = []
solutionFound = False
currentEvaluations = 0

plt.figure()

while(not solutionFound and currentEvaluations < MAXIMUM_ALLOWED_EVALUATIONS):
    DECENDENTS_PER_GENERATION = 10
    
    decendents = []
    for _ in range(DECENDENTS_PER_GENERATION):
        parents = evolution.selectParents(population)
        father = parents[0]
        mother = parents[1]
        descendant = evolution.generateDescendant(father, mother)

        mutationProbability = random.random()
        if(mutationProbability <= 0.8):
            evolution.mutate(descendant)
        decendents.append(descendant)
    
    qualitiesMapping = [(-game.countAttacks(solution), i) for i, solution in enumerate(population)]
    for i in range(10):
        _, index = heapq.heappop(qualitiesMapping)
        population[index] = decendents[i]

    bestSolutionMapping = heapq.nlargest(1, qualitiesMapping)[0]
    bestSolutionAttacksCounter = abs(bestSolutionMapping[0])
    bestSolutionIndex = bestSolutionMapping[1]

    plt.scatter(currentEvaluations + 1, bestSolutionAttacksCounter, s=10, color="blue", linewidths=0)
    
    if(bestSolutionAttacksCounter == 0):
        solutionFound = True
        solution = population[bestSolutionIndex]
    
    currentEvaluations += 1

print("Se encontró la solución" if solutionFound else "NO se encontró la solución")
if(solutionFound):
    print("Total de evaluaciones: ", currentEvaluations)
    print("Solución: ")
    helpers.printBoard(solution)

plt.xlabel("Generación")
plt.ylabel("Ataques en la mejor solución")
plt.title("Gráfica de convergencia")
plt.show()