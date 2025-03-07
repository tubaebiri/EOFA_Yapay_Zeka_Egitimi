class Kitap:
    def __init__(self, ad, yazar, yil):
        self.ad = ad  
        self.yazar = yazar  
        self.yil = yil  
    
    def kitap_bilgisi(self):
        print(f"Kitap Adı: {self.ad}\nYazar: {self.yazar}\nYıl: {self.yil}")

kitap1 = Kitap("Tutunamayanlar", "Oguz Atay", 1971)

kitap1.kitap_bilgisi()


#class nesnelerin temel özelliklerini ve davranislarini tanımlar