class Calisan:
    def __init__(self, isim, departman):
        self.isim = isim  
        self.departman = departman  
    
    def calis(self):
        print(f"{self.isim}, {self.departman} departmanında çalışıyor.")

class Yazilimci(Calisan):
    def __init__(self, isim, departman, diller):
        super().__init__(isim, departman)#(parent class) özelliklerine ve metodlarına erişmemizi sağlar
        self.diller = diller  
    
    def yazilim_dili(self):
        print(f"{self.isim}, {', '.join(self.diller)} dillerinde kod yazıyor")

calisan1 = Calisan("Derya", "Pazarlama")
yazilimci1 = Yazilimci("Tuba", "Yazılım Geliştirme", ["Python", "C#"])

calisan1.calis()
yazilimci1.calis() 
yazilimci1.yazilim_dili()
#bir sinifin başka bir sinifin özelliklerini miras almasını saglar
