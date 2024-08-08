# Menu.py

import pygame
import sys

import search_algorithms

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.image = pygame.image.load("imgs\menu.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        pygame.display.set_caption("Chesskoban Menu")
    
    def button (self, position, text, font, color):
        button_text = font.render(text, True, color)
        button_rect = button_text.get_rect(topleft=position)
        return button_text, button_rect


    def draw_menu(self, level_select, algorithm_select):
        self.screen.blit(self.image, (0,0))

        # título
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("Chesskoban", True, (0,0,0))
        self.screen.blit(text_title,(200,50))

        # níveis
        if level_select == 1:
            level_button1_text, level_button1_rect = self.button((180, 450), "Level 1", pygame.font.Font(None, 24), (255, 255, 255))
            level_button2_text, level_button2_rect = self.button((280, 450), "Level 2", pygame.font.Font(None, 24), (0, 0, 0))
            level_button3_text, level_button3_rect = self.button((380, 450), "Level 3", pygame.font.Font(None, 24), (0, 0, 0))
            self.screen.blit(level_button1_text, level_button1_rect)
            self.screen.blit(level_button2_text, level_button2_rect)
            self.screen.blit(level_button3_text, level_button3_rect)
        elif level_select == 2:
            level_button1_text, level_button1_rect = self.button((180, 450), "Level 1", pygame.font.Font(None, 24), (0, 0, 0))
            level_button2_text, level_button2_rect = self.button((280, 450), "Level 2", pygame.font.Font(None, 24), (255, 255, 255))
            level_button3_text, level_button3_rect = self.button((380, 450), "Level 3", pygame.font.Font(None, 24), (0, 0, 0))
            self.screen.blit(level_button1_text, level_button1_rect)
            self.screen.blit(level_button2_text, level_button2_rect)
            self.screen.blit(level_button3_text, level_button3_rect)
        elif level_select == 3:
            level_button1_text, level_button1_rect = self.button((180, 450), "Level 1", pygame.font.Font(None, 24), (0, 0, 0))
            level_button2_text, level_button2_rect = self.button((280, 450), "Level 2", pygame.font.Font(None, 24), (0, 0, 0))
            level_button3_text, level_button3_rect = self.button((380, 450), "Level 3", pygame.font.Font(None, 24), (255, 255, 255))
            self.screen.blit(level_button1_text, level_button1_rect)
            self.screen.blit(level_button2_text, level_button2_rect)
            self.screen.blit(level_button3_text, level_button3_rect)
        else:
            level_button1_text, level_button1_rect = self.button((180, 450), "Level 1", pygame.font.Font(None, 24), (0, 0, 0))
            level_button2_text, level_button2_rect = self.button((280, 450), "Level 2", pygame.font.Font(None, 24), (0, 0, 0))
            level_button3_text, level_button3_rect = self.button((380, 450), "Level 3", pygame.font.Font(None, 24), (0, 0, 0)) 
            self.screen.blit(level_button1_text, level_button1_rect)
            self.screen.blit(level_button2_text, level_button2_rect)
            self.screen.blit(level_button3_text, level_button3_rect)   

        # algoritmos   
        if algorithm_select == 1:
            algorithm_button1_text, algorithm_button1_rect = self.button((100, 500), "BFS", pygame.font.Font(None, 24), (255, 255, 255))
            algorithm_button2_text, algorithm_button2_rect = self.button((190, 500), "DFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button3_text, algorithm_button3_rect = self.button((280, 500), "Greedy Search", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button4_text, algorithm_button4_rect = self.button((440, 500), "A* Algorithm", pygame.font.Font(None, 24), (0,0,0))
            self.screen.blit(algorithm_button1_text, algorithm_button1_rect)
            self.screen.blit(algorithm_button2_text, algorithm_button2_rect)
            self.screen.blit(algorithm_button3_text, algorithm_button3_rect)
            self.screen.blit(algorithm_button4_text, algorithm_button4_rect)
        elif algorithm_select == 2:
            algorithm_button1_text, algorithm_button1_rect = self.button((100, 500), "BFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button2_text, algorithm_button2_rect = self.button((190, 500), "DFS", pygame.font.Font(None, 24), (255, 255, 255))
            algorithm_button3_text, algorithm_button3_rect = self.button((280, 500), "Greedy Search", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button4_text, algorithm_button4_rect = self.button((440, 500), "A* Algorithm", pygame.font.Font(None, 24), (0,0,0))
            self.screen.blit(algorithm_button1_text, algorithm_button1_rect)
            self.screen.blit(algorithm_button2_text, algorithm_button2_rect)
            self.screen.blit(algorithm_button3_text, algorithm_button3_rect)
            self.screen.blit(algorithm_button4_text, algorithm_button4_rect)
        elif algorithm_select == 3:
            algorithm_button1_text, algorithm_button1_rect = self.button((100, 500), "BFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button2_text, algorithm_button2_rect = self.button((190, 500), "DFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button3_text, algorithm_button3_rect = self.button((280, 500), "Greedy Search", pygame.font.Font(None, 24), (255, 255, 255))
            algorithm_button4_text, algorithm_button4_rect = self.button((440, 500), "A* Algorithm", pygame.font.Font(None, 24), (0,0,0))
            self.screen.blit(algorithm_button1_text, algorithm_button1_rect)
            self.screen.blit(algorithm_button2_text, algorithm_button2_rect)
            self.screen.blit(algorithm_button3_text, algorithm_button3_rect)
            self.screen.blit(algorithm_button4_text, algorithm_button4_rect)
        elif algorithm_select == 4:
            algorithm_button1_text, algorithm_button1_rect = self.button((100, 500), "BFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button2_text, algorithm_button2_rect = self.button((190, 500), "DFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button3_text, algorithm_button3_rect = self.button((280, 500), "Greedy Search", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button4_text, algorithm_button4_rect = self.button((440, 500), "A* Algorithm", pygame.font.Font(None, 24), (255, 255, 255))
            self.screen.blit(algorithm_button1_text, algorithm_button1_rect)
            self.screen.blit(algorithm_button2_text, algorithm_button2_rect)
            self.screen.blit(algorithm_button3_text, algorithm_button3_rect)
            self.screen.blit(algorithm_button4_text, algorithm_button4_rect)
        else:
            algorithm_button1_text, algorithm_button1_rect = self.button((100, 500), "BFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button2_text, algorithm_button2_rect = self.button((190, 500), "DFS", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button3_text, algorithm_button3_rect = self.button((280, 500), "Greedy Search", pygame.font.Font(None, 24), (0,0,0))
            algorithm_button4_text, algorithm_button4_rect = self.button((440, 500), "A* Algorithm", pygame.font.Font(None, 24), (0,0,0))
            self.screen.blit(algorithm_button1_text, algorithm_button1_rect)
            self.screen.blit(algorithm_button2_text, algorithm_button2_rect)
            self.screen.blit(algorithm_button3_text, algorithm_button3_rect)
            self.screen.blit(algorithm_button4_text, algorithm_button4_rect)

        # start game
        start_button_text, start_button_rect = self.button((245, 150), "Start Game", pygame.font.Font(None, 36), (0, 0, 0))
        self.screen.blit(start_button_text, start_button_rect)


        return level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect

    def draw_pop_up(self, text):
        font_title = pygame.font.Font(None, 25)
        text_title = font_title.render(text, True, (0,0,0))
        self.screen.blit(text_title,(230,182))

    def run(self, level_select, algorithm_select):
        self.level_select = level_select
        self.algorithm_select = algorithm_select
        level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)
        while True:
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if level_button1_rect.collidepoint(mouse_position):
                       self.level_select = 1
                       level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)
                    elif level_button2_rect.collidepoint(mouse_position):
                       self.level_select = 2
                       level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)
                    elif level_button3_rect.collidepoint(mouse_position):
                       self.level_select = 3
                       level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)
                    elif algorithm_button1_rect.collidepoint(mouse_position):
                        self.algorithm_select = 1
                        level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)
                    elif algorithm_button2_rect.collidepoint(mouse_position):
                        self.algorithm_select = 2
                        level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)
                    elif algorithm_button3_rect.collidepoint(mouse_position):
                        self.algorithm_select = 3
                        level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)
                    elif algorithm_button4_rect.collidepoint(mouse_position):
                        self.algorithm_select = 4
                        level_button1_rect, level_button2_rect, level_button3_rect, algorithm_button1_rect, algorithm_button2_rect, algorithm_button3_rect, algorithm_button4_rect, start_button_rect = self.draw_menu(self.level_select, self.algorithm_select)    
                    elif start_button_rect.collidepoint(mouse_position):
                        if self.level_select == 1 and self.algorithm_select > 0:
                           return True, self.level_select, self.algorithm_select
                        elif self.level_select == 2 and self.algorithm_select > 0:
                           return True, self.level_select, self.algorithm_select
                        elif self.level_select == 3 and self.algorithm_select > 0:
                           return True, self.level_select, self.algorithm_select
                        elif self.level_select == 0 and self.algorithm_select == 0:
                           self.draw_pop_up("Please select a level and an algorithm")
                        elif self.level_select == 0 and self.algorithm_select > 0:
                            self.draw_pop_up("Please select a level")
                        elif self.level_select > 0 and self.algorithm_select == 0:
                            self.draw_pop_up("Please select an algorithm")

            pygame.display.update()      
