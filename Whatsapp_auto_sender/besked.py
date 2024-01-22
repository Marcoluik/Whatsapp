import random
Hello = []
Navn = []
Text = []
Meld_ud = []

Hello.append("Hey")
Hello.append("Halløj")
Hello.append("Hejsa")
Hello.append("Hej")

Navn.append("gutter")
Navn.append("drenge")
Navn.append("brødre")
Navn.append("venner")

Text.append("her kommer ugens teknik")
Text.append("her er denne uges teknik")
Text.append("så kommer denne uges teknik")
Text.append("her er hvem der skal styre teknikken")

Meld_ud.append("Meld gerne ud hvis du er blevet forhindret :)")
Meld_ud.append("Skriv gerne hvis du er blevet forhindret :)")
Meld_ud.append("Meld gerne ud hvis du har byttet :)")
Meld_ud.append("Skriv gerne hvis du har byttet :)")

def msg():
    hello, navn, text = random.sample(range(1,4),3)
    return f"{Hello[hello]} {Navn[navn]} {Text[text]}"
def afskedmsg():
    meld_ud = random.randrange(1,4)
    return f"{Meld_ud[meld_ud]}"
