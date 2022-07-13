import random
dosya=open("sayilar.txt","w")
a=0
while(a<100):
    a+=1
    rnd=random.randrange(0,100)
    rst=str(rnd)
    dosya.write(rst)
    dosya.write("\n")
dosya.close()

dosya=open("sayilar.txt","r")
dosya2=open("sayilar2.txt","w")
for line in dosya:
    line2=int(line)
    if(line2%2==0):
        dosya2.write(str(line2))
        dosya2.write("\n")
dosya.close()
dosya2.close()