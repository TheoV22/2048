import numpy as np

CP = {
    "back": (189, 172, 161),
    0: (204, 192, 179),
    2: (238, 228, 219),
    4: (240, 226, 202),
    8: (242, 177, 121),
    16: (236, 141, 85),
    32: (250, 123, 92),
    64: (234, 90, 56),
    128: (237, 207, 114),
    256: (242, 208, 75),
    512: (237, 200, 80),
    1024: (227, 186, 19),
    2048: (236, 196, 2),
    4096: (96, 217, 146),
}

GRID = {
    "starting_numbers": [0, 2, 4],
    "size": (4,4),
    "probability": [0.8, 0.15, 0.05]
}

GUI = {
    "N": 4,
    "W": 600,
    "H": 600,
    "SPACING": 10,
    "title": "2048",
    "font_type": "Comic Sans MS",
    "grid_font_size": 30,
    "game_over": {
        "font_size": 60,
        "text": "Game Over",
        "pos": (1/2,1/2)
    },
    "replay": {
        "text": "Replay",
        "font_size": 40,
        "button": {
            "pos": (1/2, 3/4),
            "width": 150,
            "height": 55,
            "color": (0, 0, 0),
            "hover_color": (100,100,100)
        }
    }
}

