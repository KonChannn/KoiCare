# Tutorial - Handles the tutorial scene

# Tutorial Scene
label tutorial:
    $ gameState = "tutorial"
    scene bg room
    
    "Let's learn the basics of koi fish care!"
    
    "1. Fish Health:"
    "   - Keep your fish healthy by feeding it regularly"
    "   - Monitor its health status"
    "   - Healthy fish are happy fish!"
    
    "2. Water Quality:"
    "   - Maintain good water quality using the pump"
    "   - Check water quality regularly"
    "   - Clean water means healthy fish!"
    
    "3. Money Management:"
    "   - You start with $[STARTING_MONEY]"
    "   - Feeding costs $[FEEDING_COST]"
    "   - You get $20 daily allowance"
    "   - Spend wisely!"
    
    "4. Time Management:"
    "   - Each day has four phases: Morning, Afternoon, Evening, and Night"
    "   - Plan your actions carefully for each phase"
    "   - Don't forget to check on your fish!"
    
    menu:
        "I understand":
            jump day_loop
        "Show me again":
            jump tutorial 