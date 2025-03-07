from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy
    
    def alan(self):
        return self.en * self.boy

dikdortgen = Dikdortgen(5, 10)
print(f"Dikdörtgenin alanı: {dikdortgen.alan()}")



