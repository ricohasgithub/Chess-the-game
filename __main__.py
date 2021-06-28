
import pygame

from pieces import Position

from pieces import Piece
from pieces import Pawn
from pieces import Knight
from pieces import Bishop
from pieces import Rook
from pieces import Queen
from pieces import King

from board import Board

TILESIZE = 50
BOARD_POS = (120, 40)

board = []

# Fill default 8x8 chessboard with standard chess pieces
for y in range(8):
    board.append([])
    for x in range(8):
        board[y].append(None)

for x in range(0, 8):
    board[1][x] = Pawn(Position(1, x), "black", "./assets/classic_8bit/black/black_pawn.png")
for x in range(0, 8):
    board[6][x] = Pawn(Position(6, x), "white", "./assets/classic_8bit/white/white_pawn.png")

board[0][0] = Rook(Position(0, 0), "black", "./assets/classic_8bit/black/black_rook.png")
board[0][7] = Rook(Position(0, 7), "black", "./assets/classic_8bit/black/black_rook.png")
board[0][1] = Knight(Position(0, 1), "black", "./assets/classic_8bit/black/black_knight.png")
board[0][6] = Knight(Position(0, 6), "black", "./assets/classic_8bit/black/black_knight.png")
board[0][2] = Bishop(Position(0, 2), "black", "./assets/classic_8bit/black/black_bishop.png")
board[0][5] = Bishop(Position(0, 5), "black", "./assets/classic_8bit/black/black_bishop.png")
board[0][3] = Queen(Position(0, 3), "black", "./assets/classic_8bit/black/black_queen.png")
board[0][4] = King(Position(0, 4), "black", "./assets/classic_8bit/black/black_king.png")

board[7][0] = Rook(Position(7, 0), "white", "./assets/classic_8bit/white/white_rook.png")
board[7][7] = Rook(Position(7, 7), "white", "./assets/classic_8bit/white/white_rook.png")
board[7][1] = Knight(Position(7, 1), "white", "./assets/classic_8bit/white/white_knight.png")
board[7][6] = Knight(Position(7, 6), "white", "./assets/classic_8bit/white/white_knight.png")
board[7][2] = Bishop(Position(7, 2), "white", "./assets/classic_8bit/white/white_bishop.png")
board[7][5] = Bishop(Position(7, 5), "white", "./assets/classic_8bit/white/white_bishop.png")
board[7][3] = Queen(Position(7, 3), "white", "./assets/classic_8bit/white/white_queen.png")
board[7][4] = King(Position(7, 4), "white", "./assets/classic_8bit/white/white_king.png")

chess_board = Board(board, 8, 8)

def create_board_surf():
    board_surf = pygame.Surface((TILESIZE*8, TILESIZE*8))
    dark = False
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('#393939' if dark else 'white'), rect)
            dark = not dark
        dark = not dark
    return board_surf

def main():

    pygame.init()
    font = pygame.font.SysFont('', 32)
    screen = pygame.display.set_mode((640, 480))
    board_surf = create_board_surf()
    clock = pygame.time.Clock()
    selected_piece = None
    drop_pos = None

    while True:

        piece, x, y = chess_board.get_square_under_mouse()
        events = pygame.event.get()

        for e in events:

            if e.type == pygame.QUIT:
                return
            if e.type == pygame.MOUSEBUTTONDOWN:
                if piece != None:
                    selected_piece = piece, x, y
            if e.type == pygame.MOUSEBUTTONUP:
                if drop_pos:
                    
                    piece, old_x, old_y = selected_piece

                    if piece.check_move_legal(Position(drop_pos[0], drop_pos[1]), chess_board):

                        piece.move(Position(drop_pos[0], drop_pos[1]))
                        board[old_y][old_x] = None
                        new_x, new_y = drop_pos
                        board[new_y][new_x] = piece

                selected_piece = None
                drop_pos = None

        screen.fill(pygame.Color('#393939'))
        screen.blit(board_surf, BOARD_POS)
        chess_board.draw_pieces(screen, selected_piece)
        drop_pos = chess_board.draw_drag(screen, selected_piece)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()