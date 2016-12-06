import random, copy, sys, pygame
from pygame.locals import *
from threading import Thread

class Gui(Thread):

    def __init__ (self, height, width, playerNum = 0):
        global FPS, BOARDWIDTH, BOARDHEIGHT, SPACESIZE, FPSCLOCK, WINDOWWIDTH, WINDOWWIDTH
        global XMARGIN, YMARGIN, BRIGHTBLUE, WHITE, BGCOLOR, TEXTCOLOR, RED, BLACK, EMPTY
        global playerOne, playerTwo, bg, playerNumber

        # Game Variables
        BOARDWIDTH = width  # how many spaces wide the board is
        BOARDHEIGHT = height  # how many spaces tall the board is

        playerNumber = playerNum

        SPACESIZE = 50  # size of the tokens and individual board spaces in pixels

        FPS = 30  # frames per second to update the screen
        WINDOWWIDTH = 640  # width of the program's window, in pixels
        WINDOWHEIGHT = 480  # height in pixels

        XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * SPACESIZE) / 2)
        YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT * SPACESIZE) / 2)

        BRIGHTBLUE = (0, 1, 255)
        WHITE = (255, 255, 255)

        BGCOLOR = BRIGHTBLUE
        TEXTCOLOR = WHITE

        self.bg = pygame.image.load('background.jpg')


        RED = 'red'
        BLACK = 'black'
        EMPTY = -1
        playerOne = 1
        playerTwo = 0

        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('Net Four')

        self.REDPILERECT = pygame.Rect(int(SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)
        self.BLACKPILERECT = pygame.Rect(WINDOWWIDTH - int(3 * SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE,
                                    SPACESIZE)
        if playerNum == 0:
            REDTOKENIMG = pygame.image.load('red.png')
            self.REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
            BLACKTOKENIMG = pygame.image.load('blue.png')
            self.BLACKTOKENIMG = pygame.transform.smoothscale(BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
        else:
            REDTOKENIMG = pygame.image.load('blue.png')
            self.REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
            BLACKTOKENIMG = pygame.image.load('red.png')
            self.BLACKTOKENIMG = pygame.transform.smoothscale(BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
        BOARDIMG = pygame.image.load('grid.png')
        self.BOARDIMG = pygame.transform.smoothscale(BOARDIMG, (SPACESIZE, SPACESIZE))

        self.PLAYERONEWIN = pygame.image.load('player_one_win.png')
        self.PLAYERTWOWIN = pygame.image.load('player_two_win.png')
        self.TIEWINNERIMG = pygame.image.load('4row_tie.png')
        self.WINNERRECT = self.PLAYERONEWIN.get_rect()
        self.WINNERRECT.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

        self.ARROWIMG = pygame.image.load('4row_arrow.png')
        self.ARROWRECT = self.ARROWIMG.get_rect()
        self.ARROWRECT.left = self.REDPILERECT.right + 10
        self.ARROWRECT.centery = self.REDPILERECT.centery


    def mainLoop(self, board, winningPlayer):
        print winningPlayer
        while True:
            self.drawBoard(board)
            if winningPlayer == 0:
                self.DISPLAYSURF.blit(self.PLAYERONEWIN, self.WINNERRECT)
            elif winningPlayer == 1:
                self.DISPLAYSURF.blit(self.PLAYERTWOWIN, self.WINNERRECT)
            pygame.display.update()
            self.FPSCLOCK.tick()
            for event in pygame.event.get():  # event handling loop
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    # sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    pygame.quit()
                    # sys.exit()
                    return

    def animateNetworkMoving(self, board, column):
        x = self.BLACKPILERECT.left
        y = self.BLACKPILERECT.top
        speed = 1.0
        # moving the black tile up
        while y > (YMARGIN - SPACESIZE):
            y -= int(speed)
            speed += 0.5
            self.drawBoard(board, {'x':x, 'y':y, 'color':BLACK})
            pygame.display.update()
            self.FPSCLOCK.tick()
        # moving the black tile over
        y = YMARGIN - SPACESIZE
        speed = 1.0
        while x > (XMARGIN + column * SPACESIZE):
            x -= int(speed)
            speed += 0.5
            self.drawBoard(board, {'x':x, 'y':y, 'color':BLACK})
            pygame.display.update()
            self.FPSCLOCK.tick()
        # dropping the black tile
        self.animateDroppingToken(board, column, BLACK)

    def getPlayerMove(self, board, isFirstMove):
        draggingToken = False
        tokenx, tokeny = None, None
        while True:
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and not draggingToken and self.REDPILERECT.collidepoint(event.pos):
                    # start of dragging on red token pile.
                    draggingToken = True
                    tokenx, tokeny = event.pos
                elif event.type == MOUSEMOTION and draggingToken:
                    # update the position of the red token being dragged
                    tokenx, tokeny = event.pos
                elif event.type == MOUSEBUTTONUP and draggingToken:
                    # let go of the token being dragged
                    if tokeny < YMARGIN and tokenx > XMARGIN and tokenx < WINDOWWIDTH - XMARGIN:
                        # let go at the top of the screen.
                        column = int((tokenx - XMARGIN) / SPACESIZE)

                        # if self.check_full_col(board, column):
                        #    #  self.animateDroppingToken(board, column, RED)
                        #    # # board[column][self.isValidMove(board, column)] = RED
                        #    #  self.drawBoard(board)
                        #    #  pygame.display.update()

                        return column
                    tokenx, tokeny = None, None
                    draggingToken = False
            if tokenx != None and tokeny != None:
                if playerNumber == 0:
                    self.drawBoard(board, {'x':tokenx - int(SPACESIZE / 2), 'y':tokeny - int(SPACESIZE / 2), 'color':RED})
                elif playerNumber == 1:
                    self.drawBoard(board, {'x': tokenx - int(SPACESIZE / 2), 'y': tokeny - int(SPACESIZE / 2), 'color': BLACK})
            else:
                self.drawBoard(board)

            if isFirstMove:
                # Show the help arrow for the player's first move.
                self.DISPLAYSURF.blit(self.ARROWIMG, self.ARROWRECT)
            else:
                self.ARROWRECT.left = 1000

            pygame.display.update()
            self.FPSCLOCK.tick()

    def drawBoard(self, board, extraToken=None):
        # self.DISPLAYSURF.fill(BGCOLOR)
        self.DISPLAYSURF.blit(self.bg, (0, 0))
        # draw tokens
        spaceRect = pygame.Rect(0, 0, SPACESIZE, SPACESIZE)
        for y in range(0, BOARDWIDTH):
            for x in range(0, BOARDHEIGHT):
                spaceRect.topleft = (XMARGIN + (y * SPACESIZE), YMARGIN + ((5 - x) * SPACESIZE))
                #spaceRect.topleft = (YMARGIN + (y * SPACESIZE), XMARGIN + (x * SPACESIZE))
                # print "Board at: " + str(x) + ", " + str(y) + " = " + str(board[x][y])
                if playerNumber == 0:
                    if board[x][y] == playerTwo:
                        self.DISPLAYSURF.blit(self.REDTOKENIMG, spaceRect)
                    elif board[x][y] == playerOne:
                        self.DISPLAYSURF.blit(self.BLACKTOKENIMG, spaceRect)
                elif playerNumber == 1:
                    if board[x][y] == playerOne:
                        self.DISPLAYSURF.blit(self.REDTOKENIMG, spaceRect)
                    elif board[x][y] == playerTwo:
                        self.DISPLAYSURF.blit(self.BLACKTOKENIMG, spaceRect)

        # draw the extra token
        if extraToken != None:
            if playerNumber == 0:
                if extraToken['color'] == RED:
                    self.DISPLAYSURF.blit(self.REDTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))
                elif extraToken['color'] == BLACK:
                    self.DISPLAYSURF.blit(self.BLACKTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))
            elif playerNumber == 1:
                if extraToken['color'] == BLACK:
                    self.DISPLAYSURF.blit(self.REDTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))
                elif extraToken['color'] == RED:
                    self.DISPLAYSURF.blit(self.BLACKTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))
        # draw board over the tokens
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                spaceRect.topleft = (XMARGIN + (x * SPACESIZE), YMARGIN + (y * SPACESIZE))
                self.DISPLAYSURF.blit(self.BOARDIMG, spaceRect)

        # draw the red and black tokens off to the side
        self.DISPLAYSURF.blit(self.REDTOKENIMG, self.REDPILERECT) # red on the left
        self.DISPLAYSURF.blit(self.BLACKTOKENIMG, self.BLACKPILERECT) # black on the right

    def animateDroppingToken(self, board, column, color, col):
        x = XMARGIN + column * SPACESIZE
        y = YMARGIN - SPACESIZE
        dropSpeed = 1.0

        lowestEmptySpace = col

        while True:
            y += int(dropSpeed)
            dropSpeed += 0.5
            if int((y - YMARGIN) / SPACESIZE) >= lowestEmptySpace:
                return
            self.drawBoard(board, {'x':x, 'y':y, 'color':color})
            pygame.display.update()
            self.FPSCLOCK.tick()

    def display_update(self):
        pygame.display.update()
