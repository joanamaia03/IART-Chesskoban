import pygame

import time

from Menu import Menu
import board_state
import levels
import graphics
import search_algorithms

MOVE_TIME = 0.1

pygame.init()
menu = Menu(600,600)
level_select = 0
algorithm_select = 0
state, level_select, algorithm_select = menu.run(level_select, algorithm_select)

board = levels.levels[level_select]

screen = graphics.board_init(board)
graphics.draw(screen, board)
pygame.display.flip()
time.sleep(MOVE_TIME)

# ai gameplay
if algorithm_select == 1:
    start_time = time.time()
    goal = search_algorithms.breadth_first_search(board, board_state.is_goal, board_state.children)
elif algorithm_select == 2:
    start_time = time.time()
    goal = search_algorithms.depth_first_search(board, board_state.is_goal, board_state.children)
elif algorithm_select == 3:
    start_time = time.time()
    goal = search_algorithms.greedy_search(board, board_state.is_goal, board_state.children, search_algorithms.eval)
elif algorithm_select == 4:
    start_time = time.time()
    goal = search_algorithms.a_star_search(board, board_state.is_goal, board_state.children, search_algorithms.eval)  

ms = search_algorithms.moves(goal.path())
m = 0

#state = True
while state:    
    event = pygame.event.wait(int(MOVE_TIME * 1000))
    if event.type == pygame.QUIT:
        state = False
    elif event.type == pygame.NOEVENT:
        board = ms[m](board)
        m += 1
        graphics.draw(screen, board)
        pygame.display.flip()
        time.sleep(MOVE_TIME)
    
    if board_state.is_goal(board):
        state = False

end_time = time.time()
print(f"Time:{end_time-start_time:.3f}")
print("Moves: " + str(len(ms)))

# manual gameplay
# state = True
# while state != False:
#     event = pygame.event.wait()
#     if event.type == pygame.QUIT:
#         state = False
#     elif event.type == pygame.KEYDOWN:
#         match event.key:
#             case pygame.K_UP:
#                 new_board = board_state.up(board)
#             case pygame.K_RIGHT:
#                 new_board = board_state.right(board)
#             case pygame.K_DOWN:
#                 new_board = board_state.down(board)
#             case pygame.K_LEFT:
#                 new_board = board_state.left(board)
#             case pygame.K_r:
#                 new_board = levels.levels[level]
#             case _:
#                 continue
#         if new_board:
#             board = new_board
#             graphics.draw(screen, board)
#             pygame.display.flip()
    
#     if board_state.is_goal(board):
#         state = False

pygame.quit()
