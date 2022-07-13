a=1
b=2 #sıradaki fibonacci sayısı
for x in range(100):
    c=a+b
    a,b=b,c  #çoklu atama
    print(c)
