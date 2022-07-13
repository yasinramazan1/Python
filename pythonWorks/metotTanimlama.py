def kareAl():
    a=int(input("Lütfen karesini almak istediğiniz sayıyı giriniz: "))
    kare=a*a
    print("Girilen sayının karesi: ",end="{}".format(kare))

kareAl()
a=int(input("Lütfen kuvvetini almak istediğiniz sayıyı giriniz: "))
b=int(input("Lütfen kuvveti giriniz: "))
def kupHesapla(a,b):
    kup=a**b
    print("{0} sayısının {2}. kuvveti: {1}'dir.".format(a,kup,b))
kupHesapla(a,b)
