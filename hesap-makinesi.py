def sayi_al(mesaj, tam_sayi = False):
    while True:
        deger = input(mesaj)
        try:
            if tam_sayi:
             return int(deger)
            else:
             return float(deger)
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı giriniz.")    

def topla(x,y):
    sonuc = x+y
    return sonuc

def cikar(x,y):
    sonuc = x-y
    return sonuc

def böl(x,y):
    if y == 0:
        return None
    sonuc = x / y
    return sonuc


def üs_al(x,y):
    sonuc = x ** y 
    return sonuc

def mod_al(x,y):
    if y == 0:
     return None
   
    sonuc = x % y
    return sonuc

def faktoriyel(x):
    if x < 0:
       return "Negatif sayının faktoriyeli alınmaz."
    sonuc = 1
    for i in range(1,x+1):
        sonuc *= i
    return sonuc


while True:
    print("Yaptırmak istediğiniz işlemi seçiniz. \n1-Toplama \n2-Çıkarma " \
    "\n3-Bölme \n4-Üs Alma \n5-Mod Alma \n6-Faktoriyel Alma \n7-Çıkış")

    secim = sayi_al("Seçiminiz :" , tam_sayi= True)

    if secim == 1:
        x = sayi_al("1. sayıyı giriniz: ")
        y = sayi_al("2. sayıyı  giriniz: ")
        print(topla(x,y))
        
    elif secim == 2:
        x = sayi_al("1. sayıyı giriniz: ")
        y = sayi_al("2. sayıyı  giriniz: ")
        print(cikar(x,y))

    elif secim == 3:
        x = sayi_al("1. sayıyı giriniz: ")
        y = sayi_al("2. sayıyı  giriniz: ")      
        sonuc = böl(x,y)
        if sonuc is None:
           print("Payda sıfır olamaz.")
        else:
           print(sonuc)  

    elif secim == 4:
        x = sayi_al("1. sayıyı giriniz: ")
        y = sayi_al("2. sayıyı  giriniz: ")
        print(üs_al(x,y)) 

    elif secim == 5:
        x = sayi_al("1. sayıyı giriniz: ")
        y = sayi_al("2. sayıyı giriniz: ")
        sonuc = mod_al(x, y)
        if sonuc is None:
          print("Payda 0 olamaz.")
        else:
          print(sonuc)
        

    elif secim == 6:
        x = sayi_al("1. sayıyı giriniz: " , tam_sayi=True)
        print(faktoriyel(x))

    elif secim == 7:
        break       

    else: 
        print("Geçersiz seçim yaptınız.")    