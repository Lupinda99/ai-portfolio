stadt = input("Wo wohnst du?")
farbe = input("Was ist deine Lieblingsfarbe?")
name = input("Was ist dein Name?")

from datetime import datetime
jetzt = datetime.now()
text = jetzt.strftime("%d.%m.%Y um %H:%M:%S")
print(text)
print(f"Dein Name ist: {name} du wohnst in {stadt} und deine Lieblingsfarbe ist {farbe}")