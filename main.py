stadt = input("Wo wohnst du?")

if stadt == "Ulm":
        print(" Ah da komm ich auch her")
elif stadt =="Stuttgart":
        print(" Ohh aus unserer Landeshauptstadt cool!")
else:
        print(f"{stadt} da kenne ich mich nicht so gut aus :)")

farbe = input(" Was ist deine Lieblingsfarbe?")

if farbe == "Blau":
        print(" cool das ist auch meine lieblingsfarbe!")
elif farbe == ("Rot"):
        print(" Rot mag ich auch sehr gerne!")
else:
        print(f"{farbe}ist auch eine schöne Farbe!")

name = input("Was ist dein Name?")



from datetime import datetime
jetzt = datetime.now()
text = jetzt.strftime("%d.%m.%Y um %H:%M:%S")
print(text)
print(f"Dein Name ist: {name} du wohnst in {stadt} und deine Lieblingsfarbe ist {farbe}")