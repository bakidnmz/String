# String İfadeler İle Çalışma
print(type("3"))
isim = "Baki Dönmez"
print(isim[2])
print(isim[10])
print(isim[0])
print(isim[-1])
# isim[2]= "y" string ifadeler düzenlenemezler. k harfi y harfine dönüşmedi.
a = 'Baki'
b = '''Dönmez'''
print(a+b)
print("Hoşgeldin " + a + " " + b)
print(isim[:])
print(isim[0:4])
print(isim[5:])
print(isim[-6:])
print(isim[2:7])
print(isim[:4])
print(isim[0::2])
print(isim[1::2])
print(isim[2:10:3])
print(isim[2:8:3])
print(isim[::-1])
yeni_isim = isim.replace('Baki', "Nur")
print(yeni_isim)
print(isim)

metin = "Limit Türev İntegral"
print(len(metin))
print(metin.count("i"))
print(metin)
print(metin.upper())
print(metin.lower())
print(metin.capitalize())
print(metin.swapcase())


A = "ve"
print("Ayşe {} Fatma".format(A))  # string ifadeler arasına {} ile format fonk kullanarak veri girilebilir.

yazi = "Python"
for i in range(0, 7):
    print(yazi[:i])
print("*"*7)
yazi = "Python"
print(yazi)
for i in range(1, 7):
    print(yazi[:-i])

harf = ""
b = 0
indis = int(input("Kaçıncı harfi arıyorsunuz: "))
for i in "abcçdefgğhıijklmnoöprsştuüvyz":
    b += 1
    if b == indis:
        harf = i
print(f"Alfabenin {indis}.Harfi : {harf}")

adres = input("Adresinizi giriniz: ")
adres_parcalari = adres.split(" ")  # split fonk. verilen argümana göre ayırma işlemi yapar, varsayılan arg. boşluktur.
# fonksiyona verilen değişkeni listeye dönüştürür.
print(adres_parcalari)
print(adres_parcalari[0])
