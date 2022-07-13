# Asal Sayıları Hesaplama
def asalMi(sayi):
    bayrak=0
    a=2
    while(a<sayi):
        if(sayi%a==0):
            bayrak=1
            break
        a+=1
    if(bayrak==0):
        print("sayısı asal sayıdır!")
    elif(bayrak==1):
        print("sayısı asal sayı değildir!")       

asalMi(9)

# Fibonacci Sayı Dizisi
def fibonacciHesapla(diziUzunlugu):
    sayi1=0
    sayi2=1
    print("Fibonacci dizisi: "+str(sayi1)+" "+str(sayi2)+" ",end="")
    for i in range(2,diziUzunlugu):
        sayi3=sayi1+sayi2
        sayi1=sayi2
        sayi2=sayi3
        print(sayi3,end="")
        print(" ",end="")

fibonacciHesapla(15)

# Faktöriyel Hesaplama

def faktoriyelHesapla(sayi):
    gosterilecekSayi=sayi
    sonuc=1
    if(sayi==sonuc):
        print("\n1'in faktöriyeli 1'dir!\n0'ın faktöriyeli 1'dir!")
    elif(sayi<0):
        print("\nLütfen negatif olmayan bir sayı giriniz!")
    else:
        while(0<sayi):
            sonuc=sonuc*sayi
            sayi-=1
        print("\n{} sayısının faktöriyeli: {}'dir.".format(gosterilecekSayi,sonuc))

faktoriyelHesapla(5)

# Rekürsif Fonksiyonlar Örnek-1
def recursiveOne(sayi):
    if(sayi==1):
        return 1
    return recursiveOne(sayi-1)+sayi

print(recursiveOne(8))

# Rekürsif Fonksiyonlar Örnek-2
def recursiveSecond(sayi):
    if(sayi==0):
        return 0
    if(sayi%2==0):
        return recursiveSecond(sayi-2)+sayi
            
print(recursiveSecond(6))
        
    