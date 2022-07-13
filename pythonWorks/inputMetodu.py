print("Lütfen bir tamsayı giriniz: ",end="")
a=int(input()) # input() metoduna cast işlemi uygulandığında belirtilen türde değer girilmelidir. Aksi takdirde ValueError hatası alınır.
# a=int(input("Lütfen bir tamsayı giriniz: "))
print("Girdiğiniz sayı: {}".format(a), end=" Girdiğiniz sayının veri türü: {0}".format(type(a)))
