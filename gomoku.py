def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return False
    return True
                
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    y_start_of_seq = y_end - d_y * (length - 1)
    x_start_of_seq = x_end - d_x * (length - 1) 
    bounded = 0 
   
    # (0,1) Cases
    
    if d_y == 0 and d_x == 1:
        if x_start_of_seq == 0 or x_end == 7:
            bounded += 1
            if x_start_of_seq != 0:
                if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                    bounded += 1
            elif x_end != 7:
                if board[y_end + d_y][x_end + d_x] != " ":
                    bounded += 1
        else:
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
            if board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
                
            
    # (1,0) Cases  
    
    elif d_y == 1 and d_x == 0:
        if y_start_of_seq == 0 or y_end == 7:
            bounded += 1
            if y_end != 7:
                if board[y_end + d_y][x_end + d_x] != " ":
                    bounded += 1
            elif y_start_of_seq != 0:
                if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                    bounded += 1
        else:
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
            if board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
    
    # Diagonal Case (1,1)
    
    elif d_y == 1 and d_x == 1:
        
        if 0 < y_start_of_seq < 7 and x_start_of_seq == 0:
            bounded += 1
            if y_end == 7:
                bounded += 1
            elif board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
        
        elif  0 < x_start_of_seq < 7 and y_start_of_seq == 0:
            bounded += 1
            if x_end == 7:
                bounded += 1
            elif board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
        
        elif y_start_of_seq == 0 and x_start_of_seq == 0:
            bounded += 1
            if board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
        
        elif y_end == 7 and 0 < x_end < 7 and x_start_of_seq != 0:
            bounded += 1
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
        
        elif x_end == 7 and 0 < y_end < 7 and yield_start != 0:
            bounded += 1
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
        
        elif x_end == 7 and y_end == 7:
            bounded += 1
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
        
        elif (x_start_of_seq == 0 and y_start_of_seq == 7) or (x_start_of_seq == 7 and y_start_of_seq == 0):
            bounded += 2
        

        else:
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
            if board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
        
    # Diagonal Case (1, -1)
    
    elif d_y == 1 and d_x == -1:
        
        if 0 < y_start_of_seq < 7 and x_start_of_seq == 7:
            bounded += 1
            if y_end == 7:
                bounded += 1
            elif board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
        
        elif  0 < x_start_of_seq < 7 and y_start_of_seq == 0:
            bounded += 1
            if x_end == 0:
                bounded += 1
            elif board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
        
        elif y_start_of_seq == 0 and x_start_of_seq == 7:
            bounded += 1
            if board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
        
        elif y_end == 7 and 0 < x_end < 7 and x_start_of_seq != 7:
            bounded += 1
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
        
        elif x_end == 0 and 0 < y_end < 7 and y_start_of_seq != 0:
            bounded += 1
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
        
        elif x_end == 0 and y_end == 7:
            bounded += 1
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
        
        elif (x_start_of_seq == 0 and y_start_of_seq == 0) or (x_start_of_seq == 7 and y_start_of_seq == 7):
            bounded += 2
                
        else:
            if board[y_start_of_seq - d_y][x_start_of_seq - d_x] != " ":
                bounded += 1
            if board[y_end + d_y][x_end + d_x] != " ":
                bounded += 1
    
    if bounded == 0:
        return "OPEN"
    elif bounded == 1:
        return "SEMIOPEN"
    elif bounded == 2:
        return "CLOSED"
        
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    current_y = y_start
    current_x = x_start
    open_seq_count = 0
    semi_open_seq_count = 0
    open_truth = None
    semi_open_truth = None
    i = 0
    
    # Open
    
    if d_x == -1:
        
        while (i < x_start - length) and (i < (8 - y_start - length)):
    
            open_truth = True
            current_y += d_y * 1
            current_x += d_x * 1
            
            if board[current_y][current_x] == col:
                for j in range(length):
                    if board[current_y + d_y * j][current_x + d_x * j] != col:
                        open_truth = False
            
            if board[current_y][current_x] == col:
                if open_truth == True:                
                    y_end = current_y + d_y * (length - 1)
                    x_end = current_x + d_x * (length - 1)
                    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN":
                        open_seq_count += 1

            i += 1
    
    elif d_x == 1 or d_x == 0:
        
        while (i < (8 - (x_start * d_x) - (length * d_x))) and (i < (8 - y_start - (d_y * length))):
            
            open_truth = True
            current_y += d_y * 1
            current_x += d_x * 1
            
            if board[current_y][current_x] == col:
                for j in range(length):
                    if board[current_y + d_y * j][current_x + d_x * j] != col:
                        open_truth = False
            
            if board[current_y][current_x] == col:
                if open_truth == True:                
                    y_end = current_y + d_y * (length - 1)
                    x_end = current_x + d_x * (length - 1)
                    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN":
                        open_seq_count += 1

            i += 1
    
    
    # Reset of currents (y,x)
    
    current_y = y_start
    current_x = x_start
    
    # Semi Open
    
    if d_x == -1:
        
        while ((current_y + d_y * length) <= 8) and ((current_x + d_x * length) <= 8):
    
            semi_open_truth = True
            if board[current_y][current_x] == col:
                for j in range(length):
                    if board[current_y + d_y * j][current_x + d_x * j] != col:
                        semi_open_truth = False 
            
            if board[current_y][current_x] == col:
                if semi_open_truth == True:
                    y_end = current_y + d_y * (length - 1)
                    x_end = current_x + d_x * (length - 1)
                    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMIOPEN":
                        current_y += d_y * length
                        current_x += d_x * length
                        semi_open_seq_count += 1
                    else:
                        current_y += d_y * 1
                        current_x += d_x * 1 
                else:
                    current_y += d_y * 1
                    current_x += d_x * 1 
            else:
                current_y += d_y * 1
                current_x += d_x * 1 
                        
    elif d_x == 1 or d_x == 0:
        
        while ((current_y + d_y * (length -1)) < 8) and ((current_x + d_x * (length - 1)) < 8):
            
            semi_open_truth = True
            if board[current_y][current_x] == col:
                for j in range(length):
                    if board[current_y + d_y * j][current_x + d_x * j] != col:
                        semi_open_truth = False 
            
            if board[current_y][current_x] == col:
                if semi_open_truth == True:
                    y_end = current_y + d_y * (length - 1)
                    x_end = current_x + d_x * (length - 1)
                    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMIOPEN":
                        current_y += d_y * length
                        current_x += d_x * length
                        semi_open_seq_count += 1
                    else:
                        current_y += d_y * 1
                        current_x += d_x * 1
                else:
                    current_y += d_y * 1
                    current_x += d_x * 1 
            else:
                current_y += d_y * 1
                current_x += d_x * 1 
    
    seq_count = (open_seq_count, semi_open_seq_count)
    return seq_count
                
            
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    #0,1
    for i in range (len(board)-1):
        open_seq_count += detect_row(board, col, i, 0, length, 0, 1)[0]
        semi_open_seq_count += detect_row(board, col, i, 0, length, 0, 1)[1]
    #1,0
    for i in range (len(board)-1):
        open_seq_count += detect_row(board, col, 0, i, length, 1, 0)[0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, 0)[1]
    #1,1
    for i in range (len(board)-1):
        open_seq_count += detect_row(board, col, 0, i, length, 1, 1)[0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, 1)[1]
    for i in range (1,len(board)-1):
        open_seq_count += detect_row(board, col, i, 0, length, 1, 1)[0]
        semi_open_seq_count += detect_row(board, col, i, 0, length, 1, 1)[1]
    #1,-1
    for i in range (len(board)-1):
        open_seq_count += detect_row(board, col, 0, i, length, 1, -1)[0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, -1)[1]
    for i in range (1,len(board)-1):
        open_seq_count += detect_row(board, col, i, 7, length, 1, -1)[0]
        semi_open_seq_count += detect_row(board, col, i, 7, length, 1, -1)[1]
    
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    max_score = 0
    max_score_coords = []
    for i in range(7):
        for j in range(7):
            if board[i][j] == " ":
                board[i][j] = "b"
                if score(board) > max_score:
                    max_score = score(board)
                    max_score_coords = [i, j]
                    board[i][j] = " "
    return max_score_coords

