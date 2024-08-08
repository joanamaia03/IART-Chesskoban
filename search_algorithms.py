from collections import deque
from heapq import heappush, heappop

import board_state

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    def __lt__(self, other):
        return True

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
    
    def moves_until(self):
        if self.parent:
            return 0
        return 1 + self.parent.moves_until()
    
    def path(self):
        if not self.parent:
            return [self.state]
        else:
            return self.parent.path() + [self.state]

def moves(path):
    moves = []
    for i in range(1, len(path)):
        before = path[i-1]
        after = path[i]
        if before.player[0] > after.player[0]:
            moves.append(board_state.up)
        elif before.player[0] < after.player[0]:
            moves.append(board_state.down)
        elif before.player[1] > after.player[1]:
            moves.append(board_state.left)
        elif before.player[1] < after.player[1]:
            moves.append(board_state.right)
    return moves


class MinHeap:
    def __init__(self):
        self.elements = []
 
    def isEmpty(self):
        return len(self.elements) == 0
 
    def push(self, priority, element):
        heappush(self.elements, (priority, element))

    def pop(self):
        return heappop(self.elements)


def breadth_first_search(initial_state, goal_state_func, operators_func):
    root = TreeNode(initial_state)
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if goal_state_func(node.state):
            return node

        for state in operators_func(node.state):
            new_node = TreeNode(state, node)
            node.add_child(new_node)
            queue.append(new_node)
    
    return None

def depth_first_search(initial_state, goal_state_func, operators_func):
    root = TreeNode(initial_state)
    visited = set([initial_state])
    stack = [root]

    while stack:
        node = stack.pop()
        if goal_state_func(node.state):
            return node

        for state in operators_func(node.state):
            if state not in visited:
                new_node = TreeNode(state)
                node.add_child(new_node)
                stack.append(new_node)
                visited.add(state)
    
    return None


def eval(state):
    total = 0
    for black_knight in state.black_knights:
        ts = board_state.targets(state, black_knight)
        distance = 999
        for t in ts:
            for white_knight in state.white_knights:
                if white_knight == t:
                    distance = 0
                else:
                    d = abs(white_knight[0] - t[0]) + abs(white_knight[1] - t[1])
                    if d < distance:
                        distance = d
        total += distance
    return total

def greedy_search(initial_state, goal_state_func, operators_func, heuristic_func):
    root = TreeNode(initial_state)
    visited = set([initial_state])
    queue = MinHeap()
    queue.push(heuristic_func(root.state), root)

    while queue:
        node = queue.pop()[1]
        if goal_state_func(node.state):
            return node

        for state in operators_func(node.state):
            if state not in visited:
                new_node = TreeNode(state)
                node.add_child(new_node)
                queue.push(heuristic_func(new_node.state), new_node)
                visited.add(state)
    
    return None

def a_star_search(initial_state, goal_state_func, operators_func, heuristic_func):
    root = TreeNode(initial_state)
    visited = set([initial_state])
    queue = MinHeap()
    queue.push(heuristic_func(root.state), root)

    while queue:
        node = queue.pop()[1]
        if goal_state_func(node.state):
            return node

        for state in operators_func(node.state):
            if state not in visited:
                new_node = TreeNode(state)
                node.add_child(new_node)
                queue.push(new_node.moves_until() + heuristic_func(new_node.state), new_node)
                visited.add(state)
    
    return None
