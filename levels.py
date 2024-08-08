import board_state

def level1():
    tiles = [
        [False, False, False, False, False],
        [False, False, False, False, True],
        [True, True, True, True, True],
        [False, True, True, True, False],
        [False, True, True, True, False],
        [False, True, True, True, False]
    ]
    player = (4, 3)
    white_knights = [(3, 3), (4, 2)]
    black_knights = [(0, 4), (1, 0)]

    return board_state.BoardState(tiles, player, white_knights, black_knights)

def level2():
    tiles = [
            [False, False, False, False, False, False, False, False],
            [False, True, True, True, True, True, True, False],
            [False, True, True, True, True, False, True, False],
            [True, True, True, True, True, False, True, False],
            [True, True, False, True, True, False, True, False],
            [True, True, False, True, True, True, True, False],
            [True, True, True, True, False, False, False, False],
            [True, True, True, False, False, False, False, False],
            [False, False, True, False, False, False, False, False]
    ]
    player = (1, 6)
    white_knights = [(1, 5), (2, 6), (2, 3), (4, 1), (6, 1), (6, 2)]
    black_knights = [(0, 0), (3, 7), (4, 2), (5, 2), (6, 7), (8, 3)]

    return board_state.BoardState(tiles, player, white_knights, black_knights)

def level3():
    tiles = [
        [False, False, False, False, False, False, False, True, True, False],
        [False, False, False, True, True, True, False, True, False, False],
        [False, False, False, True, False, True, False, True, True, False],
        [False, False, False, True, False, True, True, True, True, False],
        [True, True, True, True, False, True, True, True, True, True],
        [False, False, True, True, True, True, True, True, False, False],
        [False, False, True, False, False, True, False, True, False, False],
        [False, False, True, True, True, True, False, True, True, False],
        [False, False, False, False, True, True, True, True, False, False],
        [False, False, False, False, True, True, False, False, False, False]
    ]
    player = (5, 7)
    white_knights = [(2, 5), (3, 7), (4, 6), (5, 4), (7, 7)]
    black_knights = [(0, 9), (1, 8), (3, 0), (7, 9), (9, 3)]

    return board_state.BoardState(tiles, player, white_knights, black_knights)

levels = [0, level1(), level2(), level3()]
