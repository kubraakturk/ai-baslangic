# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello AI ERA")

10
12.3
a*3
"a"*3
"a" + "k"
# Cancağızım yanımda olsa
type("a")
type(34)

gel_yaz = "gelecegi_yazanlar"
# del a

p = 6
k = 5
p*k

len(gel_yaz)
len("gelecegi_yazanlar")

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()
B = gel_yaz.upper()

B.isupper()
B.islower()

gel_yaz.replace("e", "a")
gel_yaz
# atama işlemi yapmadığımız için değişiklik olmaz

gel_yaz = "*gelecegi_yazanlar*"
gel_yaz
gel_yaz.strip()
gel_yaz.strip("*")
dir(gel_yaz)

gel_yaz = "gelecegi_yazanlar"
gel_yaz.capitalize()
gel_yaz.title()

gel_yaz[0]
gel_yaz[20]
gel_yaz[0:3]

type(1+2j)
type(100.5)
type(19)


toplama_bir = input()
toplama_iki = input()

type(toplama_bir)
toplama_bir+toplama_iki

int(toplama_bir)+int(toplama_iki)

float(12)
type(float(12))

print("Hello AI ERA")
print("hello", "space")
print("hello", "sun", sep="_")
# fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belirticilere
# argüman denir.
print()
"10" + 2
"_Python_".strip("_")

ifade = "gelecegi yaziyoruz"
ifade[0:2]

"9" + 1

ifade = "gelecek_geldi"
ifade.replace("i", "ı")

degisken = 4
degisken*degisken

ifade = "Merhaba!"
ifade = ifade.lower()
ifade = ifade.replace("!", "")
ifade

ifade = "Merhaba! "
ifade.strip("")
type(4)



# Veri Yapıları

# Listeler

notlar = [45, 56, 78, 96]
type(notlar)

liste = ["a", 34, "b", 45]
liste_genis = ["a", 34, "b", 45, notlar]
len(liste_genis)

liste_genis[0]
liste_genis[3]

type(liste_genis[4])

tum_liste = [liste, liste_genis]
# del tum_liste

string_liste = ["ali", "veli", "berkcan", "ayse"]
string_liste

string_liste[1] = "velinin_babasi"
string_liste

string_liste[:3] = "alinin_babasi", "velinin_babasi", "berkcanin_babasi"

string_liste

string_liste = string_liste+["pohli_got"]
string_liste

dir(string_liste)

string_liste.append("berkcan")
string_liste

string_liste.remove("berkcan")
string_liste

string_liste.insert(0, "kubra")

string_liste.insert(len(string_liste), "sona_ekleme")
string_liste

string_liste.pop(0)
string_liste

string_liste.count("sona_ekleme")

kopya_liste = string_liste.copy()
kopya_liste

string_liste.extend(["a", "b", 10])
string_liste

string_liste.remove(10)

string_liste.index("pohli_got")

string_liste.reverse()
string_liste

string_liste.sort()

string_liste.clear()
string_liste

# Listeler 1.Kapsayıcıdır 2.Sıralıdır 3.Değiştirilebilir

# Tuple

# Listelerden farklı olarak değiştirilemezdir.

t = ("ayı", "balı", 12, 4.6, [1, 2, 3, 4])
t = "ayı", "balı", 12, 4.6, [1, 2, 3, 4]
t = ("eleman",)
type(t)

t[1]
t[0:3]

# Dictionary (Sozluk)

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

len(sozluk)

sozluk = {"REG": [10, "RMSE"],
          "LOJ": [20, "MSE"],
          "CART": [30, "SSE"]}

sozluk = {"REG": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30},

          "LOJ": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30},

          "CART": {"RMSE": 10,
                   "MSE": 20,
                   "SSE": 30}}

sozluk["LOJ"]["SSE"]


sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk[1] = "Yapay Sinir Aglari"
sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk
# Not: Sozluklerde key yapıları sadece sabit değerler ile oluşturulur.
# örn:int,str,tuple
# listeler key olarak atılamaz.

t = ("tuple",)
sozluk[t] = "Yeni bir sey"
sozluk


# Setler

s = set()
s

l = [123, "ali", "veli", 1]

s = set(l)
s

t = ("a", "ali", 56)
s = set(t)

ali = "ali_lütfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali)
s

liste = ["ali", "veli", "berkcan", "ayse"]
l

s = set(liste)
s

l[0]
s[0]  # TypeError: 'set' object is not subscriptable hatasını verir.
# set elemanlarını kendisi sıralar ve index işlemini desteklemez.

l = ["gelecegi", "yazanlar"]

s = set(l)

dir(s)
s.add("ile")
s.add("python")
s

s.add("kübra")
s.add("kübra")
s
s.remove("kübra")
s
# silinecek eleman varsa silsin yoksa hata vermeden devam etsin.
s.discard("kübra")


