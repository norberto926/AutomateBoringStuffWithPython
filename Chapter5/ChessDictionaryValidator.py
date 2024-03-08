def isValidChessBoard(board):
    
    all_chess_pieces = {"wpawn": 8, "wknight": 2, "wbishop": 2, "wrook": 2, "wqueen": 1, "wking": 1, \
                        "bpawn": 8, "bknight" : 2, "bbishop" : 2, "brook": 2, "bqueen": 1, "bking": 1}
    
    all_board_positions = []
    
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
    for i in range(1, 9):
        
        for j in range(8):
            
            board_position = str(i) + letters[j]
            
            all_board_positions.append(board_position)
            
    isWKing = False
        
    isBKing = False
            
    for position, figure in board.items():
        
        if figure == "bking":
            isBKing = True
        
        if figure == "wking":
            isWKing = True
            

        
        if position not in all_board_positions:
            
            return False
        
        if figure not in all_chess_pieces:
            
            return False
        
        #checking if two pieces have the same position
        
        if position in all_board_positions:
            
            all_board_positions.remove(position)
            
        else:
            
            return False
        
        #checking the proper count of each piece
        
        all_chess_pieces[figure] = all_chess_pieces[figure] - 1
        
        if all_chess_pieces[figure] < 0:
            
            return False
        
    #checking if there are two kings on the board

    if isWKing == False or isBKing == False:
        return False
    
    return True
            
    
print(isValidChessBoard({"1g": "wking", "2f": "bking"}))