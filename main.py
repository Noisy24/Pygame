import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.r = 0
        self.g = 255
        self.b = 0
        self.cell_size = 70
        self.left = 1000 // 2 - (self.cell_size * 9) // 2
        self.top = 700 // 2 - (self.cell_size * 9) // 2

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                pygame.draw.rect(surface, '#99DDCC',
                                 ((self.left + c * self.cell_size),
                                  (self.top + r * self.cell_size),
                                  self.cell_size + 1, self.cell_size + 1), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_coord):
        x, y = mouse_coord
        r, c = (y - self.top) // self.cell_size, (x - self.left) // self.cell_size
        if 0 <= r <= self.height and 0 <= c < self.width:
            return r, c
        return None

    @staticmethod
    def on_click(cell):
        print(cell)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    screen.fill('#BAD7DF')
    board = Board(9, 9)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.render(screen)
        pygame.display.flip()
