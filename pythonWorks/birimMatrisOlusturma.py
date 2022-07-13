#nxn Birim matris oluşturma
n=5
x=list()
for i in range(n):
    y=list()
    for j in range(n):
        y.append(1) if i==j else y.append(0)  # if-else satır içi kullanımı
    x.append(y)
    
for i in x:
    print(i)
