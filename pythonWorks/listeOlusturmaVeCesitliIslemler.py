# Listeler farklı türde verileri aynı anda tutabilen ve içeriği dinamik olan bir veri türüdür.
a=list() # boş liste tanımlama
# a=[]
""" 
# %%
....
...
...
...
# %% 
şeklinde section yaparak kodları bölümlemeye ve 
sadece ihtiyaç duyulduğunda 
o bölümdeki kodları çalıştırmaya yarar.
"""
print("a öğesinin veri türü: ",end="")
print(type(a))
for i in range(1,11): # 11 dahil değildir.
    a.append(i)
    i+=1 

# print(a) # Listeyi ekrana yazdırma
# print(a[3]) # Belirtilen indeksteki değeri ekrana yazdırma, indeks değeri tamsayı olmalıdır ve listelerde zero based indexing yaklaşımı vardır.
# print(a[-1]) # Listenin son elemanını döndürür.
# print(a[-2]) # Listenin sondan ikinci elemanını döndürür.
"""
uzunluk=len(a) # len() metodu listenin uzunluğunu int türünden geri döndürür.
print(uzunluk)
print(len(a))
"""
"""
print(a)
a.append("Yasin Ramazan GÖK") # Listenin sonuna yeni eleman ekleme
print(a)
"""
"""
a.append("Yasin Ramazan GÖK")
t=a.index("Yasin Ramazan GÖK") # index() metodu girilen parametrenin indeks numarasını int türünden geri döndürür.
print(t)
"""
"""
del a[-1] # del komutu ile belirtilen indeksteki eleman listeden silinir.
a.sort() # Listeyi sıralar.
print(a)
a.reverse() # Listeyi ters çevirir.
print(a)
a.pop() # Listenin en son elemanını siler.
print(a)
a.insert(2,"YRG") # Belirtilen indeks numarasına belirtilen değeri ekler.
print(a)
print(a.count(7)) # count() metodu parametre olarak girilen değerin listede kaç defa tekrar ettiğini int türünden geri döndürür.
a[-1]="Yasin Ramazan GÖK" # son elemana belirtilen değeri atar.
print(a)
del a[6]
print(a)
a.remove("YRG") # remove() metodu parametre olarak girilen elemanı listeden kaldırır.
print(a)
"""
b=[] # Boş liste oluşturmanın diğer bir yolu bu şekildedir.
i=0
while i<len(a):
    b.append("Yasin Ramazan GÖK")
    i+=1
a.extend(b) # extend() metodu iki listeyi birleştirir.
c=a+b # + operatörü ile de listeler birleştirilebilir.
d=a.copy()
print(b)
print(a)
print(c)
print("d listesine kopyalanmış a listesi: ",d)
# dir(a)
# help(b)
c=list()
c.append("Kuş")
c.append("Memeli")
c.append(1)
c.append(29)
c.append(234.234123)
x=True
c.append(x)
y=False
c.append(y)
print("C Listesi: ",end="") # end komutu ile alt satıra geçmeyi engelliyoruz.
for i in range(0,len(c)):
    eleman=c[i]
    print(eleman)
    i+=1
print("C Listesinin elemanlarının veri türleri: ")
for i in range(0,len(c)):
    dataType=type(c[i])
    print(dataType)
    # print(type(c[i])) # Bu şekilde de yazılabilir.
    i+=1








