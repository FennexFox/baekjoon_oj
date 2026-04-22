import sys

input = sys.stdin.readline
print = sys.stdout.write

proximity_map = tuple((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y)

def is_on_board(position):
    return 0 <= position[0] <= 2 and 0 <= position[1] <= 2

def get_position(board, turn):
    positions = []

    for y, row in enumerate(board):
        for x, pos in enumerate(row):
            if turn == pos:
                positions.append([x, y])
    
    return positions

def is_proxy(board, turn, positions):
    is_proxy = False

    pos_1 = positions[0]
    for proxy in proximity_map:
        pos_2 = (pos_1[0] + proxy[0], pos_1[1] + proxy[1])
        
        if is_on_board(pos_2):
            token_at_pos2 = board[pos_2[1]][pos_2[0]]
            if token_at_pos2 == turn:
                is_proxy = True
            
    return is_proxy

def get_winning_pos(positions, is_proxy):
    pos_1, pos_2 = positions
    if not is_proxy:
        winning_pos = ((pos_1[0] + pos_2[0])/2, (pos_1[1] + pos_2[1])/2)
    else:
        delta_x = pos_2[0] - pos_1[0]
        delta_y = pos_2[1] - pos_1[1]
        winning_pos = ((pos_2[0] + delta_x), (pos_2[1] + delta_y))
        if not is_on_board(winning_pos):
            winning_pos = ((pos_1[0] - delta_x), (pos_1[1] - delta_y))
    
    return tuple(map(int, winning_pos))

def solve():
    num = int(input())

    for i in range(num):
        board = [list(input().strip()) for _ in range(3)]
        turn = input().strip()
        
        positions = get_position(board, turn)
        proxy = is_proxy(board, turn, positions)
        wininng_pos = get_winning_pos(positions, proxy)
        
        board[wininng_pos[1]][wininng_pos[0]] = turn
        
        print(f"Case {i+1}:\n")
        for row in board:
            print("".join(row)+"\n")

if __name__ == "__main__":
    solve()