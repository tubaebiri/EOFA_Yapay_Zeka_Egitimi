class Ogrenci:
    def __init__(self, isim):
        self.isim = isim  
        self.__notlar = []#private

    def not_ekle(self, not_):
        if 0 <= not_ <= 100:
            self.__notlar.append(not_)  
        else:
            print("Geçersiz not")

    def notlari_goster(self):
        print(f"{self.isim}'in notları: {self.__notlar}")

ogrenci1 = Ogrenci("Mehmet")

ogrenci1.not_ekle(85)
ogrenci1.not_ekle(92)
ogrenci1.notlari_goster()

#veriyi gizler sadece belirtilen metotlarda erişilmesini saglar
