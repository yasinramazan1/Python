class Bisiklet():
    hız=0
    vites=1

    def vitesArttır(self):
        print("vites artıyor...")
        self.vites+=1
        print("yeni vites:",self.vites)
    def hızArttır(self):
        print("hız artıyor...")
        self.hız+=1
        print("yeni hız: ",self.hız)

bisikletNesnesi=Bisiklet()
print("Bisikletin ilk hızı: ",bisikletNesnesi.hız)
print("bisikletin ilk durumda vitesi: ",bisikletNesnesi.vites)
bisikletNesnesi.vitesArttır()
bisikletNesnesi.vitesArttır()
bisikletNesnesi.hızArttır()
bisikletNesnesi.hızArttır()