def is_win(board):
    
    # Checking Horizontal  
    
    for i in range(len(board)):
        for j in range(4):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == board[i][j + 4]:
                if board[i][3] == "w":
                   return "White won"
                elif board[i][3] == "b":
                    return "Black won"
                    
    # Checking Vertical
    
    for i in range(len(board)):
        for j in range(4):
            if board[j][i] == board[j + 1][i] == board[j + 2][i] == board[j + 3][i] == board[j + 4][i]:
                if board[3][i] == "w":
                    return "White won"
                elif board[3][i] == "b":
                    return "Black won"
    
    # Checking Diagonal Right
    
    win_truth = True
    for i in range(5):
        if board[3][0] != board[3 + i][0 + i]:
            win_truth = False
    if win_truth == True:
        if board[5][2] == "w":
            return "White won"
        elif board[5][2] == "b":
            return "Black won"
    
    counter = 0
    for i in range(2):
        for j in range(5):
            if board[2 + i][i] == board[2 + i + j][i + j]:
                counter += 1
            if counter == 5:
                if board[5][3] == "w":
                    return "White won"
                elif board[5][3] == "b":
                    return "Black won"  
        counter = 0
    
    counter = 0
    for i in range(3):
        for j in range(5):
            if board[1 + i][i] == board[1 + i + j][i + j]:
                counter += 1
            if counter == 5:
                if board[4][3] == "w":
                    return "White won"
                elif board[4][3] == "b":
                    return "Black won"  
        counter = 0
    
    counter = 0
    for i in range(4):
        for j in range(5):
            if board[i][i] == board[i + j][i + j]:
                counter += 1
            if counter == 5:
                if board[3][3] == "w":
                    return "White won"
                elif board[3][3] == "b":
                    return "Black won"  
        counter = 0
        
    counter = 0
    for i in range(3):
        for j in range(5):
            if board[i][1 + i] == board[i + j][1 + i + j]:
                counter += 1
            if counter == 5:
                if board[3][4] == "w":
                    return "White won"
                elif board[3][4] == "b":
                    return "Black won"  
        counter = 0
        
    counter = 0
    for i in range(2):
        for j in range(5):
            if board[i][2 + i] == board[i + j][2 + i + j]:
                counter += 1
            if counter == 5:
                if board[3][5] == "w":
                    return "White won"
                elif board[3][5] == "b":
                    return "Black won"  
        counter = 0
    
    win_truth = True
    for i in range(5):
        if board[0][3] != board[i][3 + i]:
            win_truth = False
    if win_truth == True:
        if board[2][5] == "w":
            return "White won"
        elif board[2][5] == "b":
            return "Black won"
            
    # Checking Diagonal Left 
    
    win_truth = True    
    for i in range(5):
        if board[3][7] == board[3 + i][7 - i]:
            win_truth = False
    if win_truth == True:
        if board[5][5] == "w":
            return "White won"
        elif board[5][5] == "b":
            return "Black won"
            
    counter = 0
    for i in range(2):
        for j in range(5):
            if board[2 + i][7 - i] == board[2 + i + j][7 - i - j]:
                counter += 1
            if counter == 5:
                if board[5][4] == "w":
                    return "White won"
                elif board[5][4] == "b":
                    return "Black won"  
        counter = 0 
    
    counter = 0
    for i in range(3):
        for j in range(5):
            if board[1 + i][7 - i] == board[1 + i + j][7 - i - j]:
                counter += 1
            if counter == 5:
                if board[4][4] == "w":
                    return "White won"
                elif board[4][4] == "b":
                    return "Black won"  
        counter = 0
                
    counter = 0
    for i in range(4):
        for j in range(5):
            if board[i][7 - i] == board[i + j][7 - i - j]:
                counter += 1
            if counter == 5:
                if board[3][4] == "w":
                    return "White won"
                elif board[3][4] == "b":
                    return "Black won"  
        counter = 0
                
    counter = 0
    for i in range(3):
        for j in range(5):
            if board[i][6 - i] == board[i + j][6 - i - j]:
                counter += 1
            if counter == 5:
                if board[3][3] == "w":
                    return "White won"
                elif board[3][3] == "b":
                    return "Black won"  
        counter = 0
                
    counter = 0
    for i in range(2):
        for j in range(5):
            if board[i][5 - i] == board[i + j][5 - i - j]:
                counter += 1
            if counter == 5:
                if board[2][3] == "w":
                    return "White won"
                elif board[2][3] == "b":
                    return "Black won"  
        counter = 0
    
    win_truth = True
    for i in range(5):
        if board[0][4] == board[i][4 - i]:
            win_truth = False
    if win_truth == True:
        if board[2][2] == "w":
            return "White won"
        elif board[2][2] == "b":
            return "Black won"
            
    # Draw or Continue Playing
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return "Continue playing"
    return "Draw"
                
    
    
    
   
    ####CHANGE ME
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    pass


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
        
        
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 3, 0, 1, 2, "w")
    put_seq_on_board(board, 3, 3, 0, 1, 2, "w")
    put_seq_on_board(board, 5, 7, 1, -1, 2, "w")
    put_seq_on_board(board, 1, 5, 1, 0, 3, "b")
    put_seq_on_board(board, 3, 1, 1, 1, 3, "b")
    put_seq_on_board(board, 0, 2, 1, 0, 3, "b")
    print(board)
    print(detect_row(board, "w", 0, 5, 1, 1, 0))
    print(detect_rows(board,'w',2))
    print(detect_rows(board,'b',3))
    print(search_max(board))
    
   









