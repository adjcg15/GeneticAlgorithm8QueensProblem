import matplotlib.pyplot as plt
import random
import heapq
import evolution
import game
import helpers

# Establecee el número máximo de evaluaciones para el algoritmo
MAXIMUM_ALLOWED_EVALUATIONS = 10000
# Crea la primera generación de la población
population = evolution.generateInitialPopulation()

# Variables para llevar control de las evaluaciones y la solución
solution = []
solutionFound = False
currentEvaluations = 0

# Crea una nueva gráfica para mostrar la convergencia del algoritmo
plt.figure()

# Mientras no haya sido encontrada una solución y el número de evaluaciones sea menor al máximo
# extablecido, se ejecuta el algoritmo
while(not solutionFound and currentEvaluations < MAXIMUM_ALLOWED_EVALUATIONS):
    # Establece el número de descendientes por generación
    DECENDENTS_PER_GENERATION = 10
    
    # Genera una lista de descendientes 
    decendents = []
    for _ in range(DECENDENTS_PER_GENERATION):
        # Selecciona a dos padres de la población
        parents = evolution.selectParents(population)
        father = parents[0]
        mother = parents[1]
        # Genera un descendiente a partir de esos padres
        descendant = evolution.generateDescendant(father, mother)

        # Aplica una mutación con 0.8 de probabilidad
        mutationProbability = random.random()
        if(mutationProbability <= 0.8):
            evolution.mutate(descendant)
        # Agrega el descendiente a la lista descendientes
        decendents.append(descendant)
    
    # Genera una lista de tuplas, en donde el primer elemento es el número de ataques negativo de la solución
    # y el segundo elemento la posición en la lista de la población de dicha solución
    qualitiesMapping = [(-game.countAttacks(solution), i) for i, solution in enumerate(population)]
    # Sustituye las peores soluciones de la población por los descendientes previamente generados
    for i in range(DECENDENTS_PER_GENERATION):
        _, index = heapq.heappop(qualitiesMapping)
        population[index] = decendents[i]

    # Obtiene la tupla con el menor número de ataques
    bestSolutionMapping = heapq.nlargest(1, qualitiesMapping)[0]
    # Determina cuál es el menor número de ataques de la población
    bestSolutionAttacksCounter = abs(bestSolutionMapping[0])
    # Determina en qué posición de la población se encuentra la solución con menor número de ataques
    bestSolutionIndex = bestSolutionMapping[1]

    # Agrega la mejor solución (su número de ataques) a la gráfica
    plt.scatter(currentEvaluations + 1, bestSolutionAttacksCounter, s=10, color="blue", linewidths=0)
    
    # En caso de que el número de ataques de la mejor solución de la población sea 0, es decir, el
    # programa ya encontró la solución al problema, se indica para parar el algoritmo y se guarda
    # la solución
    if(bestSolutionAttacksCounter == 0):
        solutionFound = True
        solution = population[bestSolutionIndex]
    
    currentEvaluations += 1

# Se imprime en consola el resultado del algoritmo
print("Se encontró la solución" if solutionFound else "NO se encontró la solución")
if(solutionFound):
    print("Total de evaluaciones: ", currentEvaluations)
    print("Solución: ")
    helpers.printBoard(solution)

# Se muestra la gráfica de convergencia
plt.xlabel("Generación")
plt.ylabel("Ataques en la mejor solución")
plt.title("Gráfica de convergencia")
plt.show()