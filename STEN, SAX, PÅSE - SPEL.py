# STEN, SAX, PÅSE - SPEL
import random


sten = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


påse = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


sax = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


bilder = [sten, påse, sax]

# 0 = sten
# 1 = påse
# 2 = sax


# START


print("Starta spelet genom att välja: STEN, SAX, PÅSE\n")

print("Välj:\n")
print("0 = Sten\n")
print("1 = Påse\n")
print("2 = Sax\n")


# Spelaren väljer

spelare = int(input("Ditt val: \n"))


if spelare < 0 or spelare > 2:

    print("Ogiltigt val!\n")

else:

    # Visar bild
    print("Du valde:\n")
    print(bilder[spelare])

    # Datorn väljer

    dator_val = random.randint(0, 2)

    print("Datorn valde:\n")
    print(bilder[dator_val])

    # Resultat

    if spelare == dator_val:

        print("Oavgjort!\n")

    elif spelare == 0 and dator_val == 2:

        print("Du vann!\n")

    elif spelare == 1 and dator_val == 0:

        print("Du vann!\n")

    elif spelare == 2 and dator_val == 1:

        print("Du vann!\n")

    else:

        print("Du förlorade..\n")
