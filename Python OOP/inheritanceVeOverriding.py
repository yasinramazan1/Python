"""
class Asker():
    def __init__(self, isim, rutbe):
        self.ad=isim
        self.rank=rutbe
        self.guc=80
    def hareketEttir(self):
        print("Hareket ettiriliyor")
    def puanKazan(self):
        print("Puan kazanıldı!")
    def puanKaybet(self):
        print("Puan kaybedildi!")
class Isci():
    def __init__(self, isim, rutbe):
        self.ad=isim
        self.rank=rutbe
        self.guc=80
    def hareketEttir(self):
        print("Hareket ettiriliyor")
    def puanKazan(self):
        print("Puan kazanıldı!")
    def puanKaybet(self):
        print("Puan kaybedildi!")
class Yonetici():
    def __init__(self, isim, rutbe):
        self.ad=isim
        self.rank=rutbe
        self.guc=80
    def hareketEttir(self):
        print("Hareket ettiriliyor")
    def puanKazan(self):
        print("Puan kazanıldı!")
    def puanKaybet(self):
        print("Puan kaybedildi!")

askerNesnesi=Asker("Yasin Ramazan Gök", "Teğmen")
askerNesnesi.puanKaybet()
isciNesnesi=Isci("Yasin Ramazan Gök", "Demirci")
isciNesnesi.puanKazan()
yoneticiNesnesi=Yonetici("Yasin Ramazan Gök", "CEO")
yoneticiNesnesi.hareketEttir()
# Bu şekilde bir oyunda her oyuncu için ayrı sınıf tanımladık ancak kalıtım ile bu kod fazlalığını azaltırız.
# Yani kalıtım ile bir sınıf oluşturup ( süper sınıf ) bu sınıftan gerekli sınıfları türeterek ( subclass )
# türetilen sınıfları da kendi içlerinde özelleştirebiliriz.
"""
class Oyuncu():
    def __init__(self, isim, rutbe):
        self.ad=isim
        self.rank=rutbe
        self.guc=80
    def bilgileriGoster(self):
        print(self.ad)
        print(self.rank)
        print(self.guc)
    def hareketEttir(self):
        print("Hareket ettiriliyor")
    def puanKazan(self):
        print("Puan kazanıldı!")
    def puanKaybet(self):
        print("Puan kaybedildi!")
class Asker(Oyuncu): # Bu Oyuncu super sınıfında türetilmiş bir alt sınıftır( subclass ).
    pass
askerNesnesi1=Asker("Mehmet Ali Gök", "Albay")
askerNesnesi1.puanKaybet()
class Isci(Oyuncu):
    pass # pass anahtar sözcüğü, herhangi bir subclass'ta superclass'tan alınan özellik ve metotlarda herhangi bir 
         # değişiklik yapılmayacaksa kullanılır. 
isciNesnesi1=Isci("Mehmet Ali Gök", "Kalıpçı")
isciNesnesi1.puanKazan()
class Yonetici(Oyuncu):
    def __init__(self, isim, rutbe):
        # self.ad=isim
        # self.rank=rutbe
        # self.guc=100
        # Burada bu şekilde bir nevi override ederek değiştirebiliriz ancak super() metodu kullanacağız.
        super(Yonetici, self).__init__(isim, rutbe)
        self.guc=150
        # Burada normalde superclass'ta 80 olan guc özelliği 150 olarak değiştirildi.
        # super() metodu ile nesne yönelimli programlama mantığında super class'ların constructor metotlarına erişilir.
        # Öncelikli olarak super() metodunu kullandık ki değiştirmek istediğimiz özelliği scope içinde tanımlı hale getirebilelim.
    def hareketEttir(self):
        print("Bu metot override eden metottur! Normalde 'Hareket ettiriliyor' yazması gerekirdi.")
        # Burada superclass'taki metodu override ediyoruz ve subclass'ın gerektirdiği şekilde kullanabiliyoruz
yoneticiNesnesi1=Yonetici("Mehmet Ali Gök", "İş Analisti")
# Burada super class'ın güç özelliğine erişemiyoruz ancak super() metodu ile bunu yapabiliyoruz.
yoneticiNesnesi1.hareketEttir()
yoneticiNesnesi1.bilgileriGoster() 