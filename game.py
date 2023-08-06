# game class
# contains a board and a list of players
import Screen
from holes import create_holes
import simulation
import pygame
from random import randint
import time
import sys
depth = 0

pygame.font.init()
font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("bahnschrift", 40)
font2 = pygame.font.SysFont("comicsans", 72)
font3 = pygame.font.SysFont("comicsans", 20)
font4 = pygame.font.SysFont("comicsans", 20)


PIT_WIDTH = 100
PADDING = 20
class game:
    def __init__(self, board_size, pit_count):
        self.game_board = simulation.board(board_size, pit_count)
        Screen.player_score = [0, 0]
        self.current_player = 0


    def switchPlayer(self):
        '''
      moves to the next player
      '''
        self.current_player = (self.current_player + 1) % 2

    def updateScore(self, score):
        '''
      update scores of the current player
      '''

        Screen.player_score[self.current_player] = Screen.player_score[self.current_player] + score

    def isGame(self):
        '''
      returns True is the game has not reached the end
      returns False otherwise
      '''
        if self.game_board.isHalfEmpty():
            return False
        else:
            return True

    def getCurrentWinner(self):
        '''
      get who leads currently
      this method will return the winning player once called after the game is over
      '''
        return max(range(2), key=Screen.player_score.__getitem__)

    def Naiveplay2(self):
        '''
      play the game
      heuristics: select a random pit
      '''
        # choosing a pit
        time.sleep(0.5)
        pits = self.game_board.generateOptions(self.current_player)
        pit = pits[randint(0, len(pits)-1)]

        # make moves and update score
        score = self.game_board.move(pit)
        self.updateScore(score)
        self.switchPlayer()

    def UserPlay(self,pit):
        '''
      play the game
      heuristics: move from the user selected pit
      '''

        # make moves and update score
        score = self.game_board.move(pit)
        self.updateScore(score)
        self.switchPlayer()

    def ModifiedMinMax(self, board, limit, player, checker=0):
        global depth
        depth = depth + 1
        '''
      a recursive min-max function
      the function changes min/max utility based on the player passed
      the algorithm is modified such that the selection is made based on maximizing one score and minimizing a different score at each step
      '''

        # if the board is half empty the game is over
        if board.isHalfEmpty():
            return 0

        max_score = float("-inf")
        max_move = 0
        moves = board.generateOptions(player)
        # isCloneMove = True

        # check if the game state is in the level just above the limit in the min max tree
        # only check for maximum profit of the current player and return the best move
        if ((depth == (limit - 1)) or ((depth == limit) and (limit == 1))):
            for move_option in moves:

                new_board = board.clone()
                new_board_score = new_board.move2(move_option)

                if new_board_score > max_score:
                    max_score = new_board_score
                    max_move = move_option

                    # on any depth other than limit - 1 recursively call the function and get the best score of the opponent in the resulting stage of the current move
        # calculate the ratio of the addition to current player score by the move, to best potential addition to the opponent score of the resulting game state by the move
        # choose the move with maximum ratio
        else:
            max_ratio = float("-inf")
            for move_option in moves:
                new_board = board.clone()
                new_player = (player + 1) % 2
                score = new_board.move2(move_option)
                opponent_score = self.ModifiedMinMax(new_board, limit, new_player, depth)

                if opponent_score != 0:
                    if float(score / opponent_score) > max_ratio:
                        max_score = score
                        max_ratio = float(score / opponent_score)
                        max_move = move_option
                else:
                    max_score = score
                    max_move = move_option

        if checker == 1:
            return max_move
        else:
            return max_score

    def MinMaxplay(self, limit):
        '''
      plays the game based on modified min max strategy
      since the entire tree traversal is not optimal, a depth limit is provided
      '''
        global depth

        # choosing a pit
        pit = self.ModifiedMinMax(self.game_board, limit, self.current_player, 1)
        depth = depth - 1
        # make moves and update score
        score = self.game_board.move(pit)
        self.updateScore(score)
        self.switchPlayer()

    def drawText(self, text, color, rect, font, aa=False, bkg=None):
        print(rect)
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            Screen.screen.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

    def __main__(self):
        flagMain = 1
        isGame = True

        Screen.initialize()
        pygame.font.init()
        Screen.screen = pygame.display.set_mode((1000, 580))
        pygame.display.set_caption("Gebeta")
        Screen.screen.fill((0,0,0))
        pygame.display.flip()

        while isGame & self.isGame():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    isGame = False

            # clearing Screen.screen before printing boards
            if flagMain == 1:

                flag = 1
                while flag:
                    Screen.screen.fill((0, 0, 0))
                    bg = pygame.image.load("board.png").convert()
                    Screen.screen.blit(bg, (0, 0))
                    pygame.display.flip()
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            isGame = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            
                            flag = 0

                pygame.display.flip()
            bg = pygame.image.load("bg.jpg").convert()
            Screen.screen.blit(bg, (0, 0))
            pygame.display.flip()
            create_holes(Screen.screen)
            flagMain = 0

            size = int(self.game_board.board_size / 2)
            
            # displaying board 0
            new_list = self.game_board.board_list[::-1]
            temp_list = new_list[:size]

            for i in range(size):
                text = font.render(str(temp_list[i]), 1, (0, 0, 0))
                Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 180))

            # displaying board 1
            temp_list = self.game_board.board_list[:size]
            for i in range(size):
                text = font.render(str(temp_list[i]), 1, (0, 0, 0))
                Screen.screen.blit(text, (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING + 40, 320))

            text = font.render(
                str(Screen.player_score[0]), 1, (0, 0, 0))
            Screen.screen.blit(text, (7*PIT_WIDTH + 8*PADDING + 40, 250))

            text = font.render(str(Screen.player_score[1]), 1,(0, 0, 0))
            Screen.screen.blit(text, (PADDING + 40, 250))

            pygame.display.flip()
            if self.current_player == 1:
                temp = "Computer's move, Click to proceed"
                text = font1.render(temp, 1, (255, 255, 255))
                Screen.screen.blit(text, (PIT_WIDTH + 2*PADDING, PADDING))

            else:
                temp = "Your move, click on a Hole"
                text = font1.render(temp, 1, (255, 255, 255))
                Screen.screen.blit(text, (PIT_WIDTH + 2*PADDING, PADDING))

            pygame.display.flip()

            mouseClick = False
            while not mouseClick:
                if self.current_player == 1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            isGame = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseClick = True

                if self.current_player == 0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            isGame = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()

                            pits = self.game_board.generateOptions(self.current_player)

                            flag = 0
                            for i in pits:
                                if pos[0] > (( i + 1 )*PIT_WIDTH + ( i + 2 )*PADDING) and pos[0] < (( i + 2 )*PIT_WIDTH + ( i + 2 )*PADDING) and pos[1] > 300 and pos[1] < 300 + PIT_WIDTH:
                                    flag = 1
                                    pit = i
                                    break
                            if flag:
                                mouseClick = True

            if self.current_player == 0 and isGame:
                self.UserPlay(pit)
            elif self.current_player == 1 and isGame:
                self.MinMaxplay(2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    isGame = False

        if self.getCurrentWinner() == 0:
            Screen.screen.fill((0,0,0))
            pygame.draw.rect(Screen.screen, (93, 121, 125), [50, 200, 600, 200], 5, 5)
            text = font2.render("YOU WIN!!!",1,(93, 121, 125))
            Screen.screen.blit(text, (95,275))
        else:
            Screen.screen.fill((0, 0, 0))
            pygame.draw.rect(Screen.screen, (93, 121, 125), [50, 200, 600, 200], 5, 5)
            text = font2.render("GAME OVER!", 1, (93, 121, 125))
            Screen.screen.blit(text, (95, 270))
        pygame.display.flip()
        while isGame:
            time.sleep(2)
            text = font.render("Press N to start, Press Q to exit",1,(90, 100, 25),(255,255,255))
            Screen.screen.blit(text,(40,450))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        isGame = False
                    isGame = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        isGame = False
                    if event.key == pygame.K_n:

                        newgame = game(12, 5)
                        newgame.__main__()

        pygame.quit()

