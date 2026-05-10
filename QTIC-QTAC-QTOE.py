# Quantum Tic Tac Toe with Quantum Simulation and AI Opponent
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import math
# ---------- Quantum Setup ----------
qc = QuantumCircuit(9, 9)
player_map = {}
taken_positions = set()
mid_game_message_shown = False
# ---------- Utilities ----------
def display_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
def available_positions():
    return [i for i in range(9) if i not in taken_positions]
def current_classical_view():
    board = ['-'] * 9
    for pos in taken_positions:
        board[pos] = player_map[pos]
    return board
# ---------- Quantum Logic ----------
def quantum_move(player, position):
    global qc, player_map
    qc.h(position) 
    if player == 'x':
        qc.z(position)
    elif player == 'o':
        qc.x(position)
    player_map[position] = player
    taken_positions.add(position)
def quantum_simulation():
    backend = Aer.get_backend("aer_simulator")
    while True:
        qc_copy = qc.copy()
        qc_copy.measure(range(9), range(9))
        compiled = transpile(qc_copy, backend)
        job = backend.run(compiled, shots=512)
        result = job.result()
        counts = result.get_counts()
        state = max(counts, key=counts.get)[::-1]
        board = ['-'] * 9
        x_count = 0
        o_count = 0
        for i, bit in enumerate(state):
            if bit == '1':
                player = player_map.get(i, 'x')
                board[i] = player
                if player == 'x':
                    x_count += 1
                else:
                    o_count += 1
        if x_count >= 3 and o_count >= 3:
            return board
# ---------- Primary Win Check ----------
def check_winner(board):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for a,b,c in wins:
        if board[a]==board[b]==board[c] and board[a]!='-':
            return board[a]
    return None
# ---------- Secondary Neighbour Logic ----------
def neighbour_score(board):
    x_score = 0
    o_score = 0
    for i in range(9):
        if i == 4:  # ignore centre
            continue
        if board[i] == '-':
            continue
        row = i // 3
        col = i % 3
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr == 0 and dc == 0:
                    continue
                nr = row + dr
                nc = col + dc
                if 0 <= nr < 3 and 0 <= nc < 3:
                    ni = nr*3 + nc
                    if ni == 4:
                        continue
                    if board[ni] == board[i]:
                        if board[i] == 'x':
                            x_score += 1
                        elif board[i] == 'o':
                            o_score += 1
    return x_score, o_score
# ---------- Mid Game Check ----------
def mid_game_check():
    board = current_classical_view()
    return check_winner(board)
# ---------- AI ----------
def minimax(board, depth, is_max, alpha, beta, ai, human):
    winner = check_winner(board)
    if winner == ai:
        return 10 - depth
    if winner == human:
        return depth - 10
    if '-' not in board:
        return 0
    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = ai
                val = minimax(board, depth+1, False, alpha, beta, ai, human)
                board[i] = '-'
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = human
                val = minimax(board, depth+1, True, alpha, beta, ai, human)
                board[i] = '-'
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best
def best_move(ai, human):
    board = current_classical_view()
    best_score = -math.inf
    move = None
    for i in available_positions():
        board[i] = ai
        score = minimax(board, 0, False, -math.inf, math.inf, ai, human)
        board[i] = '-'
        if score > best_score:
            best_score = score
            move = i
    return move
# ---------- Main Game ----------
def TIC_TAC_TOE():
    global qc, player_map, taken_positions, mid_game_message_shown
    print("Quantum Tic Tac Toe")
    print("[1][2][3]")
    print("[4][5][6]")
    print("[7][8][9]")
    qc = QuantumCircuit(9,9)
    player_map = {}
    taken_positions = set()
    mid_game_message_shown = False
    while True:
        mode = input("\n1. Player vs Player\n2. Player vs Computer\nChoice: ")
        if mode in ['1','2']:
            break
        print("Invalid choice")
    while True:
        p1 = input("Player 1 choose (x/o): ").lower()
        if p1 in ['x','o']:
            break
        print("Invalid choice")
    p2 = 'o' if p1 == 'x' else 'x'
    if mode == '2':
        print(f"Computer is '{p2.upper()}'")
    current = 'x'
    turn_count = 0
    while turn_count < 9:
        print("\nCurrent Board:")
        display_board(current_classical_view())
        print("Remaining positions:", [i+1 for i in available_positions()])
        if mode == '2' and current == p2:
            pos = best_move(p2, p1)
            print(f"Computer chooses position {pos+1}")
        else:
            try:
                pos = int(input(f"Player {current.upper()} choose position (1-9): ")) - 1
            except:
                print("Invalid choice")
                continue
        if pos not in available_positions():
            print("Invalid choice")
            continue
        quantum_move(current, pos)
        # Mid-game encouragement (only once)
        mid_winner = mid_game_check()
        if mid_winner and not mid_game_message_shown:
            other = 'O' if mid_winner == 'x' else 'X'
            print(f"\n{mid_winner.upper()} has formed a line!")
            print(f"{other}, do not lose hope — this is quantum. The final result can still change.\n")
            mid_game_message_shown = True
        turn_count += 1
        current = 'o' if current == 'x' else 'x'
    # ---------- After 9 Moves ----------
    print("\nAll positions filled.")
    print("\nRunning 3 quantum simulations...\n")
    for sim in range(1,4):
        print(f"Simulation {sim}:")
        final_board = quantum_simulation()
        display_board(final_board)
        winner = check_winner(final_board)
        if winner:
            print("Winner:", winner.upper())
        else:
            x_score, o_score = neighbour_score(final_board)
            print(f"Neighbour Score -> X: {x_score} | O: {o_score}")
            if x_score > o_score:
                print("Winner by neighbour rule: X")
            elif o_score > x_score:
                print("Winner by neighbour rule: O")
            else:
                print("Tie")
        print("-" * 30)
if __name__ == "__main__":
    # ---------- Welcome Message ----------
    print("Welcome to Quantum Tic Tac Toe!\n \
    In this game, the final outcome is determined by quantum simulations after all moves are made.\n \
    Make your moves wisely, but remember - in the quantum world, anything can happen!\nInstructions:\n \
          1. Choose your mode (PvP or PvC).\n \
          2. Players take turns choosing positions (1-9) to place their mark (X or O).\n \
          3. After all positions are filled, 3 quantum simulations will determine the final board state \n \
          and the winner.\n \
          4. In case of no clear winner, a neighbour-based scoring system will determine the winner.\n \
    Note: The center position (5) is not affected by quantum moves and cannot be chosen by players.\n \
    Good luck, and may the quantum odds be ever in your favor!\n")
    # ---------- Run Game Loop ----------
    while True:
        TIC_TAC_TOE()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing Quantum Tic Tac Toe!")
            break   