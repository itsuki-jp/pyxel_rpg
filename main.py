import pyxel
from random import randint, random

GRASS = 0
STONE = 1
SEA = 2
ITEM = 3
BLOCK_SIZE = 5


class App:
    def __init__(self):
        pyxel.init(120, 120)
        self.x = 50
        self.y = 50
        self.item_count = 0
        self.map = [
            [
                (GRASS if random() < 0.7 else STONE if random() < 0.9 else ITEM)
                for j in range(150)
            ]
            for i in range(150)
        ]
        pyxel.run(self.update, self.draw)

    ##############
    # Game logic #
    ##############
    def update(self):
        self.handle_input()

    def handle_input(self):
        new_x = self.x
        new_y = self.y

        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            new_x -= 1
        elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(
            pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT
        ):
            new_x += 1
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            new_y -= 1
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            new_y += 1
        else:
            return
        if self.is_inside_map(new_x, new_y) and self.map[new_y][new_x] != STONE:
            self.x = new_x
            self.y = new_y
            print("hogehoge!")

            if self.is_get_item(new_x, new_y):
                self.item_count += 1

    def is_inside_map(self, x, y):
        return 0 <= x < len(self.map[0]) and 0 <= y < len(self.map)

    def is_get_item(self, x, y):
        return self.map[y][x] == ITEM

    ##############
    # Draw logic #
    ##############
    def draw(self):
        pyxel.cls(0)
        self.draw_map()
        self.draw_player()
        self.draw_text(x=0, y=0, text=f"Item: {self.item_count}")

    def draw_player(self):
        pyxel.rect(
            pyxel.width // 2,
            pyxel.height // 2,
            BLOCK_SIZE,
            BLOCK_SIZE,
            0,
        )

    def draw_text(self, x, y, text):
        pyxel.text(x, y, text, 1)

    def draw_map(self):
        start_x = max(self.x - pyxel.width // (2 * BLOCK_SIZE), 0)
        start_y = max(self.y - pyxel.height // (2 * BLOCK_SIZE), 0)
        end_x = min(self.x + pyxel.width // (2 * BLOCK_SIZE), len(self.map[0]))
        end_y = min(self.y + pyxel.height // (2 * BLOCK_SIZE), len(self.map))

        for y, row in enumerate(self.map[start_y:end_y]):
            for x, tile in enumerate(row[start_x:end_x]):
                color = [
                    11,
                    4,
                    5,
                    11,
                ][tile]
                pyxel.rect(
                    (x + start_x - self.x + pyxel.width // (2 * BLOCK_SIZE))
                    * BLOCK_SIZE,
                    (y + start_y - self.y + pyxel.height // (2 * BLOCK_SIZE))
                    * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                    color,
                )


App()
