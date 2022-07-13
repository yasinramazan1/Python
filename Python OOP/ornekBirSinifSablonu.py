class StajBasvurusu():
    def __init__(self,stajıYapan,stajAdı,stajYeri,stajGunSayısı):
        self.ogrenciAdı=stajıYapan
        self.stajIsmi=stajAdı
        self.yer=stajYeri
        self.gunSayısı=stajGunSayısı
    def bilgileriGoster(self):
        print("Öğrenci Adı: ",self.ogrenciAdı)
        print("Staj Adı: ",self.stajIsmi)
        print("Staj Yeri: ",self.yer)
        print("Staj Gün Sayısı: ",self.gunSayısı," İş Günü")
    def bigileriDegistir(self,stajAdı):
        self.stajIsmi=stajAdı


        

stajNesnesi=StajBasvurusu("Yasin Ramazan Gök", "Zorunlu Staj-1", "Ankara", 30)
stajNesnesi.bilgileriGoster()
print("*************************************************")
print("Bilgilerde değişiklik yapıldı! Güncel bilgileriniz aşağıdadır!")
stajNesnesi.bigileriDegistir("İş Yeri Eğitimi")
stajNesnesi.bilgileriGoster()
