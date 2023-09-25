from os import environ
import sys

import pygame

from big_eater_cursor import ClickableSprite

# Environments 
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Colours
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 100)

# Window Details
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1850

class BigEater():
    def main():
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(WHITE)

        # cursor
        # sprite = ClickableSprite(pygame.Surface((100, 100)), 50, 50, BigEater.on_click)
        # group = pygame.sprite.GroupSingle(sprite=sprite)
        # events =  pygame.event.get()
        while True:
            BigEater.drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    BigEater.drawCircle()
                    pygame.display.update()
            
            pygame.display.update()

    def drawGrid():
        blockSize = 20 #Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
 
    def get_mouse_position():
        position = pygame.mouse.get_pos()
        return position

    def drawCircle():
        position=BigEater.get_mouse_position()
        pygame.draw.circle(SCREEN, BLUE, position, 5)

        


if __name__ == "__main__":
    BigEater.main()