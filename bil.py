class biljävel:
    def __init__(self):
        self.stårpåbilen = ""
        self.reg = ""
        self.fabrikat = ""
        self.model = ""
        self.årsmodel = ""
        self.tjänstevikt = ""
        self.effekt = ""

class ägare:
    def __init__(self):
        self.förnamn = ""
        self.efternamn = ""
ownera = input("Vem ska stå på bilen? efternamn:")
owner = input("Vem ska stå bå bilen? förnamn:")
bilcheck = input("Vad har du för bil?")
bilmodell = input("Vad är det för model?")
årsmodell = input("Vad är det för årsmodell?")
tvikt = input("Vad är tjänstevikten?")                  
regnummer = input("Vad har du för regnummer")
hp = input("Vad ha har för effekt?")

bil1 = ägare()
bil1.stårpåbilen = ägare()
bil1.förnamn = owner
bil1.efternamn = ownera

bil1 = biljävel()
bil1.reg = regnummer
bil1.fabrikat = bilcheck
bil1.model = bilmodell
bil1.årsmodel = årsmodell
bil1.tjänstevikt = tvikt
bil1.effekt = hp

bilcheck2 = input("Vad har du för bil?")
bilmodell2 = input("Vad är det för model?")
årsmodell2 = input("Vad är det för årsmodell?")
tvikt2 = input("Vad är tjänstevikten?")                  
regnummer2 = input("Vad har du för regnummer")
hp2 = input("Vad ha har för effekt?")

bil2 = biljävel()
bil2.reg = regnummer2
bil2.fabrikat = bilcheck2
bil2.model = bilmodell2
bil2.årsmodel = årsmodell2
bil2.tjänstevikt = tvikt2
bil2.effekt = hp2

print(f"reggunmer:{bil1.reg}. fabrikat: {bil1.fabrikat}. modell: {bil1.model}. årsmodell: {bil1.årsmodel}. tjänstevikt: {bil1.tjänstevikt}. effekten: {bil1.effekt}hk.")
print(f"reggunmer:{bil2.reg}. fabrikat: {bil2.fabrikat}. modell: {bil2.model}. årsmodell: {bil2.årsmodel}. tjänstevikt: {bil2.tjänstevikt}. effekten: {bil2.effekt}hk.")
