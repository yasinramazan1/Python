from turtle import *

def dikdörtgenCiz(uzunKenar, kısaKenar, renk, cizgiKalinligi):
    color(renk)
    width(cizgiKalinligi)
    for i in range(4):
        if i%2==1:
            k=kısaKenar
        else:
            k=uzunKenar
        forward(k)
        left(90)

def eskenarUcgenCiz(kenar, renk, cizgiKalinligi):
    color(renk)
    width(cizgiKalinligi)
    for i in range(3):
        forward(kenar)
        left(120)

def baslangicNoktasinaGit(x,y):
    penup()
    goto(x,y)
    pendown()

if __name__ == "__main__":
    baslangicNoktasinaGit(-200, 0)
    dikdörtgenCiz(200, 100, 'red', 10)
    baslangicNoktasinaGit(0, 0)
    eskenarUcgenCiz(150, 'purple', 15)   
    done()