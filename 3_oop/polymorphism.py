class Araba:
    def hareket_et(self):
        print("Araba hareket ediyor")

class Bisiklet:
    def hareket_et(self):
        print("Bisiklet pedallarla hareket ediyor")

araba = Araba()
bisiklet = Bisiklet()

araba.hareket_et()
bisiklet.hareket_et()

#aynı metod adının farklı sınıflarda farklı şekilde çalışmasıdır

