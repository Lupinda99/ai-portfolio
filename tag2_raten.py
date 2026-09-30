import random
geheim = random.randint(1, 20)

print("Ich habe mir eine Zahl von 1-20 ausgedacht wenn du richtig rätst darft du pushen")

versuche = 0

while True:
    versuche = versuche +1
    antwort = int(input("Zahl eingeben: "))
    if antwort == geheim:
        print("Du hast richtig geraten und darfst pushen! ")
        if versuche == 1:
            print("Du hast es in einem Versuch geschafft. Hut ab!")
        else:
            print(f"Du hast es in {versuche} Versuchen geschafft")
        break
    elif antwort > geheim:
        print("Die Zahl ist zu hoch aber rate gerne nochmal! ")
    elif antwort < geheim:
        print("Die Zahl ist zu niedrig aber rate gerne nochmal! ")

