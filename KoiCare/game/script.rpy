# The script of the game goes in this file.

# Game Constants
define DEFAULT_TIME = 50
define DEATH_TIME = 30
define LVL1_MOVES = 5
define MAX_FISH_HEALTH = 100
define MAX_WATER_QUALITY = 100
define FEEDING_COST = 10
define STARTING_MONEY = 100

# Game State Variables
default money = STARTING_MONEY
default gameState = "intro"

# Main Game Flow
label start:
    jump intro

# Introduction Scene
label intro:
    $ gameState = "intro"
    scene black
    
    "Selamat datang di KoiCare - Your Koi Fish Care Simulator!"
    "Dalam game ini, Anda akan belajar cara merawat ikan koi Anda."
    "Tujuan Anda adalah menjaga ikan Anda tetap sehat dan bahagia!"
    
    menu:
        "Tutorial":
            jump tutorial
        "Skip Tutorial":
            jump day_loop
        "Quit":
            return



