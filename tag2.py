from datetime import datetime
zeit = datetime.now().hour

if zeit == 12:
    print("Mahlzeit")
elif 12 <= zeit < 18:
    print ("Guten Mittag!")
elif 0 <= zeit < 12:
    print("Guten Morgen!")
elif 13 <= zeit < 24:
    print("Guten Abend!")
else:
    print("Das ist doch keine richtige Uhrzeit du Witzbold!")