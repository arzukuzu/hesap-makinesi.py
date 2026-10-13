
#  Gelişmiş Hesap Makinesi (Python)

Bu proje; temel ve ileri düzey matematiksel işlemleri gerçekleştiren, kullanıcı kaynaklı hatalara karşı korumalı (try-except) modüler bir konsol uygulamasıdır.

---

##  Proje Özellikleri

- **Güvenli Girdi Kontrolü:** Sayısal olmayan girişlerde program çökmez, kullanıcıdan tekrar giriş ister.
- **Sıfıra Bölme Koruması:** Bölme ve mod alma işlemlerinde paydanın 0 olması durumu kontrol edilir.
- **Tip Dönüşümü:** İşleme göre dinamik olarak tam sayı (`int`) veya ondalıklı sayı (`float`) kabul eder.
- **Negatif Sayı Kontrolü:** Faktöriyel hesabında negatif sayılar engellenir.

---

##  Desteklenen İşlemler

| No | İşlem | Açıklama |
| :---: | :--- | :--- |
| **1** | Toplama | İki sayıyı toplar |
| **2** | Çıkarma | İki sayının farkını alır |
| **3** | Bölme | Sıfıra bölme kontrollü bölme işlemi |
| **4** | Üs Alma | Sayının kuvvetini hesaplar |
| **5** | Mod Alma | Kalan bulma işlemi |
| **6** | Faktöriyel | Pozitif tam sayıların faktöriyeli |
| **7** | Çıkış | Programı sonlandırır |

---

##  Örnek Çalışma Çıktısı

```text
Yaptırmak istediğiniz işlemi seçiniz. 
1-Toplama 
2-Çıkarma 
3-Bölme 
4-Üs Alma 
5-Mod Alma 
6-Faktoriyel Alma 
7-Çıkış

Seçiminiz : 6
1. sayıyı giriniz: 5
120
