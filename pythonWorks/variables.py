# Değişken tanımlama kuralları
# -Büyük küçük harf duyarlılığı vardır.
# -Türkçe karakter kullanılmaz.
# -Sayı ile başlayamaz.
# kucukHarfleBaslamaliVeCamelCaseKullanilmali
name = "Yasin Ramazan"
surname="GÖK"
age=24
print('My name is '+name+" "+surname+" and I am "+str(age)+" years old!")
array='My name is '+name+" "+surname+" and I am "+str(age)+" years old!"
uzunluk=len(array)
print(array[uzunluk-1]) # Dizinin son elemanını yazdırma
print(array[1])
print(array[-4])
print(array[2:5]) # 5'e kadar ama 5 dahil değil.
print(array[2:]) 
print(array[:15]) 
print(array[2::3]) 