# Setler - Klasik küme işlemleri

# difference() ile iki kümenin farkını buluyoruz. İkinci yönten '-' iledir.
# intersection() iki küme kesişimini bulur. İkinci yöntem '&' iledir.
# union() iki kümenin birleşimini
# symmetric_difference() iki kümede de olmayanları birden gösterir.

set1 = set([1, 3, 5])
set2 = set([1, 2, 3, 5])

set1.difference(set2)
set2.difference(set1)

set1 - set2
set2 - set1

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

set1.intersection(set2)
set2.intersection(set1)

kesisim = set1 & set2
kesisim
birlesim = set1.union(set2)
birlesim
set1.intersection_update(set2)
set1
set2

set1 = set([1, 3, 5])
set2 = set([1, 2, 3, 5, 7, 8, 9, 10])

# iki kümenin kesişiminin boş olup olmamasını kontrol ediyor.
set1.isdisjoint(set2)

# Bir kümenin diğerinin alt kümesi olup olmadığını kontrol eder.
set1.issubset(set2)

set1.issuperset(set2)  # bir kümenin diğerini kapsadığının kontrolünü yapar.

set1 = set([5, 7, 9])
set2 = set([5, 6, 7])
set1.difference(set2)


liste = ["a", "b", "c"]
liste.reverse()
print(liste)

liste = [10, 10, 20, 40]
liste.clear()
liste

set1 = set([5, 7, 9])
set2 = set([5, 6, 7])
set1.symmetric_difference(set2)

set1 = set([5, 7, 9])
set2 = set([5, 6, 7])
set1.union(set2)


liste = ["a", "b", "c"]
liste.index("b")

sozluk = {"REG": {"RMSE": 10,
                  "MSE": 11,
                  "SSE": 12},

          "LOJ": {"RMSE": 111,
                  "MSE": 2222,
                  "SSE": 333},

          "CART": {"RMSE": 99,
                   "MSE": 00,
                   "SSE": 66}}

sozluk["CART"]["SSE"]

t = ("a", 10, "b")
t[0] = 1

liste = ["a", "b", "c"]
liste.extend(liste)
liste

liste = [50, 10, 30, 40]
liste.sort()
liste

set1 = set([5, 7, 9])
set2 = set([5, 6, 7])
set1.union(set2)

liste = [10, 20, 30, 40]
liste.pop(1)
liste


print("a", "b", sep="_")
#?print
print()


# Fonksiyonlar

4**2


def kare_al(x):
    print(x**2)


kare_al(4)


def kare_al_ekrana_yaz(x):
    print("Girilen sayı: "+str(x)+"\nKaresi: "+str(x**2))


kare_al_ekrana_yaz(4)

def carpma_yap(x,y):
    print(x*y)

carpma_yap(2, 3)

#Argümanların sıralanması

#ön tanımlı olarak y'ye 1 atadık.Bu yüzden tek parametreli olarak çalıştı.
def carpma_yap(x,y=1):
    print(x*y)
    
carpma_yap(3)

#parametrelerin sırasını unuttuğunda şöyle çağrılabilir.
carpma_yap(y=2,x=3)

def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

cikti= direk_hesap(25, 34, 56)
print(cikti)

x=10 #global değişken
y=20 #global değişken

def carpma_yap_localde(x,y):
    return x*y

carpma_yap_localde(2, 7) # 2 ve 7 local değişken olarak hesaplanır. 

#localden global değişkene erişilebilir.
global_degisken = []

def eleman_ekle(eklenecek_eleman):
    global_degisken.append(eklenecek_eleman)
    print(str(eklenecek_eleman)+" ifadesi eklendi")

eleman_ekle(5)
global_degisken
eleman_ekle("kübra")
global_degisken


#if-elif-else 

sinir=50000
magaza_adi=input("Mağaza adı nedir?")
gelir = int(input("Geliri giriniz:"))

if gelir > sinir:
    print("Tebrikler "+magaza_adi+" promosyon kazandınız!")
elif gelir < sinir:
    print("Uyarı! Düşük gelir: "+ str(gelir))
else:
    print("Takipte kalalım")

#maaşlara yüzde 20 zam yapalım
maas=[10000,20000,30000,40000,50000]

def yeni_maas(x):
    print(x*20/100 + x)

yeni_maas(maas[0])

for i in maas:
    yeni_maas(i)

#maaşı 30000den az olana yüzde 20 ; çok olana yüzde 10 zam yapalım

maas=[10000,20000,30000,40000,50000]

def maas_ust(maas):
    print(maas*10/100+maas)
    
def maas_alt(maas):
    print(maas*20/100+maas)

for i in maas:
    if(i >= 30000):
        maas_ust(i)
    else:
        maas_alt(i)

#break continue

maaslar=[4000,5000,2000,1000,1000,6000,3000]

maaslar.sort()
maaslar

