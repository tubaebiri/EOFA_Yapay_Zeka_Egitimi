class Kisi:
    def __init__(self, isim, yas, sehir):
        self.isim = isim  
        self.yas = yas  
        self.sehir = sehir  
    
    def kisi_bilgisi(self):
        print(f"İsim: {self.isim}\nYaş: {self.yas}\nŞehir: {self.sehir}")

kisi1 = Kisi("Tuba", 24, "İstanbul")
kisi1.kisi_bilgisi()

#nesnenin başlangıç değerlerini atanir
#bir nesne oluşturugunda ilk bu metot cagirilir 