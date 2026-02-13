def checkmate(board_str):
    rows = board_str.splitlines()
    n = len(rows)

    if any(len(row) != n for row in rows):
        print("Error")
        return

    board = [list(row.upper()) for row in rows]

    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == "K":
                king_pos = (i, j)

    if not king_pos:
        print("Error")
        return

    kr, kc = king_pos

    directions_rook = [(-1,0),(1,0),(0,-1),(0,1)]
    directions_bishop = [(-1,-1),(-1,1),(1,-1),(1,1)]

    for i in range(n):
        for j in range(n):
            piece = board[i][j].upper()

            # Pawn
            if piece == "P":
                if (i-1, j-1) == (kr, kc) or (i-1, j+1) == (kr, kc):
                    print(f"Success P in row:{i} , col{j}")
                    return

            # Rook
            if piece == "R":
                for dr, dc in directions_rook:
                    r, c = i+dr, j+dc
                    while 0 <= r < n and 0 <= c < n:
                        if (r, c) == (kr, kc):
                            print(f"Success R in row:{i} , col{j}")
                            return
                        if board[r][c] != '.':
                            break
                        r += dr
                        c += dc

            # Bishop
            if piece == "B":
                for dr, dc in directions_bishop:
                    r, c = i+dr, j+dc
                    while 0 <= r < n and 0 <= c < n:
                        if (r, c) == (kr, kc):
                            print(f"Success B in row:{i} , col{j}")
                            return
                        if board[r][c] != '.':
                            break
                        r += dr
                        c += dc

            # Queen
            if piece == "Q":
                for dr, dc in directions_rook + directions_bishop:
                    r, c = i+dr, j+dc
                    while 0 <= r < n and 0 <= c < n:
                        if (r, c) == (kr, kc):
                            print(f"Success Q in row:{i} , col{j}")
                            return
                        if board[r][c] != '.':
                            break
                        r += dr
                        c += dc

    print("Fail")