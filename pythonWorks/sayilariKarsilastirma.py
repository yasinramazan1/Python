# 100 adet random sayıdan birbirlerine en yakın olanı bulma(Farkları minimum olanlar)
import random
sayilar=list()
minimum=1 # minimum değişkeninin başlangıç değeri
liste=[random.random() for i in range(10)] # Random listeyi oluşturma
for x in liste[0:len(liste)-1]:                      # Her sayıyı listedeki bir sonraki sayı ile karşılaştırıyoruz
    for y in liste[(liste.index(x)+1):len(liste)]:   # Karşılaştırma işlemi listenin sonuna kadar her eleman için yapılacak
        if abs(x-y) <minimum:                        # Farkların mutlak değerini alıyoruz
            sayilar[:2]=[x,y]                        
            minimum=abs(x-y)


print("minumum fark=",minimum)
print("en yakin sayilar=",sayilar)
print("tüm liste=",liste)
