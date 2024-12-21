import pyxel
from random import randint

GRASS = 0
STONE = 1
BLOCK_SIZE = 5


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        self.map = [
            [[GRASS, STONE][randint(0, 1)] for _ in range(50)] for _ in range(50)
        ]
        self.pos = {"x": 10, "y": 10}
        pyxel.run(self.update, self.draw)

    ##############
    # Game logic #
    ##############
    def update(self):
        self.handle_input()

    def handle_input(self):
        if (
            pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)
        ) and self.is_inside_map(self.x - BLOCK_SIZE, self.y):
            self.x -= BLOCK_SIZE
        if (
            pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)
        ) and self.is_inside_map(self.x + BLOCK_SIZE, self.y):
            self.x += BLOCK_SIZE
            print(self.x)
        if (
            pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)
        ) and self.is_inside_map(self.y - BLOCK_SIZE, self.y):
            self.y -= BLOCK_SIZE
        if (
            pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)
        ) and self.is_inside_map(self.y + BLOCK_SIZE, self.y):
            self.y += BLOCK_SIZE

    def is_inside_map(self, x, y):
        return (
            0 <= x < len(self.map[0]) * BLOCK_SIZE
            and 0 <= y < len(self.map) * BLOCK_SIZE
        )

    ##############
    # Draw logic #
    ##############
    def draw(self):
        pyxel.cls(0)
        self.draw_map()
        self.draw_player()

    def draw_player(self):
        pyxel.rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE, 9)

    def draw_map(self):
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                color = [pyxel.COLOR_GREEN, pyxel.COLOR_GRAY][tile]
                pyxel.rect(
                    x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, color
                )


App()
