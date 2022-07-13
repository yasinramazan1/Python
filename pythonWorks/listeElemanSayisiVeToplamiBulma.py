import random
liste=list()
for i in range(random.randint(1,100) ): # randint() metodu çok sık kullanılır ve parantez içerisine yazılan min ve max değerleri arasında rastgele tamsayı (integer) tipinde sayı üretir.
    liste.append(random.random()) # random() metodu 0 <= n < 1.0 aralığında bir sayı döndürür.

x,s=len(liste),sum(liste) # Çoklu atama, len() metodu listenin uzunluğunu, sum() metodu ise listedeki elemanların toplamını verir.
print(x,"tane elemandan oluşan listenin toplamı=",s,"ortalaması=",s/x)