for i in maaslar:
    if i==3000:
        print("kesildi")
        break
    print(i)

for i in maaslar:
    if i==3000:
        print("devam kee")
        continue
    print(i)


#while

sayi=1

while sayi < 9:
    sayi += 1
    print(sayi)
    
print(sayi)


def yazdir(metin):
    print(metin, "yazanlar")
 
yazdir("gelecegi")

a = [1,2,3]
b = []
for i in a:
    b.append(i**2)
b

A = "*A*"    
if type(A) == str:
    A = A.strip("*")
    print(A)

def islem(x, y):
    print(x + y)
 
islem(1,9)

def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)


A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())


sayilar = [10,20,30]
 
for i in sayilar:
    if i > 20:
        print(i/2)

def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")


A = []
B = []

for i in [1,"a",12,"b"]:
    if type(i) == int:
        B.append(i)
    else:
        A.append(i)

A[1]

def mesaj():
    print("Merhaba!")    
    
mesaj() 

A = []

for i in [1,2,3,4]:
    A.append(i)

A[0]

a = [2,4,6,8]
for i in a:
    print(i**2)

#Sınıflar

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
VeriBilimci.bolum
VeriBilimci.sql

VeriBilimci.deneyim_yili=1
VeriBilimci.deneyim_yili

# Örnek Özellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"] #Sınıf özelliği
    bolum=''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = [] # örnek özelliği
        self.bolum= ''

#Sınıf özellikleri ile örnek özelliklerini farklı isimlendirebiliriz. Fakat henüz yapmadık.

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("object")
ali.bildigi_diller

VeriBilimci.bildigi_diller


#Örnek Metodları

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=''
    def dil_ekle(self , yeni_dil):
        self.bildigi_diller.append(yeni_dil)


ali = VeriBilimci()
ali.bildigi_diller.append("R")
ali.bildigi_diller
ali.dil_ekle("Python")
ali.bildigi_diller


#Miras Yapıları (Inheritance)


class Employees():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        
veribilimci = DataScience()
veribilimci.Address = "djf"
veribilimci.Address


class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""


satis = Marketing()
satis.StoryTelling = "jkdsc"

#Fonksiyonel programlama

#Olumcul yan etkiler
# ornek oop
class LineCounter():
    def __init__(self , filename):
        self.file = open(filename,'r')
        self.lines = []
        
    def read (self):
        self.lines = [line for line in self.file]
            
    def count (self):
        return len(self.lines)

lc = LineCounter("deneme.txt")
print(lc.lines)
print(lc.count())

lc.read() # okuma yapmadan satırar gelmedi

print(lc.lines)
print(lc.count())


#ornek fonksiyonel programlama

def read(filename):
    with open("deneme.txt",'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)


example_lines = read("deneem.txt")
lines_count = count(example_lines)
lines_count


# İsimsiz fonksiyonlar

def old_sum(a,b):
    return a+b

old_sum(4, 5)


new_sum = lambda a,b : a+b
new_sum(4,5)

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste, key= lambda x:x[1])

#Vektörel Operasyonlar

#OOP 
a=[1,2,3,4]
b=[2,3,4,5]

ab = []

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
ab

#FP

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

# map & filter & reduce

liste = [1,2,3,4,5]

for i in liste:
    print(i*10)

list(map(lambda x: x*10,liste))

# filter
liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x:x%2==0, liste))

#reduce
from functools import reduce

liste=[1,2,3,4]
reduce(lambda a,b: a+b,liste)

# modul ekleme

import HesapModulu

HesapModulu.yeni_maas(1000)

import HesapModulu as hm
hm.yeni_maas(hm.maaslar[2])

from HesapModulu import yeni_maas
yeni_maas(4000)

hm.maaslar

# Hatalar / istisnalar ( exceptions)

a = 10
b = 0

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("Payda sifir olamaz")

#tip hatasi ornek

a= 10
b="2"

a/b

try:
    print(a/b)
except TypeError:
    print("Sayi string bir ifadeye bolunemez")

a= 10
b=2

a/b

try:
    print(a/b)
except TypeError:
    print("Sayi string bir ifadeye bolunemez")

list(map(lambda x: x.capitalize(), ["abc","bcd","cde"]))

import numpy as np
a = np.array([1,1,1])
b = np.array([2])

a+b

list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50])))

A = [1,2,3,4,5]

if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))

from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)


liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))

from functools import reduce
reduce(lambda a,b: a/b, [8,4,2])


list(map(lambda x: x*1, [2,7,4]))


from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])



fun = lambda x: x**2
fun(3)

a = [1,2,3]
list(map(lambda x: x*2, a))


A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i)))  




A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]


for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x-3, i)))





list(filter(lambda x: x < 2, [1,2,3,4,5]))


list(map(lambda x: x.upper(), ["Ali","Veli","isik"]))


from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))





