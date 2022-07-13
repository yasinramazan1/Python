name="Yasin Ramazan"
surname="GÖK"
age=24
print('My name is {} {}'.format(name,surname))
print('My name is {1} {0}'.format(name,surname))
print('My name is {n} {s}'.format(n=name,s=surname))

result =200/700
print('the result is {r:5.4}'.format(r=result)) 
print('the result is {r:10.4}'.format(r=result)) 
# Burada 5, sayı için kaç karakterlik 
# boşluk bırakılacağını; 4 ise virgülden sonra kaç basamak 
# alınacağını belirler. Sağa hizalı çıktı verir.
print(f"My name is {name} {surname} and I'm {age} years old.")

