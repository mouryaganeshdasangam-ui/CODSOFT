import random
import time
import math

COMPUTER = 1
HUMAN = 2
SIDE = 3
COMPUTERMOVE = 'O'
HUMANMOVE = 'X'


def initialise():
    board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
    return board


def showBoard(board):
    print("\n\n")
    print("\t\t\t {} | {} | {} ".format(board[0][0], board[0][1], board[0][2]))
    print("\t\t\t--------------")
    print("\t\t\t {} | {} | {} ".format(board[1][0], board[1][1], board[1][2]))
    print("\t\t\t--------------")
    print("\t\t\t {} | {} | {} ".format(board[2][0], board[2][1], board[2][2]))
    print("\n")


def showInstructions():
    print("\t\t\t Tic-Tac-Toe\n\n")
    print("Choose a cell numbered from 1 to 9 as below and play\n\n")
    print("\t\t\t 1 | 2 | 3 ")
    print("\t\t\t-------------")
    print("\t\t\t 4 | 5 | 6 ")
    print("\t\t\t-------------")
    print("\t\t\t 7 | 8 | 9 ")
    print("\n")
    print("==========================================\n\n")


def declareWinner(whoseTurn):
    if whoseTurn == COMPUTER:
        print("COMPUTER has won")
    else:
        print("HUMAN has won")


def rowCrossed(board):
    for i in range(SIDE):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' ':
            return True
    return False


def columnCrossed(board):
    for i in range(SIDE):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
            return True
    return False


def diagonalCrossed(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False


def gameOver(board):
    return rowCrossed(board) or columnCrossed(board) or diagonalCrossed(board)


def getAvailableMoves(board):
    """Returns a list of available (row, col) positions on the board."""
    moves = []
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves


def checkWinner(board, player):
    """Checks if the given player ('X' or 'O') has won."""
    # Check rows
    for i in range(SIDE):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # Check columns
    for i in range(SIDE):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def isBoardFull(board):
    """Returns True if no empty cells remain on the board."""
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == ' ':
                return False
    return True


def minimax(board, depth, isMaximizing):
    """
    Minimax algorithm to evaluate board states.

    Scoring:
        HUMAN (X) wins   -> +10 - depth  (maximizer)
        COMPUTER (O) wins -> -10 + depth  (minimizer)
        Draw             ->  0

    The depth parameter makes the AI prefer faster wins and slower losses.
    """
    # Terminal state checks
    if checkWinner(board, HUMANMOVE):
        return 10 - depth
    if checkWinner(board, COMPUTERMOVE):
        return -10 + depth
    if isBoardFull(board):
        return 0

    if isMaximizing:
        # Human's perspective — maximize the score
        best = -math.inf
        for (r, c) in getAvailableMoves(board):
            board[r][c] = HUMANMOVE
            score = minimax(board, depth + 1, False)
            board[r][c] = ' '
            best = max(best, score)
        return best
    else:
        # Computer's perspective — minimize the score
        best = math.inf
        for (r, c) in getAvailableMoves(board):
            board[r][c] = COMPUTERMOVE
            score = minimax(board, depth + 1, True)
            board[r][c] = ' '
            best = min(best, score)
        return best


def findBestMove(board):
    """
    Calls minimax for each available move and returns the best (row, col)
    for the COMPUTER (minimizer). Picks the move with the lowest score.
    """
    bestScore = math.inf
    bestMove = (-1, -1)

    for (r, c) in getAvailableMoves(board):
        board[r][c] = COMPUTERMOVE
        score = minimax(board, 0, True)  # Next turn is Human (maximizer)
        board[r][c] = ' '

        if score < bestScore:
            bestScore = score
            bestMove = (r, c)

    return bestMove


def getHumanMove(board):
    """Prompts, validates, and returns the human's chosen (row, col)."""
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input! Please enter a number between 1 and 9.\n")
                continue
            row = (move - 1) // SIDE
            col = (move - 1) % SIDE
            if board[row][col] != ' ':
                print("That cell is already taken! Choose another.\n")
                continue
            return row, col
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.\n")


def playTicTacToe(whoseTurn):
    board = initialise()
    showInstructions()
    moveCount = 0

    while not gameOver(board) and moveCount != SIDE * SIDE:
        if whoseTurn == COMPUTER:
            print("COMPUTER is thinking...")
            time.sleep(1)
            row, col = findBestMove(board)
            board[row][col] = COMPUTERMOVE
            cellNumber = row * SIDE + col + 1
            print("COMPUTER has put a {} in cell {}".format(COMPUTERMOVE, cellNumber))
            showBoard(board)
            moveCount += 1
            whoseTurn = HUMAN

        elif whoseTurn == HUMAN:
            row, col = getHumanMove(board)
            board[row][col] = HUMANMOVE
            cellNumber = row * SIDE + col + 1
            print("HUMAN has put a {} in cell {}".format(HUMANMOVE, cellNumber))
            showBoard(board)
            moveCount += 1
            whoseTurn = COMPUTER

    if not gameOver(board) and moveCount == SIDE * SIDE:
        print("Draw Match")
    else:
        # The last player who moved caused the win, so switch back
        if whoseTurn == COMPUTER:
            whoseTurn = HUMAN
        elif whoseTurn == HUMAN:
            whoseTurn = COMPUTER
        declareWinner(whoseTurn)


if __name__ == "__main__":
    playTicTacToe(COMPUTER)
