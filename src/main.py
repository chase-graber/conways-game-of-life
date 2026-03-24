from raylib import *
from pyray import *

from copy import deepcopy

GRID_WIDTH = 150
GRID_HEIGHT = 150
BOX_SIZE = 5

class GOL:
    def __init__(self, grid_width, grid_height, box_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.box_size = box_size

        self.cells = self.randomize_cells()

        set_trace_log_level(LOG_WARNING | LOG_ERROR | LOG_FATAL)
        init_window(grid_width * box_size, grid_height * box_size, 'Conway\'s Game of Life')
        set_target_fps(30)

    def randomize_cells(self):
        cells = []

        for _ in range(self.grid_width):
            row = []
            for _ in range(self.grid_height):
                row.append(get_random_value(0, 1))
            cells.append(row)

        return cells

    def run(self):
        while not window_should_close():
            self.update()
            self.draw()
        
        close_window()

    def update(self):
        cells_copy = deepcopy(self.cells)

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                num_living = 0

                # Check each cell nearby, if living increment num_living
                if j > 0 and i > 0: num_living += cells_copy[i - 1][j - 1]
                if j > 0: num_living += cells_copy[i][j - 1]
                if j > 0 and i < self.grid_width - 1: num_living += cells_copy[i + 1][j - 1]
                if i < self.grid_width - 1: num_living += cells_copy[i + 1][j]
                if j < self.grid_height - 1 and i < self.grid_width - 1: num_living += cells_copy[i + 1][j + 1]
                if j < self.grid_height - 1: num_living += cells_copy[i][j + 1]
                if j < self.grid_height - 1 and i > 0: num_living += cells_copy[i - 1][j + 1]
                if i > 0: num_living += cells_copy[i - 1][j]

                # Determine living or dead based on num_living
                if self.cells[i][j] == 1 and (num_living < 2 or num_living > 3):
                    self.cells[i][j] = 0
                elif num_living == 3:
                    self.cells[i][j] = 1

    def draw(self):
        begin_drawing()

        clear_background(RAYWHITE)

        for i, row in enumerate(self.cells):
            for j, col in enumerate(row):
                draw_rectangle(j * self.box_size, i * self.box_size, self.box_size, self.box_size, WHITE if col == 1 else BLACK)

        draw_fps(10, 10)

        end_drawing()

if __name__ == '__main__':
    gol = GOL(GRID_WIDTH, GRID_HEIGHT, BOX_SIZE)
    gol.run()
