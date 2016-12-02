import random, copy, sys, pygame
from pygame.locals import *
class Gui:

    def __init__ (self):
        global FPS, BOARDWIDTH, BOARDHEIGHT, SPACESIZE, FPSCLOCK, WINDOWWIDTH, WINDOWWIDTH
        global XMARGIN, YMARGIN, BRIGHTBLUE, WHITE, BGCOLOR, TEXTCOLOR, RED, BLACK, EMPTY
        global playerOne, playerTwo
        # Game Variables
        BOARDWIDTH = 7  # how many spaces wide the board is
        BOARDHEIGHT = 6  # how many spaces tall the board is

        SPACESIZE = 50  # size of the tokens and individual board spaces in pixels

        FPS = 30  # frames per second to update the screen
        WINDOWWIDTH = 640  # width of the program's window, in pixels
        WINDOWHEIGHT = 480  # height in pixels

        XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * SPACESIZE) / 2)
        YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT * SPACESIZE) / 2)

        BRIGHTBLUE = (0, 50, 255)
        WHITE = (255, 255, 255)

        BGCOLOR = BRIGHTBLUE
        TEXTCOLOR = WHITE

        RED = 'red'
        BLACK = 'black'
        EMPTY = None
        playerOne = 'playerOne'
        playerTwo = 'playerTwo'

        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('Four in a Row')

        self.REDPILERECT = pygame.Rect(int(SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)
        self.BLACKPILERECT = pygame.Rect(WINDOWWIDTH - int(3 * SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE,
                                    SPACESIZE)
        REDTOKENIMG = pygame.image.load('4row_red.png')
        self.REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
        BLACKTOKENIMG = pygame.image.load('4row_black.png')
        self.BLACKTOKENIMG = pygame.transform.smoothscale(BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
        BOARDIMG = pygame.image.load('4row_board.png')
        self.BOARDIMG = pygame.transform.smoothscale(BOARDIMG, (SPACESIZE, SPACESIZE))

        self.HUMANWINNERIMG = pygame.image.load('4row_humanwinner.png')
        self.COMPUTERWINNERIMG = pygame.image.load('4row_humanwinner.png')
        self.TIEWINNERIMG = pygame.image.load('4row_tie.png')
        self.WINNERRECT = self.HUMANWINNERIMG.get_rect()
        self.WINNERRECT.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

        self.ARROWIMG = pygame.image.load('4row_arrow.png')
        self.ARROWRECT = self.ARROWIMG.get_rect()
        self.ARROWRECT.left = self.REDPILERECT.right + 10
        self.ARROWRECT.centery = self.REDPILERECT.centery


        # while True:
        #     runGame()
        #

    def runGame(self):


        # Set up a blank board data structure.
        mainBoard = self.getNewBoard()
        turn = playerOne
        showHelp = True
        while True: # main game loop
            if turn == playerOne:
                # Human player's turn.
                self.getPlayerMove(mainBoard, showHelp)
                if showHelp:
                    # turn off help arrow after the first move
                    showHelp = False
                if self.isWinner(mainBoard, RED):
                    winnerImg = self.HUMANWINNERIMG
                    break
                turn = playerTwo # switch to other player's turn
            else:
                if showHelp:
                    # turn off help arrow after the first move
                    showHelp = False
                if self.isWinner(mainBoard, RED):
                    winnerImg = self.HUMANWINNERIMG
                    break
                turn = playerOne # switch to other player's turn

            if self.isBoardFull(mainBoard):
                # A completely filled board means it's a tie.
                winnerImg = self.TIEWINNERIMG
                break

        while True:
            # Keep looping until player clicks the mouse or quits.
            self.drawBoard(mainBoard)
            self.DISPLAYSURF.blit(winnerImg, self.WINNERRECT)
            pygame.display.update()
            self.FPSCLOCK.tick()
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    return

    def mainLoop(self, board, winnerImg):
        self.drawBoard(board)
        self.DISPLAYSURF.blit(winnerImg, self.WINNERRECT)
        pygame.display.update()
        self.FPSCLOCK.tick()
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
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
                        if self.isValidMove(board, column):
                            self.animateDroppingToken(board, column, RED)
                            board[column][self.getLowestEmptySpace(board, column)] = RED
                            self.drawBoard(board)
                            pygame.display.update()
                            return column
                    tokenx, tokeny = None, None
                    draggingToken = False
            if tokenx != None and tokeny != None:
                self.drawBoard(board, {'x':tokenx - int(SPACESIZE / 2), 'y':tokeny - int(SPACESIZE / 2), 'color':RED})
            else:
                self.drawBoard(board)

            if isFirstMove:
                # Show the help arrow for the player's first move.
                self.DISPLAYSURF.blit(self.ARROWIMG, self.ARROWRECT)

            pygame.display.update()
            self.FPSCLOCK.tick()

    def drawBoard(self, board, extraToken=None):
        self.DISPLAYSURF.fill(BGCOLOR)

        # draw tokens
        spaceRect = pygame.Rect(0, 0, SPACESIZE, SPACESIZE)
        for y in range(BOARDWIDTH):
            for x in range(BOARDHEIGHT):
                spaceRect.topleft = (XMARGIN + (x * SPACESIZE), YMARGIN + (y * SPACESIZE))
                if board[x][y] == playerOne:
                    self.DISPLAYSURF.blit(self.REDTOKENIMG, spaceRect)
                elif board[x][y] == BLACK:
                    self.DISPLAYSURF.blit(self.BLACKTOKENIMG, spaceRect)

        # draw the extra token
        if extraToken != None:
            if extraToken['color'] == RED:
                self.DISPLAYSURF.blit(self.REDTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))
            elif extraToken['color'] == BLACK:
                self.DISPLAYSURF.blit(self.BLACKTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))

        # draw board over the tokens
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                spaceRect.topleft = (XMARGIN + (x * SPACESIZE), YMARGIN + (y * SPACESIZE))
                self.DISPLAYSURF.blit(self.BOARDIMG, spaceRect)

        # draw the red and black tokens off to the side
        self.DISPLAYSURF.blit(self.REDTOKENIMG, self.REDPILERECT) # red on the left
        self.DISPLAYSURF.blit(self.BLACKTOKENIMG, self.BLACKPILERECT) # black on the right

    def animateDroppingToken(self, board, column, color):
        x = XMARGIN + column * SPACESIZE
        y = YMARGIN - SPACESIZE
        dropSpeed = 1.0

        lowestEmptySpace = self.getLowestEmptySpace(board, column)
        while True:
            y += int(dropSpeed)
            dropSpeed += 0.5
            if int((y - YMARGIN) / SPACESIZE) >= lowestEmptySpace:
                return
            self.drawBoard(board, {'x':x, 'y':y, 'color':color})
            pygame.display.update()
            self.FPSCLOCK.tick()

    def isBoardFull(self, board):
        # Returns True if there are no empty spaces anywhere on the board.
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if board[x][y] == EMPTY:
                    return False
        return True

    def isValidMove(self, board, column):
        # Returns True if there is an empty space in the given column.
        # Otherwise returns False.
        if (board[5][column] == -1):
            return True
        return False

    def isWinner(self, board, tile):
        # check horizontal spaces
        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    return True
        # check vertical spaces
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    return True
        # check / diagonal spaces
        for x in range(BOARDWIDTH - 3):
            for y in range(3, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    return True
        # check \ diagonal spaces
        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    return True
        return False

    def getLowestEmptySpace(self, board, column):
        # Return the row number of the lowest empty row in the given column.
        for row in range(0, 5):
            if (board[row][column] == -1):
                return row
        return -1

    def getNewBoard(self):
        board = []
        for x in range(BOARDWIDTH):
            board.append([EMPTY] * BOARDHEIGHT)
        return board