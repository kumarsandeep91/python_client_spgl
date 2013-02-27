import gwindow
import gobjects

WIDTH = 400
HEIGHT = 650

window = gwindow.GWindow(width = WIDTH, height = HEIGHT)

BRICK_SPACE = 4
BRICKS_IN_ROW = 10
BRICK_HEIGHT = 10
NUM_ROWS = 5
TOP_OFFSET = 50
BRICK_WIDTH = (WIDTH - (BRICKS_IN_ROW - 1)*BRICK_SPACE) / BRICKS_IN_ROW

y = TOP_OFFSET
for i in range(NUM_ROWS):
	x = 0
	for j in range(BRICKS_IN_ROW):
		brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
		window.add(brick, x, y)
		x = x + BRICK_SPACE + BRICK_WIDTH
	

