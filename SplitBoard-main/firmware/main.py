import board

from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# 4x2 matrix
col_pins = (board.A0, board.A1, board.A2, board.A3, board.A4)
row_pins = (board.A5, board.D6, board.D10, board.D9, board.D8, board.D7)
diode_orientation = DiodeOrientation.COL2ROW

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BKDL, 
     KC.Y, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.TAB,
     KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.ENTER,
     KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.SHIFT,
     KC.SPACE, KC.LALT, KC.LEFT, KC.UP, KC.DOWN, KC.RIGHT
     ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()