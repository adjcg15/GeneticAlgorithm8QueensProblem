import random
import game

def selectSolutionsRandomly(population, numberOfSolutions = 5):
    return random.sample(population, min(numberOfSolutions, len(population)))

def sortSolutionsByAttacks(solutions):
    return sorted(solutions, key=game.countAttacks)

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