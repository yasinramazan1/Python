class Calisan():
    def __init__(self, ad, soyad, maas):
        self.isim=ad 
        # Buradaki değişkenin erişim seviyesi default olarak public'tir. Ancak biz bazen bunu sınırlandırmak isteriz.
        # Bunun için bir örnek gösterim aylikMaas değişkeninde private olarak yapılmıştır.
        self.soyisim=soyad
        self.__aylikMaas=maas # private yapıldı, bu değişkene erişim artık ancak Calisan sınıfından yapılabilir.
    def getMaas(self):
        print(self.__aylikMaas) # Bu şekilde Calisan sınıfından erişim sağladık.
    def setMaas(self,zam):
        self.__aylikMaas=zam+self.__aylikMaas # Bu şekilde de özellik üzerinde değişim yapabiliyoruz.

class Yonetici(Calisan):
    pass
yoneticiNesnesi2=Yonetici("Yasin Ramazan","Gök",10000)
print(yoneticiNesnesi2.isim)
print(yoneticiNesnesi2.soyisim)
# print(yoneticiNesnesi2.aylikMaas) # private yapılmadan önce bu şekilde erişim sağlanabiliyordu.
yoneticiNesnesi2.setMaas(1000)
yoneticiNesnesi2.getMaas()

    