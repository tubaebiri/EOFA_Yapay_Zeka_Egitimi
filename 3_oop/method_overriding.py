class Hayvan:
    def ses_cikar(self):
        print("Hayvan ses çıkarıyor!")

class Kopek(Hayvan):
    def ses_cikar(self):  
        print("Hav! Hav!")

class Kedi(Hayvan):
    def ses_cikar(self):  
        print("Miyav!")

kopek = Kopek()
kedi = Kedi()

kopek.ses_cikar()
kedi.ses_cikar()

#alt sınıfların üst sınıftan miras alınan metodu değiştirmesidir