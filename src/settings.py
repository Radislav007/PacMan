# flake8: noqa

MAP = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
	['1','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','1'],
	['1','B','1','1','.','1','1','1','.','1','.','1','1','1','.','1','1','B','1'],
	['1','.','.','.','.','1','.','.','.','1','.','.','.','1','.','.','.','.','1'],
	['1','1','.','1','.','1','.','1','.','1','.','1','.','1','.','1','.','1','1'],
	['1','.','.','1','.','.','.','1','.','.','.','1','.','.','.','1','.','.','1'],
	['1','.','1','1','1','1','.','1','1','1','1','1','.','1','1','1','1','.','1'],
	['1','.','.','.','.','.',' ',' ',' ','b',' ',' ',' ','.','.','.','.','.','1'],
	['1','1','.','1','1','1',' ','1','1','-','1','1',' ','1','1','1','.','1','1'],
	['.','.','.','.','.','1',' ','1','c','i','p','1',' ','1','.','.','.','.','.'],
	['1','1','.','1','.','1',' ','1','1','1','1','1',' ','1','.','1','.','1','1'],
	['1','.','.','1','.','.',' ',' ',' ',' ',' ',' ',' ','.','.','1','.','.','1'],
	['1','.','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1','.','1'],
	['1','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','1'],
	['1','1','1','.','1','1','1','.','1','1','1','.','1','1','1','.','1','1','1'],
	['1','.','.','.','1','.','.','.','.','P','.','.','.','.','1','.','.','.','1'],
	['1','B','1','.','1','.','1','.','1','1','1','.','1','.','1','.','1','B','1'],
	['1','.','1','.','.','.','1','.','.','.','.','.','1','.','.','.','1','.','1'],
	['1','.','1','1','1','.','1','1','1','.','1','1','1','.','1','1','1','.','1'],
	['1','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','1'],
	['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
]

BOARD_RATIO = (len(MAP[0]), len(MAP))
CHAR_SIZE = 32

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TILE_COLOR = (0, 0, 255)
DOT_COLOR = (255, 184, 151)


WIDTH, HEIGHT = (BOARD_RATIO[0] * CHAR_SIZE, BOARD_RATIO[1] * CHAR_SIZE)
MARGIN_BOTTOM = 64

PACMAN_SPEED = CHAR_SIZE // 4

GHOST_SPEED = 4

FPS = 30
