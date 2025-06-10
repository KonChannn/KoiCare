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
    scene bg room
    
    "Welcome to KoiCare - Your Koi Fish Care Simulator!"
    "In this game, you'll learn how to take care of your koi fish."
    "Your goal is to keep your fish healthy and happy!"
    
    menu:
        "Start New Game":
            jump tutorial
        "Skip Tutorial":
            jump day_loop
        "Quit":
            return



