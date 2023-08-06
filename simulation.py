import copy
import sys
import pygame
import Screen
import time

from holes import create_holes
# from game import screen
pygame.font.init()
Screen.initialize()
font = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 72)

PIT_WIDTH = 100
PADDING = 20
class board:
    def __init__(self, board_size, pit_count):
        self.board_list = [pit_count] * board_size
        self.board_size = board_size
        self.pit_count = pit_count

    def isHalfEmpty(self):
        '''
        checks if one size of the board is empty or not
        useful in determining if the game is over or not
        '''

        # check if any one side of the board leaves the player with no option to choose from
        return self.generateOptions(0) == [] or self.generateOptions(1) == []

    def clone(self):
        '''
        clones the original board
        '''

        new = board(len(self.board_list), self.pit_count)
        new.board_list = copy.copy(self.board_list)
        return new

    def generateOptions(self, current_player):
        '''
        returns a list of indices the current player is eligable to choose from
        the half the board returned represnts the side of the current player
        '''

        selection = []
        side = []
        size = int(len(self.board_list) / 2)

        if current_player == 0:
            for index in range(0, size):
                if self.board_list[index] != 0:
                    selection.append(index)
        else:
            for index in range(size, size * 2):
                if self.board_list[index] != 0:
                    selection.append(index)

        return selection

    def nextPit(self, pit):
        return (pit + 1) % self.board_size

    def move(self, start):
        '''
        the game is played beginning from the start index
        the move ends when there the next pit is empty
        the move function returns a score
        '''

        # scores, get coins to move around and set the start pit to zero coins
        score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    isGame = False
        coins = self.board_list[start]

        # Screen.screen.fill((0, 0, 0))
        bg = pygame.image.load("bg.jpg").convert()
        Screen.screen.blit(bg, (0, 0))
        


        create_holes(Screen.screen)

        size = int(self.board_size / 2)

        # displaying board 0
        new_list = self.board_list[::-1]
        temp_list = new_list[:size]

        for i in range(size):
            text = font.render(str(temp_list[i]), 1, (0, 0, 0))
            Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 180))

        # displaying board 1
        temp_list = self.board_list[:size]
        for i in range(size):
            text = font.render(str(temp_list[i]), 1, (0, 0, 0))
            Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 320))

        text = font.render(
            str(Screen.player_score[0]), 1, (0, 0, 0))
        Screen.screen.blit(text, (7*PIT_WIDTH + 8*PADDING + 40, 250))

        text = font.render(str(Screen.player_score[1]), 1,(0, 0, 0))
        Screen.screen.blit(text, (PADDING + 40, 250))

        # Starting pit color changed to golden
        text = font.render(str(self.board_list[start]), 1, (218, 165, 32))
        size = self.board_size

        if start < size // 2:
            x = ( start + 1 )*PIT_WIDTH + ( start + 2 )*PADDING + 40
            # x = 80 * start + 42
            y = 320
        else:
            x = ( size - start )*PIT_WIDTH + ( size - start + 1 )*PADDING + 40
            # x = 80 * (size - start - 1) + 42
            y = 180
        Screen.screen.blit(text, (x, y))

        pygame.display.update()

        self.board_list[start] = 0
        time.sleep(0.5)
        text = font.render(str(self.board_list[start]), 1, (218, 165, 32))
        size = self.board_size
        if start < size // 2:
            x = ( start + 1 )*PIT_WIDTH + ( start + 2 )*PADDING + 40
            # x = 80 * start + 42
            y = 320
            color = (160, 160, 160)
        else:
            x = ( size - start )*PIT_WIDTH + ( size - start + 1 )*PADDING + 40
            # x = 80 * (size - start - 1) + 42
            y = 180
            color = (0, 153, 153)
        
        Screen.screen.blit(text, (x, y))
        pygame.display.update()
        # move the coins to corresponding pits
        for coin in range(coins):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        isGame = False
            start = self.nextPit(start)

            self.board_list[start] = self.board_list[start] + 1
            time.sleep(0.35)
            create_holes(Screen.screen)

            size = int(self.board_size / 2)

            # displaying board 0
            new_list = self.board_list[::-1]
            temp_list = new_list[:size]

            for i in range(size):
                text = font.render(str(temp_list[i]), 1, (0, 0, 0))
                Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 180))

            # displaying board 1
            temp_list = self.board_list[:size]
            for i in range(size):
                text = font.render(str(temp_list[i]), 1, (0, 0, 0))
                Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 320))

            text = font.render(
                str(Screen.player_score[0]), 1, (0, 0, 0))
            Screen.screen.blit(text, (7*PIT_WIDTH + 8*PADDING + 40, 250))

            text = font.render(str(Screen.player_score[1]), 1,(0, 0, 0))
            Screen.screen.blit(text, (PADDING + 40, 250))

            text = font.render(str(self.board_list[start]), 1, (255, 255, 255))
            size = self.board_size

            if start < size // 2:
                x = ( start + 1 )*PIT_WIDTH + ( start + 2 )*PADDING + 40
                # x = 80 * start + 42
                y = 320
            else:
                x = ( size - start )*PIT_WIDTH + ( size - start + 1 )*PADDING + 40
                # x = 80 * (size - start - 1) + 42
                y = 180
            Screen.screen.blit(text, (x, y))

            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    isGame = False
        # next_pit = self.nextPit(start)
        next_pit = start

        time.sleep(0.5)
        if self.board_list[next_pit] == 1:

            text = font.render("",1,(93, 121, 125))
            Screen.screen.blit(text, (PADDING, 500))
            # (12 + 6)%12
            # score_pit = self.nextPit(next_pit)
            score_pit = (self.board_size - 1) - next_pit
            text = font.render(str(self.board_list[score_pit]),1,(0,255,0))
            size = self.board_size
            
            if score_pit < size // 2:
                x = ( score_pit + 1 )*PIT_WIDTH + ( score_pit + 2 )*PADDING + 40
                # x = 80 * start + 42
                y = 320
            else:
                x = ( size - score_pit )*PIT_WIDTH + ( size - score_pit + 1 )*PADDING + 40
                # x = 80 * (size - start - 1) + 42
                y = 180
            Screen.screen.blit(text,(x,y))
            text = font.render(str(self.board_list[next_pit]),1,(255,0,0))
            size = self.board_size
            
            if next_pit < size // 2:
                x = ( next_pit + 1 )*PIT_WIDTH + ( next_pit + 2 )*PADDING + 40
                # x = 80 * start + 42
                y = 320
            else:
                x = ( size - next_pit )*PIT_WIDTH + ( size - next_pit + 1 )*PADDING + 40
                # x = 80 * (size - start - 1) + 42
                y = 180
            Screen.screen.blit(text,(x,y))
            pygame.display.update()
            time.sleep(3)
            # score_pit = self.nextPit(next_pit)
            score = self.board_list[score_pit]

            self.board_list[score_pit] = 0
            

            create_holes(Screen.screen)


            size = int(self.board_size / 2)

            # displaying board 0
            new_list = self.board_list[::-1]
            temp_list = new_list[:size]

            for i in range(size):
                text = font.render(str(temp_list[i]), 1, (0, 0, 0))
                Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 180))

            # displaying board 1
            temp_list = self.board_list[:size]
            for i in range(size):
                text = font.render(str(temp_list[i]), 1, (0, 0, 0))
                Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 320))

            text = font.render(
                str(Screen.player_score[0]), 1, (0, 0, 0))
            Screen.screen.blit(text, (7*PIT_WIDTH + 8*PADDING + 40, 250))

            text = font.render(str(Screen.player_score[1]), 1,(0, 0, 0))
            Screen.screen.blit(text, (PADDING + 40, 250))

            text = font.render(str(self.board_list[score_pit]), 1, (255, 0, 0))
            size = self.board_size
            if start < size // 2:
                x = ( start + 1 )*PIT_WIDTH + ( start + 2 )*PADDING + 40
                # x = 80 * start + 42
                y = 320
            else:
                x = ( size - start )*PIT_WIDTH + ( size - start + 1 )*PADDING + 40
                # x = 80 * (size - start - 1) + 42
                y = 180

            # if score_pit < size // 2:
            #     x = 80 * score_pit + 42
            #     y = 375
            # else:
            #     x = 80 * (size - score_pit - 1) + 42
            #     y = 275
            Screen.screen.blit(text, (x, y))


            pygame.display.update()

        else:
            score = self.move(next_pit)

        return score

    def move2(self, start):
        '''
        the game is played beginning from the start index
        the move ends when there the next pit is empty
        the move function returns a score
        '''
        # scores, get coins to move around and set the start pit to zero coins
        score = 0

        coins = self.board_list[start]
        self.board_list[start] = 0

        # move the coins to corresponding pits
        for coin in range(coins):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        isGame = False
            start = self.nextPit(start)
            start = self.nextPit(start)
            self.board_list[start] = self.board_list[start] + 1

        # next_pit = self.nextPit(start)
        next_pit = start

        # check if next pit after the move is empty or not
        # if empty the move is over, take the coin from the consecutive pit to return as score
        # if not empty, recursively move again starting from the next pit
        if self.board_list[next_pit] == 1:
            # score_pit = self.nextPit(next_pit)
            score_pit = (self.board_size - 1) - next_pit

            score = self.board_list[score_pit]

            self.board_list[score_pit] = 0

        else:
            score = self.move2(next_pit)

        return score