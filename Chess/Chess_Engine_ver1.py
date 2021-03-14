"""
database .plirofories gia ta dedomena sto game,kai pies einai i kinisis pou mpori na kanei kai na apothikevi tis kinissis pou eginan
"""
class GameState():
    def __init__(self):
        #8x8 2d diastasis exoume dio xaraktires  to w einai gia leuka kia to b gia maura to deutero grama einai gia ton tipo apo to pouli
        #"--" == gia ta kena pou exoume

        self.board=[
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],

        ]
        self.white_to_move =True
        self.move_log =[]

    def kaneKinisi(self, kinisi):
        self.board[kinisi.startRow][kinisi.startCol] = "--"
        self.board[kinisi.endRow][kinisi.endCol] = kinisi.pouliaKinisi
        self.move_log.append(kinisi)
        self.white_to_move = not self.white_to_move #allagi siras paixti

    def undoKinisi(self):
        if len(self.move_log) !=0:
            kinisi = self.move_log.pop()
            self.board[kinisi.startRow][kinisi.startCol] = kinisi.pouliaKinisi
            self.board[kinisi.endRow][kinisi.endCol] = kinisi.pouliaCapture
            self.white_to_move = not self.white_to_move  # allagi siras paixti

    def getValidMoves(self):
        return self.getAllPosMoves() #den kinati akoma ta checks pros ton king

    def getAllPosMoves(self):
        kinisis = [Kinisis((6, 4), (4, 4), self.board)]
        for r in range (len(self.board)): # to leng to board einai 8
            for c in range(len(self.board[r])):# ta colums stin sigekrimeni row
                sira = self.board[r][c][0]
                if (sira == 'w' and self.white_to_move) and (sira == 'b'and self.white_to_move): #tsekari to xrwma apo to pouli
                    poulia = self.board[r][c][1]
                    if poulia == 'P':
                        self.getThePawnMoves(r, c, kinisis)
                    elif  poulia == 'R':
                        self.getTheRookMoves(r, c, kinisis)
                    elif poulia == 'B':
                        self.getTheBishopMoves(r, c, kinisis)
                    elif poulia == 'N':
                        self.getTheKnightMoves(r, c, kinisis)
                    elif poulia == 'Q':
                        self.getTheQueenMoves(r, c, kinisis)
                    elif poulia == 'K':
                        self.getTheKingMoves(r, c, kinisis)
        return  kinisis

    def getThePawnMoves(self, r, c, kinisis):# thesi apo to stratiotaki kai kinisis pou mori na kanei
        pass

    def getTheRookMoves(self, r, c, kinisis):# thesi apo to pirgo kai kinisis pou mori na kanei
        pass

    def getTheBishopMoves(self, r, c, kinisis):# thesi apo to stratigo kai kinisis pou mori na kanei
        pass

    def getTheKnightMoves(self, r, c, kinisis):# thesi apo to alogo kai kinisis pou mori na kanei
        pass

    def getTheQueenMoves(self, r, c, kinisis):# thesi apo to vasilissa kai kinisis pou mori na kanei
        pass

    def getTheKingMoves(self, r, c, kinisis):# thesi apo to vasilia kai kinisis pou mori na kanei
        pass


class Kinisis():

    ranksToRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1,"8:":0}

    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, }

    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSqr, endSqr, board):
        self.startRow = startSqr[0]
        self.startCol = startSqr[1]
        self.endRow = endSqr[0]
        self.endCol = endSqr[1]
        self.pouliaKinisi = board[self.startRow][self.startCol]
        self.pouliaCapture = board[self.endRow][self.endCol]
        self.kinisiID = self.startRow * 1000 + self.startCol * 100 +self.endRow *10 + self.endCol
        print(self.kinisiID)
    def __eq__(self, other):
        if isinstance(other, Kinisis):
            return self.kinisiID == other.kinisiID
        return False



    def getChessNotes(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)


    def getRankFile(self, r, c):
        return  self.colsToFiles[c] + self.rowsToRanks[r]





