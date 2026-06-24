# Tic-Tac-Toe AI using Minimax Algorithm

An unbeatable AI agent that plays Tic-Tac-Toe against a human player. Built with Python, using the **Minimax Algorithm** for optimal decision-making. The AI explores every possible future game state and always chooses the best move — it **never loses**.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Objective](#objective)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [How to Run](#how-to-run)
6. [Board Representation](#board-representation)
7. [Game Flow](#game-flow)
8. [Win Detection Logic](#win-detection-logic)
9. [Draw Detection Logic](#draw-detection-logic)
10. [Minimax Algorithm](#minimax-algorithm)
11. [How AI Chooses the Best Move](#how-ai-chooses-the-best-move)
12. [Function-Wise Explanation](#function-wise-explanation)
13. [Sample Input / Output](#sample-input--output)
14. [Test Cases](#test-cases)
15. [Complexity Analysis](#complexity-analysis)
16. [Advantages of Minimax](#advantages-of-minimax)
17. [Limitations of Minimax](#limitations-of-minimax)
18. [Future Enhancements](#future-enhancements)
19. [Flowchart Description](#flowchart-description)
20. [Viva / Interview Questions](#viva--interview-questions)
21. [Demo Video Script](#demo-video-script)
22. [Resume Project Description](#resume-project-description)
23. [LinkedIn Post](#linkedin-post)

---

## Project Overview

This project implements a classic **Tic-Tac-Toe** game where a human player (X) competes against an AI opponent (O). The AI uses the **Minimax algorithm** — a fundamental concept in Artificial Intelligence and Game Theory — to evaluate every possible outcome of the game and select the move that guarantees the best result for itself.

The game runs in the terminal with a clean, user-friendly interface that displays the board with cell numbers, validates all user inputs, and announces the result at the end.

---

## Objective

- Develop an intelligent AI agent capable of playing Tic-Tac-Toe optimally.
- Demonstrate understanding of the **Minimax search algorithm**.
- Implement concepts from **Game Theory**, **Decision Trees**, and **Recursive Search**.
- Create clean, modular, beginner-friendly Python code.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **`math` module** | Provides `math.inf` for infinity in minimax scoring |
| **`time` module** | Adds a small delay to simulate AI "thinking" |
| **`random` module** | Imported for potential future use / extensions |

No external libraries or installations are required.

---

## Project Structure

```
Tic_Tac_Toe_AI/
│
├── tic_tac_toe.py      # Main Python source code
└── README.md           # Project documentation (this file)
```

---

## How to Run

1. Make sure **Python 3.x** is installed.
2. Open a terminal and navigate to the project folder:
   ```bash
   cd Tic_Tac_Toe_AI
   ```
3. Run the game:
   ```bash
   python tic_tac_toe.py
   ```
4. Enter a number (1-9) to place your mark on the board.
5. Try to beat the AI!

---

## Board Representation

The board is stored as a **2D list (3×3 matrix)**. Each element holds `"X"`, `"O"`, or `" "` (empty space).

```python
board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
```

```
 Index Mapping:              Display (shown to user):
 board[0][0] | board[0][1] | board[0][2]       1 | 2 | 3
 board[1][0] | board[1][1] | board[1][2]       4 | 5 | 6
 board[2][0] | board[2][1] | board[2][2]       7 | 8 | 9
```

**Conversion between user input (1-9) and board indices:**
```python
row = (move - 1) // SIDE    # SIDE = 3
col = (move - 1) % SIDE
```

---

## Constants

| Constant | Value | Purpose |
|---|---|---|
| `COMPUTER` | `1` | Identifier for the computer player |
| `HUMAN` | `2` | Identifier for the human player |
| `SIDE` | `3` | Board dimension (3×3) |
| `COMPUTERMOVE` | `'O'` | Symbol used by the computer |
| `HUMANMOVE` | `'X'` | Symbol used by the human |

---

## Game Flow

```
Start
  │
  ├── Display instructions (showInstructions)
  │   └── Show numbered 3×3 grid (1-9)
  │
  ├── Create empty 3×3 board (initialise)
  │
  ├── LOOP ──────────────────────────────┐
  │   ├── COMPUTER's turn:              │
  │   │   ├── AI calculates best move   │
  │   │   │   (using findBestMove +     │
  │   │   │    Minimax)                 │
  │   │   ├── Place O on board          │
  │   │   ├── Display board             │
  │   │   ├── Check game over → end     │
  │   │   └── Switch to HUMAN           │
  │   │                                 │
  │   ├── HUMAN's turn:                 │
  │   │   ├── Prompt for move (1-9)     │
  │   │   ├── Validate input            │
  │   │   ├── Place X on board          │
  │   │   ├── Display board             │
  │   │   ├── Check game over → end     │
  │   │   └── Switch to COMPUTER        │
  │   └─────────────────────────────────┘
  │
  ├── Display result (Win/Lose/Draw)
  └── End
```

> **Note:** The computer goes first by default (`playTicTacToe(COMPUTER)`).

---

## Win Detection Logic

A player wins by filling any of **8 possible lines**. The code uses three separate functions:

### `rowCrossed(board)`
Checks all 3 rows:
```python
for i in range(SIDE):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' ':
        return True
```

### `columnCrossed(board)`
Checks all 3 columns:
```python
for i in range(SIDE):
    if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
        return True
```

### `diagonalCrossed(board)`
Checks both diagonals:
```python
if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
    return True
if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
    return True
```

### `gameOver(board)`
Combines all three checks:
```python
def gameOver(board):
    return rowCrossed(board) or columnCrossed(board) or diagonalCrossed(board)
```

Additionally, `checkWinner(board, player)` checks if a **specific player** has won (used by the Minimax algorithm):

| Type | Winning Combinations |
|---|---|
| **Rows** | `[0][0],[0][1],[0][2]` — `[1][0],[1][1],[1][2]` — `[2][0],[2][1],[2][2]` |
| **Columns** | `[0][0],[1][0],[2][0]` — `[0][1],[1][1],[2][1]` — `[0][2],[1][2],[2][2]` |
| **Diagonals** | `[0][0],[1][1],[2][2]` — `[0][2],[1][1],[2][0]` |

---

## Draw Detection Logic

The `isBoardFull(board)` function checks if there are **no empty cells remaining** on the board. If all 9 cells are filled and neither player has won, the game is a draw.

```python
def isBoardFull(board):
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == ' ':
                return False
    return True
```

---

## Minimax Algorithm

### What is Minimax?

Minimax is a **recursive backtracking algorithm** used in two-player zero-sum games. It builds a complete **game tree** of all possible future states and assigns a score to each terminal state:

| Outcome | Score |
|---|---|
| Human (X) wins | `+10 - depth` |
| Computer (O) wins | `-10 + depth` |
| Draw | `0` |

### How it Works

1. The algorithm considers all possible moves using `getAvailableMoves(board)`.
2. For each move, it recursively simulates the game to completion.
3. The **Maximizer** (Human/X) tries to maximize the score.
4. The **Minimizer** (Computer/O) tries to minimize the score.
5. Scores propagate back up the tree.
6. The Computer picks the move with the **lowest** score (since it's the minimizer).

### Why `depth` is Used

The `depth` variable makes the AI prefer **faster wins** and **slower losses**. For example:
- Winning in 2 moves: `-10 + 2 = -8`
- Winning in 6 moves: `-10 + 6 = -4`
- The AI picks `-8` because it's lower (faster win).

### Pseudocode

```
function minimax(board, depth, isMaximizing):
    if Human wins:    return +10 - depth
    if Computer wins: return -10 + depth
    if Board full:    return 0

    if isMaximizing:
        best = -infinity
        for each empty cell (r, c):
            board[r][c] = HUMANMOVE
            score = minimax(board, depth+1, false)
            board[r][c] = ' '
            best = max(best, score)
        return best

    else:
        best = +infinity
        for each empty cell (r, c):
            board[r][c] = COMPUTERMOVE
            score = minimax(board, depth+1, true)
            board[r][c] = ' '
            best = min(best, score)
        return best
```

### Actual Implementation

```python
def minimax(board, depth, isMaximizing):
    if checkWinner(board, HUMANMOVE):
        return 10 - depth
    if checkWinner(board, COMPUTERMOVE):
        return -10 + depth
    if isBoardFull(board):
        return 0

    if isMaximizing:
        best = -math.inf
        for (r, c) in getAvailableMoves(board):
            board[r][c] = HUMANMOVE
            score = minimax(board, depth + 1, False)
            board[r][c] = ' '
            best = max(best, score)
        return best
    else:
        best = math.inf
        for (r, c) in getAvailableMoves(board):
            board[r][c] = COMPUTERMOVE
            score = minimax(board, depth + 1, True)
            board[r][c] = ' '
            best = min(best, score)
        return best
```

---

## How AI Chooses the Best Move

The `findBestMove(board)` function:

1. Iterates through every available (empty) cell using `getAvailableMoves(board)`.
2. Places the Computer's symbol (`O`) in that cell temporarily.
3. Calls `minimax()` to evaluate the resulting board state.
4. Undoes the move (restores `' '`).
5. Tracks the cell with the **lowest minimax score** (best for the minimizer).
6. Returns that `(row, col)` tuple as the Computer's chosen move.

```python
def findBestMove(board):
    bestScore = math.inf
    bestMove = (-1, -1)

    for (r, c) in getAvailableMoves(board):
        board[r][c] = COMPUTERMOVE
        score = minimax(board, 0, True)
        board[r][c] = ' '

        if score < bestScore:
            bestScore = score
            bestMove = (r, c)

    return bestMove
```

---

## Function-Wise Explanation

| Function | Purpose |
|---|---|
| `initialise()` | Returns a 3×3 list of empty strings `' '` representing the board |
| `showBoard(board)` | Prints the 2D board with pipe separators and dashes |
| `showInstructions()` | Prints the game title and a numbered 3×3 grid showing cell positions |
| `declareWinner(whoseTurn)` | Prints whether COMPUTER or HUMAN has won |
| `rowCrossed(board)` | Checks all 3 rows for a winning line |
| `columnCrossed(board)` | Checks all 3 columns for a winning line |
| `diagonalCrossed(board)` | Checks both diagonals for a winning line |
| `gameOver(board)` | Returns `True` if any row, column, or diagonal is crossed |
| `getAvailableMoves(board)` | Returns a list of `(row, col)` tuples where the board is still empty |
| `checkWinner(board, player)` | Checks all 8 winning lines for a specific player (used by Minimax) |
| `isBoardFull(board)` | Returns `True` if no empty cells remain (used by Minimax) |
| `minimax(board, depth, isMaximizing)` | Recursively evaluates board states and returns the optimal score |
| `findBestMove(board)` | Calls minimax for each available move and returns the best `(row, col)` for the Computer |
| `getHumanMove(board)` | Prompts, validates, and returns the human's chosen `(row, col)` |
| `playTicTacToe(whoseTurn)` | Main game loop: alternates turns, checks for game over, declares result |

---

## Sample Input / Output

```
			 Tic-Tac-Toe

Choose a cell numbered from 1 to 9 as below and play

			 1 | 2 | 3
			-------------
			 4 | 5 | 6
			-------------
			 7 | 8 | 9

==========================================

COMPUTER is thinking...
COMPUTER has put a O in cell 1


			 O |   |
			--------------
			   |   |
			--------------
			   |   |

Enter your move (1-9): 5
HUMAN has put a X in cell 5


			 O |   |
			--------------
			   | X |
			--------------
			   |   |

COMPUTER is thinking...
COMPUTER has put a O in cell 2


			 O | O |
			--------------
			   | X |
			--------------
			   |   |

Enter your move (1-9): 3
HUMAN has put a X in cell 3


			 O | O | X
			--------------
			   | X |
			--------------
			   |   |

COMPUTER is thinking...
COMPUTER has put a O in cell 7


			 O | O | X
			--------------
			   | X |
			--------------
			 O |   |

...game continues until draw...

Draw Match
```

---

## Test Cases

| # | Scenario | Human Moves | Expected Outcome |
|---|---|---|---|
| 1 | Human plays center first | 5 → random | Draw (AI blocks optimally) |
| 2 | Human plays corner first | 1 → random | Draw (AI blocks optimally) |
| 3 | Human plays edge first | 2 → random | Draw (AI blocks optimally) |
| 4 | Invalid input: letter | "abc" | Shows error, asks again |
| 5 | Invalid input: out of range | 10 | Shows error, asks again |
| 6 | Occupied cell chosen | Already-taken position | Shows error, asks again |
| 7 | Full game to draw | Optimal play from both | Draw |
| 8 | Human tries to win | Any strategy | AI blocks and forces draw |

---

## Complexity Analysis

### Time Complexity

- **Worst case:** `O(b^d)` where `b` = branching factor and `d` = depth.
- For Tic-Tac-Toe: up to `O(9!)` = **362,880** possible game states.
- In practice, many branches terminate early due to wins/draws.

### Space Complexity

- **O(d)** = `O(9)` for the recursion stack depth (maximum 9 moves in a game).
- The board itself uses `O(3×3)` = `O(1)` constant space.

Since Tic-Tac-Toe has a small state space, Minimax runs nearly instantly.

---

## Advantages of Minimax

| Advantage | Description |
|---|---|
| **Optimal play** | Guarantees the best possible outcome for the AI |
| **Complete** | Explores the entire game tree — no moves are missed |
| **Deterministic** | Same board state always produces the same move |
| **Simple to implement** | Clean recursive structure, easy to understand |
| **No training data needed** | Unlike ML, it works purely through logical search |

---

## Limitations of Minimax

| Limitation | Description |
|---|---|
| **Exponential time** | Impractical for games with huge state spaces (e.g., Chess, Go) |
| **No learning** | The AI doesn't improve over time or adapt to specific opponents |
| **Full tree exploration** | Explores unnecessary branches that could be pruned |
| **Memory usage** | Deep recursion can be an issue for complex games |

---

## Future Enhancements

### 1. Alpha-Beta Pruning
The most important optimization for Minimax. It **prunes branches** of the game tree that cannot possibly affect the final decision, reducing time complexity from `O(b^d)` to `O(b^(d/2))` in the best case.

```python
def minimax(board, depth, isMaximizing, alpha, beta):
    # ... base cases same as before ...

    if isMaximizing:
        best = -math.inf
        for (r, c) in getAvailableMoves(board):
            board[r][c] = HUMANMOVE
            score = minimax(board, depth + 1, False, alpha, beta)
            board[r][c] = ' '
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break   # Beta cutoff — prune this branch
        return best
    else:
        # ... similar with alpha cutoff ...
```

### 2. GUI with Pygame or Tkinter
Build a graphical interface with clickable cells, animations, and sound effects.

### 3. Adjustable Difficulty
Add Easy (random moves) and Medium (minimax with depth limit) modes.

### 4. Multiplayer Mode
Allow two human players to compete against each other.

### 5. Larger Boards (4x4, 5x5)
Extend the game to bigger grids with Alpha-Beta pruning for performance.

---

## Flowchart Description

```
┌─────────────┐
│    START     │
└──────┬──────┘
       │
       ▼
┌──────────────┐
│ Show         │
│ Instructions │
│ (numbered    │
│  grid 1-9)   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Create Empty │
│ 3×3 Board    │
│ (initialise) │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ COMPUTER's Turn? │──── NO ──► HUMAN's Turn
└──────┬───────────┘
       │ YES
       ▼
┌──────────────────┐
│ findBestMove()   │
│ using Minimax    │
│ Place O on board │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐     YES    ┌───────────┐
│ gameOver(board)?  ├──────────►│ Declare   │
│                  │            │ Winner    │
└──────┬───────────┘            └───────────┘
       │ NO
       ▼
┌──────────────────┐     YES    ┌───────────┐
│ moveCount == 9?  ├──────────►│ Draw      │
│ (Board Full?)    │            │ Match     │
└──────┬───────────┘            └───────────┘
       │ NO
       ▼
┌──────────────────┐
│ Switch to HUMAN  │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐     NO     ┌───────────┐
│ getHumanMove()   ├──────────►│ Show Error│
│ Input Valid?     │  (invalid) │ Try Again │
└──────┬───────────┘            └───────────┘
       │ YES (valid)
       ▼
┌──────────────────┐
│ Place X on board │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐     YES    ┌───────────┐
│ gameOver(board)?  ├──────────►│ Declare   │
│                  │            │ Winner    │
└──────┬───────────┘            └───────────┘
       │ NO
       ▼
┌──────────────────┐     YES    ┌───────────┐
│ moveCount == 9?  ├──────────►│ Draw      │
│ (Board Full?)    │            │ Match     │
└──────┬───────────┘            └───────────┘
       │ NO
       ▼
  (Loop back to COMPUTER's Turn)
```

---

## Viva / Interview Questions

### Q1: What is the Minimax Algorithm?
**A:** Minimax is a recursive backtracking algorithm used in two-player zero-sum games. It builds a game tree of all possible future moves, assigning scores to terminal states (win/lose/draw), and picks the move that guarantees the best outcome for the current player.

### Q2: Why is the Computer called the "minimizer"?
**A:** In our implementation, the Human (X) is the maximizer (tries to maximize the score), and the Computer (O) is the minimizer (tries to minimize the score). The Computer picks the move with the lowest score to ensure the best outcome for itself.

### Q3: What is the time complexity of Minimax for Tic-Tac-Toe?
**A:** The worst-case time complexity is O(9!) ≈ 362,880 possible states. However, in practice, many branches terminate early due to wins or draws, so it runs almost instantly.

### Q4: How does the depth parameter improve the AI?
**A:** The depth parameter makes the AI prefer faster wins and slower losses. For example, if the Computer can win in 2 moves or 6 moves, the depth ensures it picks the 2-move win because that path has a lower (better for minimizer) score: `-10 + 2 = -8` vs `-10 + 6 = -4`.

### Q5: What is Alpha-Beta Pruning?
**A:** Alpha-Beta Pruning is an optimization of Minimax that eliminates branches of the game tree that cannot possibly influence the final decision. It maintains two values: alpha (best score for maximizer) and beta (best score for minimizer). When beta ≤ alpha, the branch is pruned. Our current implementation does not use it but can be added as a future enhancement.

### Q6: Can the AI ever lose?
**A:** No. With perfect Minimax implementation, the AI will either win or draw. It is mathematically impossible for the AI to lose because it evaluates every possible outcome and always chooses optimally.

### Q7: How is the board represented in your code?
**A:** The board is a 2D Python list (3×3 matrix). Each element `board[row][col]` holds `"X"`, `"O"`, or `" "` (empty space). User input (1-9) is converted to `(row, col)` using `row = (move-1) // 3` and `col = (move-1) % 3`.

### Q8: What is a zero-sum game?
**A:** A zero-sum game is one where one player's gain is exactly equal to the other player's loss. In Tic-Tac-Toe, if X wins (+1), then O loses (-1). The sum is always zero.

### Q9: What modules did you use and why?
**A:** `math` for `math.inf` (infinity values in minimax), `time` for adding a 1-second delay to simulate Computer thinking, and `random` (imported for potential extensions). No external packages are needed.

### Q10: How would you extend this project?
**A:** I would add Alpha-Beta Pruning for optimization, build a GUI using Pygame or Tkinter, add difficulty levels (easy/medium/hard), implement a multiplayer mode, and potentially extend it to larger board sizes like 4×4 or 5×5.

### Q11: What is the difference between `gameOver()` and `checkWinner()`?
**A:** `gameOver(board)` checks if **any** player has won (used in the main game loop to detect end-of-game). `checkWinner(board, player)` checks if a **specific** player has won (used by the Minimax algorithm to assign scores). They check the same 8 winning lines but serve different purposes.

### Q12: Why does the Computer go first?
**A:** In our implementation, `playTicTacToe(COMPUTER)` is called, giving the Computer the first move. This can be changed by calling `playTicTacToe(HUMAN)` to let the human go first.

---

## Demo Video Script

**Duration:** 2–3 minutes

### [0:00 – 0:20] Introduction
> "Hello! Today I'm presenting my AI internship project — a Tic-Tac-Toe game where you play against an unbeatable AI powered by the Minimax Algorithm. The AI evaluates every possible move and always makes the optimal decision."

### [0:20 – 0:50] Running the Program
> "Let me run the program. As you can see, it displays instructions with a numbered 3×3 grid. The Computer plays as O and goes first, and I play as X."

### [0:50 – 1:30] Gameplay Demo
> "The Computer starts by placing O in a cell. Now it's my turn — I'll enter a number from 1 to 9. Notice how the program validates my input — if I enter a letter or an out-of-range number, it shows an error and asks again. The Computer uses the Minimax algorithm to think for a second, then makes its move. No matter what strategy I use, the AI either wins or forces a draw."

### [1:30 – 2:00] Explaining the Algorithm
> "Behind the scenes, the AI uses the Minimax algorithm. It recursively explores every possible future game state, scores each outcome using +10 for human wins and -10 for computer wins (adjusted by depth), and picks the move that minimizes my advantage. The depth parameter ensures the AI prefers faster wins."

### [2:00 – 2:30] Code Walkthrough
> "The code uses a 2D list for the board, separate functions for row, column, and diagonal win detection, and a clean game loop that alternates between Computer and Human turns. The `findBestMove` function evaluates every empty cell using Minimax and picks the best one."

### [2:30 – 2:50] Conclusion
> "This project demonstrates key AI concepts including game tree search, recursive algorithms, and adversarial decision-making. Future improvements could include Alpha-Beta Pruning, a GUI, and adjustable difficulty levels. Thank you!"

---

## Resume Project Description

> **Tic-Tac-Toe AI using Minimax Algorithm** — Developed an intelligent, unbeatable AI agent in Python that plays Tic-Tac-Toe against a human player. Implemented the Minimax search algorithm with depth-based scoring to ensure optimal decision-making. The project features a terminal interface with a 2D board display, robust input validation (handles invalid types, out-of-range values, and occupied cells), win/draw detection using row, column, and diagonal checks, and a turn-based game loop. Demonstrated understanding of Artificial Intelligence, Game Theory, Decision Trees, and Recursive Search Algorithms.

---

## LinkedIn Post

> 🎮🤖 **Excited to share my latest AI project!**
>
> I built a **Tic-Tac-Toe AI** powered by the **Minimax Algorithm** as part of my AI internship at CodSoft!
>
> 🔹 The AI is **unbeatable** — it evaluates every possible future move and always plays optimally
> 🔹 Built with **pure Python** — no external libraries
> 🔹 Features a terminal UI with input validation and clear board display
> 🔹 Demonstrates concepts from **Game Theory**, **Decision Trees**, and **Recursive Search**
>
> The Minimax algorithm explores the entire game tree (up to 362,880 states) and picks the move that guarantees the best outcome. Try as you might, you can only draw — never win! 🏆
>
> This project deepened my understanding of adversarial search, zero-sum games, and how AI agents make decisions in competitive environments.
>
> 🔗 Check out the code on GitHub!
>
> #ArtificialIntelligence #Python #GameTheory #Minimax #CodSoft #Internship #AI #MachineLearning #TicTacToe #DSA
