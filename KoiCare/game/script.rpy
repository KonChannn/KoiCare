# The script of the game goes in this file.

define DEFAULT_TIME = 50
define DEATH_TIME = 30
define LVL1_MOVES = 5

define pumpOn = True
define fishHealthy = True
define fishHungry = False
define time = DEFAULT_TIME
define counter = 0

# Logic Timer
screen timerr:
    timer 1 repeat True action [
        SetVariable("time", time - 1),
        SetVariable("fishHealthy", time - 1 > 40),
        If(time - 1 <= 0, [Hide("timerr"), Jump("end")])
    ]
    text str(time) xalign 0.95
    
# Status Ikan
screen fish_status:
    if fishHealthy:
        text "Ikan Sehat" at topleft as text2
    else:
        text "Ikan Sakit" at topleft as text2

# The game starts here.

label start:
    "Sebelum berangkat ke kampus, aku harus memastikan ikan di rumah tetap sehat."

    jump lvl1


label lvl1:
    scene bg room

    # If the player has done a set amount of actions, proceed to the next scene
    if counter == LVL1_MOVES:
        "Whoops, Aku harus segera pergi ke kampus!"
        $ counter = 0
        jump end

    # Prints the Timer on the screen
    if pumpOn == False:
        show screen timerr
    else:
        hide screen timerr
        $ time = DEFAULT_TIME

    # Prints the status of pump
    if pumpOn:
        show text "Pompa Air Hidup" at top as text1
    else:
        show text "Pompa Air Mati" at top as text1 
    
    show screen fish_status

    menu:
        "What Should I do?"

        "Beri Makan":
            "Makan Diberikan"
            
        "Cek Kualitas Air":
            if not pumpOn:
                "Air Kotor"
                "Waduh, Pompanya Mati!"
            else:
                "Air Bersih"
        
        "Nyalakan Pompa Air" if not pumpOn:
            "Pompa Air Menyala"
            $ pumpOn = True
            $ fishHealthy = True
        
        "Matikan Pompa Air" if pumpOn:
            "Pompa Air Mati"
            $ pumpOn = False

    
    $ counter += 1
    jump lvl1

label end:

    if not fishHealthy:
        "Ikan Mati"
    else:
        "Hari Berakhir"
    
    return