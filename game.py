# Función auxiliar que cuenta el número de ataques dado un tablero
# (o solución)
def countAttacks(board):
    attacks = 0
    value = 0
    for i in range(0, len(board)):
        value = 0
        for j in range(i + 1, len(board)):
            value += 1
            if(board[i] == board[j]):
                attacks += 1
            if(board[i] + value == board[j]):
                attacks += 1
            if(board[i] - value == board[j]):
                attacks += 1
    return attacks