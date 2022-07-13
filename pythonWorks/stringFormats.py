name="Yasin Ramazan"
surname='GÖK'
age="24"
print("My name is {} {}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {n} {s}".format(n=name, s=surname))
print("My name is {s} {n}".format(n=name, s=surname))
print("My name is {} {}. I'm {} years old.".format(name, surname,age))
print("My name is {2} {0}. I'm {1} years old.".format(name, surname,age))

numbers = 23/3
print("the division result is {t:1.2}".format(t=numbers)) 
 
print(f"My name is {name} {surname} and I'm {age} years old!")

a=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
print(a)
print("Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık", sep=";")
print("Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık", sep=None)
