# Main Game Loop - Coordinates all FSMs and game states

init python:
    # Initialize game systems
    time_fsm = TimeFSM()
    fish_fsm = FishFSM()
    pond_fsm = PondFSM()
    electricity_fsm = ElectricityFSM()

transform koiSize:
    zoom 0.7

image koiNormal = "koi_normal.png"
image koiSick = "koi_sick.png"
image koiSad = "koi_sad.png"
image koiHappy = "koi_happy.png"
image koiDead = "koi_dead.png"

# Time Cycle Timer Screen
screen time_cycle:
    text "[time_fsm.current_state.title()] - Turns Remaining: [time_fsm.time_remaining]" xalign 0.5 yalign 0.05
    

# Status Display Screen
screen game_status:
    frame:
        background Solid((0, 0, 0, 180))
        xalign 0.95
        yalign 0.05
        vbox:
            text "Day: [time_fsm.day_number]"
            text "Money: $[money]"
            text "Fish Health: [fish_fsm.health]%"
            text "Water Quality: [pond_fsm.water_quality]%"
            text "Electricity: [electricity_fsm.amount]%"

# Main Game Loop
label day_loop:
    $ gameState = "day_loop"
    scene bg aquarium

    # Sets the koi image based on the health
    if fish_fsm.current_state == "normal":
        show koiNormal at truecenter, koiSize
        with dissolve
    elif fish_fsm.current_state == "sick":
        show koiSick at truecenter, koiSize
        with dissolve
    elif fish_fsm.current_state == "healthy":
        show koiHappy at truecenter, koiSize
        with dissolve

    "Day [time_fsm.day_number] - [time_fsm.current_state.title()]"
    
    # Show game status and time cycle
    show screen game_status
    show screen time_cycle
    
    # Phase-specific background and effects
    $ current_state = time_fsm.get_current_state_info()
    "[current_state['description']]"
    
    # Apply time effects
    $ time_fsm.apply_time_effects(fish_fsm, pond_fsm)
    $ fish_fsm.apply_effects()
    $ pond_fsm.apply_effects()

    # If pump is on, decrease electricity, if electricity empty, turn off pump
    if pond_fsm.pump_on:
        $ electricity_fsm.apply_effects()
        if electricity_fsm.amount <= 0:
            $ pond_fsm.pump_on = False
            "Listrik habis! Pompa air mati."

    menu:
        "Beri Makan":
            if money >= FEEDING_COST:
                scene bg feed
                $ money -= FEEDING_COST
                $ fish_fsm.feed()
                "Makan Diberikan"
                "Ikan terlihat lebih sehat!"
            else:
                "Tidak cukup uang untuk membeli makanan!"
        
        "Cek Kualitas Air":
            "[pond_fsm.get_state_description()]"
        
        "Nyalakan Pompa Air" if not pond_fsm.pump_on:
            if electricity_fsm.amount > 0:
                $ pond_fsm.toggle_pump()
                "Pompa Air Menyala"
            else:
                "Listrik habis! Tidak bisa menyalakan pompa."
        
        "Matikan Pompa Air" if pond_fsm.pump_on:
            $ pond_fsm.toggle_pump()
            "Pompa Air Mati"

        "Cek Kondisi Ikan":
            "[fish_fsm.get_state_description()]"

        "Obat - Obatan":
            menu medChoice:
                "Beli Obat Ikan":
                    if money >= MEDICINE_COST:
                        $ money -= MEDICINE_COST
                        $ fish_fsm.increaseHealth(25)
                    else:
                        "Uang Tidak Cukup Untuk Membeli Obat Ikan!"
                "Beli Treatment Air":
                    if money >= WATERTREAT_COST:
                        $ money -= WATERTREAT_COST
                        $ pond_fsm.increaseQuality(10)
                    else:
                        "Uang Tidak Cukup Untuk Membeli Pembersih Kolam"

        "Advance Time":
            $ time_fsm.time_remaining = 0
            $ fish_fsm.decreaseHealth(int(0.2 * fish_fsm.health)) #Decrease health by 20%
            if pond_fsm.pump_on:
                $ electricity_fsm.decreaseCharge(15)
            else:
                $ pond_fsm.decreaseQuality(10)
            jump advance_time

    $ time_fsm.decrement_time()
    if time_fsm.get_time_remaining() <= 0:
        "Waktu untuk hari ini telah habis."
        jump advance_time
    else:
        jump day_loop

# Time Advancement
label advance_time:
    $ new_day = time_fsm.advance_time()
    if new_day:
        jump end_of_day
    else:
        "[time_fsm.current_state.title()] has begun..."
        jump day_loop

# End of Day Processing
label end_of_day:
    $ gameState = "end_of_day"
    
    if not fish_fsm.is_alive():
        "Ikan Mati"
        jump ending
    else:
        "Hari Berakhir"
        $ money += 20  # Daily allowance
        $ electricity_fsm.recharge(50) # Recharges electricity by 50pt
        menu:
            "Continue to next day":
                jump day_loop
            "Save and Quit":
                return

# Game Ending
label ending:
    $ gameState = "ending"
    
    if not fish_fsm.is_alive():
        show koiDead at truecenter
        "Game Berakhir!"
        "Ikan koi Anda mati karena perawatan yang buruk."
        "You survived for [time_fsm.day_number] days."
    else:
        "Selamat!"
        "Anda telah berhasil merawat ikan koi Anda!"
        "You played for [time_fsm.day_number] days."
    
    menu:
        "Start New Game":
            hide screen game_status
            hide screen time_cycle
            $ time_fsm = TimeFSM()
            $ fish_fsm = FishFSM()
            $ pond_fsm = PondFSM()
            $ electricity_fsm = ElectricityFSM()
            $ money = STARTING_MONEY
            jump intro
        "Quit":
            return 