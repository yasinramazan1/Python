yazi="      benim adım Yasin Ramazan GÖK.Hatay'da yaşıyorum.  "
sonuc= yazi.upper()
print(sonuc)
sonuc=yazi.lower()
print(sonuc)
sonuc=yazi.title()
print(sonuc)
sonuc=yazi.capitalize() # Cümlenin ilk harfini büyük yapar!
print(sonuc)

sonuc=yazi.islower() # bool değer döndürür.
print(sonuc)
sonuc= yazi.strip() # Baştaki ve sondaki boşlukları siler.
print(sonuc)
sonuc= yazi.split() # stringi split() metoduna girilen parametreyi algılayacak şekilde dizi elemanlarına dönüştürür.
print(sonuc)
sonuc= "-".join(yazi)
print(sonuc)
sonuc=yazi.index("Yasin")
print(sonuc)
sonuc=yazi.startswith("Yasin")
print(sonuc)
sonuc=yazi.endswith("Yasin")
print(sonuc)
sonuc=yazi.replace("Yasin","YRG")
print(sonuc)
sonuc=yazi.replace("ı","i".replace("ş","s".replace("ö","o")))
print(sonuc)








