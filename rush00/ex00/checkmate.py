def checkmate(board):

    class pieces:
        def __init__(self, addr):
            self.addr = addr
            self.atk = list()

    rowus = board.splitlines()
    rows = [s.strip() for s in rowus]
    #print(rows)

    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell == "R": 
                rook = pieces([r,c])
            elif cell == "B": 
                bishop = pieces([r,c])
            elif cell == "P": 
                pawn = pieces([r,c])
            elif cell == "Q": 
                queen = pieces([r,c])
            elif cell == "K": 
                king = pieces([r,c])

            #print(r, c, cell)

    #rook queen  
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if r == rook.addr[0] or c == rook.addr[1]:
                rook.atk.append([r,c])
            if r == queen.addr[0] or c == queen.addr[1]:
                queen.atk.append([r,c])

    #bishop queen
    for i in range(1,len(rows)+1):
        bishop.atk.append([bishop.addr[0]+i,bishop.addr[1]+i])
        bishop.atk.append([bishop.addr[0]-i,bishop.addr[1]-i])
        bishop.atk.append([bishop.addr[0]+i,bishop.addr[1]-i])
        bishop.atk.append([bishop.addr[0]-i,bishop.addr[1]+i])
        queen.atk.append([queen.addr[0]+i,queen.addr[1]+i])
        queen.atk.append([queen.addr[0]-i,queen.addr[1]-i])
        queen.atk.append([queen.addr[0]+i,queen.addr[1]-i])
        queen.atk.append([queen.addr[0]-i,queen.addr[1]+i])

    #pawn
    pawn.atk = [[pawn.addr[0]-1,pawn.addr[1]-1],[pawn.addr[0]-1,pawn.addr[1]+1]]

    # print("PAWN",pawn.addr)
    # print(pawn.atk)
    # print("BISHOP",bishop.addr)
    # print(bishop.atk)
    # print("ROOK",rook.addr)
    # print(rook.atk)
    # print("QUEEN",queen.addr)
    # print(queen.atk)
    # print("KING",king.addr)

    if king.addr in pawn.atk or king.addr in bishop.atk or king.addr in rook.atk or king.addr in queen.atk:
        print("Success")
        return
    else: print("Fail")
