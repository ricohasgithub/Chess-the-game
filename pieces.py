
import pygame

class Position():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Piece():

    def __init__(self, position, color, img_path):
        self.position = position
        self.color = color
        self.img_path = img_path
        self.img = pygame.image.load(self.img_path)
        self.img = pygame.transform.scale(self.img, (35, 40))

    def move(self, n_position):
        self.position = n_position

    def check_move_legal(self, n_position, board):
        pass

class Pawn(Piece):

    def __init__(self, position, color, img_path):
        super(Pawn, self).__init__(position, color, img_path)
        # Track if it is the first move
        self.first = True
        self.value = 1
        self.type = "P"

    def move(self, n_position):
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp
        self.position = n_position

    def check_move_legal(self, n_position, board):
  
        capture = False
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp

        piece = board.board[n_position.x][n_position.y]

        if self.color == "white":
            if self.first:
                if (n_position.x - self.position.x == -2 or n_position.x - self.position.x == -1) and n_position.y == self.position.y:
                    self.first = False
                    return True
                if piece:
                    if (piece.color != self.color) and (n_position.x - self.position.x == -1) and abs(n_position.y - self.position.y) == 1:
                        self.first = False
                        return True
            elif not self.first and not piece:
                if n_position.x - self.position.x == -1 and n_position.y == self.position.y:
                    return True
            elif not self.first and piece:
                if (piece.color != self.color) and (n_position.x - self.position.x == -1) and abs(n_position.y - self.position.y) == 1:
                    return True                
        if self.color == "black":
            if self.first:
                if (n_position.x - self.position.x == 2 or n_position.x - self.position.x == 1) and n_position.y == self.position.y:
                    self.first = False
                    return True
                if piece:
                    if (piece.color != self.color) and (n_position.x - self.position.x == 1) and abs(n_position.y - self.position.y) == 1:
                        self.first = False
                        return True
            elif not self.first and not piece:
                if n_position.x - self.position.x == 1 and n_position.y == self.position.y:
                    return True
            elif not self.first and piece:
                if (piece.color != self.color) and (n_position.x - self.position.x == 1) and abs(n_position.y - self.position.y) == 1:
                    return True
        return False

class Knight(Piece):

    def __init__(self, position, color, img_path):
        super(Knight, self).__init__(position, color, img_path)
        self.value = 3
        self.type = "N"

    def move(self, n_position):
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp
        self.position = n_position

    def check_move_legal(self, n_position, board):

        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp

        if abs(n_position.y - self.position.y) == 2 and abs(n_position.x - self.position.x) == 1:
            return True
        elif abs(n_position.y - self.position.y) == 1 and abs(n_position.x - self.position.x) == 2:
            return True
        return False

class Bishop(Piece):

    def __init__(self, position, color, img_path):
        super(Bishop, self).__init__(position, color, img_path)
        self.value = 3
        self.type = "B"

    def move(self, n_position):
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp
        self.position = n_position

    def check_move_legal(self, n_position, board):
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp
        if abs(n_position.y - self.position.y) == abs(n_position.x - self.position.x):
            return True
        return False

class Rook(Piece):

    def __init__(self, position, color, img_path):
        super(Rook, self).__init__(position, color, img_path)
        self.value = 5
        self.type = "R"

    def move(self, n_position):
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp
        self.position = n_position

    def check_move_legal(self, n_position, board):

        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp

        if abs(n_position.y - self.position.y) <= 7 and n_position.x == self.position.x:

            for i in range(self.position.y + 1, n_position.y):
                if board.board[n_position.x][i]:
                    return False
            for i in range(n_position.y + 1, self.position.y):
                if board.board[n_position.x][i]:
                    return False

            if board.board[n_position.x][n_position.y] and board.board[n_position.x][n_position.y].color != self.color:
                return True
            elif not board.board[n_position.x][n_position.y]:
                return True
            
        elif abs(n_position.x - self.position.x) <= 7 and n_position.y == self.position.y:

            for i in range(self.position.x + 1, n_position.x):
                if board.board[i][n_position.y]:
                    return False
            for i in range(n_position.x + 1, self.position.x):
                if board.board[i][n_position.y]:
                    return False

            if board.board[n_position.x][n_position.y] and board.board[n_position.x][n_position.y].color != self.color:
                return True
            elif not board.board[n_position.x][n_position.y]:
                return True

        return False

class Queen(Piece):

    def __init__(self, position, color, img_path):
        super(Queen, self).__init__(position, color, img_path)
        self.value = 9
        self.type = "Q"

    def move(self, n_position):
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp
        self.position = n_position

    def check_move_legal(self, n_position, board):

        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp

        if abs(n_position.y - self.position.y) == abs(n_position.x - self.position.x):
            return True
        elif abs(n_position.y - self.position.y) <= 7 and n_position.x == self.position.x:
            return True
        elif abs(n_position.x - self.position.x) <= 7 and n_position.y == self.position.y:
            return True
        return False

class King(Piece):

    def __init__(self, position, color, img_path):
        super(King, self).__init__(position, color, img_path)
        self.value = 10
        self.type = "K"

    def move(self, n_position):
        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp
        self.position = n_position

    def check_move_legal(self, n_position, board):

        temp = n_position.y
        n_position.y = n_position.x
        n_position.x = temp

        if abs(n_position.y - self.position.y) == abs(n_position.x - self.position.x) and abs(n_position.y - self.position.y) == 1:
            return True
        elif abs(n_position.y - self.position.y) == 1 and n_position.x == self.position.x:
            return True
        elif abs(n_position.x - self.position.x) == 1 and n_position.y == self.position.y:
            return True
        return False