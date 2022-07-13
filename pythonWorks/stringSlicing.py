from typing import Text
# string slicing karakter dizilerini dilimlemedir.
name="Yasin Ramazan"
surname='GÖK'
age="24"
text = "Benim adım " + name + " soyadım " + surname + " yaşım " + age
print(text)
print(text[0])
print(text[3])
print(text[-5])
print(text[0:5]) # 0'dan başlayıp 5'e kadar ( 5 dahil değil ) ekrana yazdır demektir!
print(text[6:13])
print(text[:10]) # 10. indekse kadar ( 10. indeks dahil değil! ) al, ekrana yazdır!
print(text[4:]) # Başlangıcı belirtmeden bitişe kadar ekrana yazdırır!
print(text[-15:-1])
print(text[4:18:3]) # artış miktarı belirterek ekrana yazdırma 
print(text[::2])
print(text[::-1])  
print(text[::]) # sağdan sola sadece artış miktarı ile ekrana yazdırır!
