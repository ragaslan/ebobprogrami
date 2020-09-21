import time
print("***EBOBU BULMA PROGRAMI***\nEBOBUNU BULMAK İSTEDİĞİNİZ İKİ SAYIYI GİRİN")
time.sleep(1)
sayi1 = int(input("İlk sayıyı girin "))
sayi1_bolen = []
sayi2 = int(input("Bir sayı daha girin "))
sayi2_bolen = []
for i in range(1,sayi1+1):
    if sayi1 % i == 0:
        sayi1_bolen.append(i)

for a in range(1,sayi2+1):
    if sayi2 % a == 0:
        sayi2_bolen.append(a)
sayi1_bolen.reverse()
for e in sayi1_bolen:
    if (e in sayi2_bolen) == True:
        print("Bu iki sayının EBOBU {} ".format(e))
        break