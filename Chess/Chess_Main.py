"""
dedomena apo xristi tha ta elenxi kai tha ta stelni
"""
import pygame as pg
from Chess import Chess_Engine_ver1

WIDTH = HEIGHT = 720
DIMENSION = 8
SQR_SIZE = HEIGHT // DIMENSION
MAX_FPS = 30
IMAGES= {}
#FORTOSI EIKONON KALO EINAI MONO MIA FORA GT THA VARINI TO GAME KAI THA KOLAI
'''
tha fortoso se dikotou method kai tha anevi mono mia fora stin mnimi
'''
def load_Images():
    poulia = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
    for poulias in poulia:
        IMAGES[poulias] = pg.transform.scale(pg.image.load("images/" + poulias + ".png"),(SQR_SIZE,SQR_SIZE))

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    '''elenxos ton theseon meso tou def init'''
    gamestate = Chess_Engine_ver1.GameState()
    '''print (gamestate.board)'''
    validMoves = gamestate.getValidMoves()
    moveMade = False #flag gia kinisis pou mpori na gini gia na min varini pe poli epexergasia to py
    load_Images()  #mono afrti tin fora tha ta fortoso
    running = True
    sqr_Selected = () # apothikeusi telefteas kinisis paixti
    pClicks = [] #tha apothikevi ta klik tou paixti mesa se 2 tuple

    while running:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                running = False
            #pontiki elenxos

            elif i.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                col = location[0]//SQR_SIZE
                row = location[1]//SQR_SIZE
                if sqr_Selected == (row, col):#elenxos gia to ean exei idi kani ekini tin kinisi
                    sqr_Selected = (row, col)
                    pClicks = [] #katharismo timon click
                else:
                    sqr_Selected = (row, col)
                    pClicks.append(sqr_Selected)
                if len(pClicks) == 2: #meta to 2 click
                    kinisi = Chess_Engine_ver1.Kinisis(pClicks[0], pClicks[1], gamestate.board)
                    print(kinisi.getChessNotes())#debug gia na tsekarw an einai entaxi
                    if kinisi in validMoves:
                        gamestate.kaneKinisi(kinisi)
                        moveMade = True
                    sqr_Selected = () #reset sta click you paixti gia na mpune kainouries times
                    pClicks = []
            #pliktologio elenxos
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_b: #kanei piso tin kinisi otan patas to b
                     gamestate.undoKinisi()
                     moveMade = True
        if moveMade:
            validMoves =gamestate.getValidMoves() #vriski tis epitreptes kinisis mono afou gini mia epitrepti kinisi
        draw_State(screen, gamestate)
        clock.tick(MAX_FPS)
        pg.display.flip()

"""
zwgrafisi ta grafika sto paixnidi tetragona kai poulia ktlp
"""
def draw_State (screen,gamestate):
    draw_Board(screen) #zografisi ta tetragona
    draw_Poulia(screen, gamestate.board) #zpgrafise ta poulia panw apo ta tetragona

"""
zwgrafise ta tetragona
"""
def draw_Board(screen):
    colors = [pg.Color("darkgreen"), pg.Color("bisque")]
    for row in range(DIMENSION):
        for collum in range(DIMENSION):
            color=colors[((row+collum) % 2)]
            pg.draw.rect(screen, color, pg.Rect(collum*SQR_SIZE, row*SQR_SIZE, SQR_SIZE, SQR_SIZE))



"""
zografise ta poulia stin kenoyria topothesia
"""
def draw_Poulia(screen,board):
    for row in range(DIMENSION):
        for collum in range (DIMENSION):
            poulia = board[row][collum]
            if poulia != "--": #ean den einai keno tote zografise
               screen.blit(IMAGES[poulia], pg.Rect(collum*SQR_SIZE, row*SQR_SIZE, SQR_SIZE, SQR_SIZE))




'''
wtf is going on here
'''

if __name__== "__main__":
    main()


