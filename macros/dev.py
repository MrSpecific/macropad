# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Dev Shortcuts

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "Dev",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x105006, "Code", ["code .", Keycode.ENTER]),
        (0x105006, "Open", ["open .", Keycode.ENTER]),
        (0x930462, "Goto", [Keycode.COMMAND, "P"]),  # Go to file
        # 2nd row ----------
        (0x483502, "< Tab", [Keycode.COMMAND, Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x483502, "Tab >", [Keycode.COMMAND, Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x930462, "Cmd", [Keycode.COMMAND, Keycode.SHIFT, "P"]),  # Command Pallete
        # 3rd row ----------
        (0x082C57, "Status", ["git", " ", "status", Keycode.ENTER]),
        (0x002531, "Remote", ["git", " ", "remote -v", Keycode.ENTER]),
        (0x002531, "Checko", ["git", " ", "checkout "]),
        # 4th row ----------
        (0x8315B7, "Add", ["git add ."]),  # Adafruit in new window
        (0x8315B7, "Commit", ['git commit -a -m ""', Keycode.LEFT_ARROW]),
        (0x8315B7, "Push", ["git push"]),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}
