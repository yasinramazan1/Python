# Metot kendisine gelen sayı asal ise True döndürecek, parametre verilmez ise default değer 2 alınacak.
def asalmi(x=2):
    asal=True
    for i in range(2,x):
        if x%i==0:
            asal=False
            break
    return asal
x=7
if asalmi(x):
    print(x," Asal sayıdır!") 
else:
    print(x,"Asal sayı değildir!")
print(asalmi()) # Parametresiz çağrılınca x=2 default değer geçerli olacak.
