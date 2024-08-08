import itertools

class BoardState:
    
    def __init__(self, tiles, player, white_knights, black_knights):
        self.tiles = tiles
        self.height = len(self.tiles)
        self.width = len(self.tiles[0])

        self.player = player
        self.white_knights = set(white_knights)
        self.black_knights = set(black_knights)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    
    def __hash__(self):
        return hash((self.player, tuple(self.white_knights)))
    
    def __str__(self):
        return str(self.white_knights)
    
    def is_tile(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= self.height or pos[1] >= self.width:
            return False
        return self.tiles[pos[0]][pos[1]]
    

def up(state):
    new_player = (state.player[0] - 1, state.player[1])
    if not state.is_tile(new_player):
        return None
    
    new_white_knights = []
    for white_knight in state.white_knights:
        if new_player == white_knight:
            new_white_knight = (new_player[0] - 1, new_player[1])
            if not state.is_tile(new_white_knight) or new_white_knight in state.white_knights:
                return None
            new_white_knights.append(new_white_knight)
        else:
            new_white_knights.append(white_knight)
    
    return BoardState(state.tiles, new_player, new_white_knights, state.black_knights)

def right(state):
    new_player = (state.player[0], state.player[1] + 1)
    if not state.is_tile(new_player):
        return None
    
    new_white_knights = []
    for white_knight in state.white_knights:
        if new_player == white_knight:
            new_white_knight = (new_player[0], new_player[1] + 1)
            if not state.is_tile(new_white_knight) or new_white_knight in state.white_knights:
                return None
            new_white_knights.append(new_white_knight)
        else:
            new_white_knights.append(white_knight)
    
    return BoardState(state.tiles, new_player, new_white_knights, state.black_knights)

def down(state):
    new_player = (state.player[0] + 1, state.player[1])
    if not state.is_tile(new_player):
        return None
    
    new_white_knights = []
    for white_knight in state.white_knights:
        if new_player == white_knight:
            new_white_knight = (new_player[0] + 1, new_player[1])
            if not state.is_tile(new_white_knight) or new_white_knight in state.white_knights:
                return None
            new_white_knights.append(new_white_knight)
        else:
            new_white_knights.append(white_knight)
    
    return BoardState(state.tiles, new_player, new_white_knights, state.black_knights)

def left(state):
    new_player = (state.player[0], state.player[1] - 1)
    if not state.is_tile(new_player):
        return None
    
    new_white_knights = []
    for white_knight in state.white_knights:
        if new_player == white_knight:
            new_white_knight = (new_player[0], new_player[1] - 1)
            if not state.is_tile(new_white_knight) or new_white_knight in state.white_knights:
                return None
            new_white_knights.append(new_white_knight)
        else:
            new_white_knights.append(white_knight)
    
    return BoardState(state.tiles, new_player, new_white_knights, state.black_knights)
    
def children(state):
    new_states = []
    if up(state):
        new_states.append(up(state))
    if right(state):
        new_states.append(right(state))
    if down(state):
        new_states.append(down(state))
    if left(state):
        new_states.append(left(state))
    return new_states


def targets(state, black_knight):
    ts = []
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    for i in range(8):
        t = (black_knight[0] + dx[i], black_knight[1] + dy[i])
        if state.is_tile(t):
            ts.append(t)
    return ts

def is_goal(state):
    target_pools = []
    for black_knight in state.black_knights:
        target_pools.append(targets(state, black_knight))

    for potential in itertools.product(*target_pools):
        solution = set(potential)
        if len(solution) == len(potential) and state.white_knights == solution:
            return True

    return False  
