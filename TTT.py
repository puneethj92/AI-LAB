# Tic-Tac-Toe using Minimax Algorithm

HUMAN = 'X'
COMPUTER = 'O'


def print_board(board):
    print()
    for i in range(3):
        print(" " + " | ".join(board[i]))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] \
                and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] \
            and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] \
            and board[0][2] != ' ':
        return board[0][2]

    return None


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def minimax(board, maximizing):
    winner = check_winner(board)

    # Terminal states
    if winner == COMPUTER:
        return 1

    if winner == HUMAN:
        return -1

    if is_board_full(board):
        return 0

    if maximizing:
        # COMPUTER tries to maximize the score
        best_score = -float('inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = COMPUTER

                    score = minimax(board, False)

                    board[i][j] = ' '

                    best_score = max(best_score, score)

        return best_score

    else:
        # HUMAN tries to minimize the score
        best_score = float('inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = HUMAN

                    score = minimax(board, True)

                    board[i][j] = ' '

                    best_score = min(best_score, score)

        return best_score


def computer_move(board):
    best_score = -float('inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = COMPUTER

                score = minimax(board, False)

                board[i][j] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = COMPUTER


def human_move(board):
    while True:
        try:
            position = int(input("Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number from 1 to 9.")
                continue

            row = (position - 1) // 3
            col = (position - 1) % 3

            if board[row][col] != ' ':
                print("That position is already occupied.")
                continue

            board[row][col] = HUMAN
            break

        except ValueError:
            print("Please enter a valid number.")


def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    print("TIC-TAC-TOE")
    print("You are X, Computer is O")
    print()
    print("Positions are:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        # Human's turn
        human_move(board)
        print_board(board)

        winner = check_winner(board)

        if winner:
            print("Human wins!")
            break

        if is_board_full(board):
            print("Game is a draw!")
            break

        # Computer's turn
        print("Computer is thinking...")
        computer_move(board)
        print_board(board)

        winner = check_winner(board)

        if winner:
            print("Computer wins!")
            break

        if is_board_full(board):
            print("Game is a draw!")
            break


if __name__ == "__main__":
    main()