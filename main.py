import pyxel


GRASS = 0
STONE = 1


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        self.map = [[GRASS for _ in range(50)] for _ in range(50)]
        self.pos = {"x": 25, "y": 25}
        pyxel.run(self.update, self.draw)

    ##############
    # Game logic #
    ##############
    def update(self):
        self.handle_input()

    def handle_input(self):
        if (
            pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)
        ) and self.is_inside_map(self.x - 1, self.y):
            self.x -= 1
        if (
            pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)
        ) and self.is_inside_map(self.x + 1, self.y):
            self.x += 1
            print(self.x)
        if (
            pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)
        ) and self.is_inside_map(self.y - 1, self.y):
            self.y -= 1
        if (
            pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)
        ) and self.is_inside_map(self.y + 1, self.y):
            self.y += 1

    def is_inside_map(self, x, y):
        return 0 <= x < len(self.map[0]) and 0 <= y < len(self.map)

    ##############
    # Draw logic #
    ##############
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 8, 8, 9)


App()
