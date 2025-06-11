# Tutorial - Handles the tutorial scene

# Tutorial Scene
label tutorial:
    $ gameState = "tutorial"
    scene black
    
    "Mari pelajari dasar-dasar perawatan ikan Koi."
    
    "1. Kesehatan Ikan:"
    "   - Jaga kesehatan ikan Anda dengan memberinya makan secara teratur"
    "   - Pantau kesehatan ikan secara rutin"
    "   - Ikan yang sehat adalah ikan yang bahagia!"
    
    "2. Kualitas Air:"
    "   - Menjaga kualitas air yang baik dengan menggunakan pompa air"
    "   - Periksa kualitas air secara teratur"
    "   - Air bersih berarti ikan yang sehat!"
    
    "3. Manajemen Uang:"
    "   - Anda mulai dengan $[STARTING_MONEY]"
    "   - Harga Pakan Ikan $[FEEDING_COST]"
    "   - Anda mendapatkan uang saku harian sebesar $20"
    "   - Belanjakan dengan bijak!"
    
    "4. Manajemen Waktu:"
    "   - Setiap hari memiliki empat fase: Pagi, Siang, Sore, dan Malam"
    "   - Rencanakan tindakan Anda dengan hati-hati untuk setiap fase"
    "   - Jangan lupa untuk memeriksa ikan Anda!"
    
    menu:
        "Saya Mengerti":
            jump day_loop
        "Jelaskan Ulang":
            jump tutorial 