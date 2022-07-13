def bilgileriAyıkla():
    dosya=open("E:\\CS LANGUAGES\\PYTHON\\Python OOP\\fonksiyonVeDosyaIslemleriOrnekMetin.txt","r")
    dosya2=open("temizlenenler","w")

    for line in dosya:
        for character in line:
            if(character!=" "):
                dosya2.write(character)
            elif(character==" "):
                dosya2.write("\n")
                break
    dosya2=open("temizlenenler","r")
    print(dosya2.read())
    dosya2.close()
def kontrol():
    dosya3=open("temizlenenler","r") # Okuma modunda temizlenenler dosyasını açtık.
    kontrolDosyası=open("kontrol","w") # Burada kontrol isimli yeni bir text dosyası oluşturduk.
    kontrolListesi=[] # Boş liste tanımladık.
    for line in dosya3:
        if line not in kontrolListesi: 
            kontrolDosyası.write(line)
            kontrolListesi.append(line)
kontrol()
bilgileriAyıkla()