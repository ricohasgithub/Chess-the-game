
import pygame

class Board():

    def __init__(self, board, x_dim, y_dim):

        self.board = board
        self.x_dim = x_dim
        self.y_dim = y_dim

        # Display settings
        self.board_pos = (100, 100)
        self.tilesize = 50

    # Method to get either the board state is: ongoing, check, checkmate, stalemate
    def get_game_state(self):
        pass

    # Code from: https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs; thank you!!
    def get_square_under_mouse(self):

        mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - self.board_pos
        x, y = [int(v // self.tilesize) for v in mouse_pos]

        try: 
            if x >= 0 and y >= 0: return (self.board[y][x], x, y)

        except IndexError: pass
        return None, None, None

    def draw_pieces(self, screen, piece):

        sx, sy = piece.position.x, piece.position.y

        for y in range(self.y_dim):
            for x in range(self.x_dim): 
                piece = board[y][x]
                if piece:
                    selected = x == sx and y == sy
                    pos = pygame.Rect(self.board_pos[0] + x * self.tilesize + 1, self.board_pos[1] + y * self.tilesize + 1, self.tilesize, self.tilesize)
                    screen.blit(piece.img, piece.img.get_rect(center=pos.center))

    def draw_drag(self, screen, selected_piece):

        if selected_piece:
            piece, x, y = get_square_under_mouse()

            if x != None:
                rect = (self.board_pos[0] + x * self.tilesize, self.board_pos[1] + y * self.tilesize, self.tilesize, self.tilesize)
                pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)

            pos = pygame.Vector2(pygame.mouse.get_pos())
            screen.blit(piece.img, piece.img.get_rect(center=pos.center))

            selected_rect = pygame.Rect(self.board_pos[0] + piece.pos.x * self.tilesize, self.board_pos[1] + piece.pos.y * self.tilesize, self.tilesize, self.tilesize)
            return (x, y)