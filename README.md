# Veri Depolama ve Sıkıştırma Algoritmaları

## Öğrenci Bilgileri
**Ad Soyad:** Mahmoud Esam I Alfalah  
**Öğrenci Numarası:** 24360859821

## Proje Başlığı
**2. Grup: Veri Depolama ve Sıkıştırma Algoritmaları**

## Video Linki
🎥 [Proje Tanıtım Videosu](https://youtu.be/8tUiXLES65Y)

---

## Kodun Detaylı Açıklaması

### 1. Encoder Fonksiyonu (Kodlama)
**Amaç:** Metni sıkıştırma, örnek: `AAABB` → `3A2B`

#### Kodun Çalışma Mantığı:

**Değişkenler:**
- `current`: Şu anda sayıldığımız harf
- `counter`: Her harfin kaç kere yazıldığını sayan değişken
- `result`: Sonucu tutan değişken

**Algoritma Adımları:**

1. Kullanıcının girdiği metni tek tek dolaş
2. Her iterasyonda:
   - Eğer `i == current` ise, demek ki hala aynı harfi sayıyoruz, `counter` değişkenini artır
   - Eğer `i != current` ise, farklı bir durumla karşılaştık:
     - **Eğer `counter > 0` ise:** Demek ki daha önce saydığımız harf var, ve bu iterasyonda farklı bir harf ile karşılaştık, dolayısıyla sonuca ekleme yapmalıyız: `result += f"{counter}{current}"`
     - **Yoksa:** Birinci harf demektir ve hala herhangi bir sayma işlemi yapmadık
   - Yeni harfe geç: `counter = 1` ve `current = i` olur, yani yeni bir harf ile sayma işlemi başladık

3. **Son adım:** Son harften sonra başka bir iterasyonu olmayacağı için, son harfi ve sayısını eklememiz lazım, çünkü her zaman ekleme işlemi sonraki iterasyonda olur
   - `result += f"{counter}{current}"`
   - Kullandığım ekleme yöntemi f-string ile yapıldı

### 2. Decoder Fonksiyonu (Kod Çözme)
**Amaç:** Sıkıştırılmış metni açma, örnek: `3A2B` → `AAABB`

#### Kodun Çalışma Mantığı:

**Değişkenler:**
- `result`: Sonucu tutan değişken
- `count`: Sayaç değişkeni, ve string olarak başlatıldı çünkü birden fazla basamaklı sayılar olabilir, ve o durumda sayıyı string olarak tutup sonra int'e çevireceğiz

**Algoritma Adımları:**

1. Kullanıcının girdiği metni tek tek dolaş
2. Her iterasyonda:
   - **Eğer `i.isdigit()` true ise:** i'inci karakter sayı ise, `count` değişkenine ekle (string concatenation): `count += i`
     - `isdigit()` fonksiyonu bir karakter sayı olup olmadığını belirten bir methodtur
     - Ayrıca kendi fonksiyonumuz da oluşturabiliriz try, except ve int() kullanarak
   
   - **Yoksa:** Count değişkenini int'e çevir ve i karakteri ile çarp
     - Burada **try-except** kullanıldı, çünkü birinci iterasyonda eğer i'inci karakter sayı değil ise, count hala boş string olacak ve `int("")` hata verecek
     - **ValueError** durumunda: Hata verdi ise, demek ki bu birinci karakter ve count hala boş ve sadece bir kez yazmak istemiş, önce 1 yazmayı unutmuş ve o anda count'u 1 tamamlıyoruz
       - Örnek: Girdiği metin `A3B`, sonuç `ABBB` olmalı
     - Sonucu güncelle: `result += i * count`
     - Count'u sıfırla: `count = ""`

### 3. Ana Program Akışı

#### Kullanıcı Girdisi (Metin):
```python
while True:
    inp = input("Lutfen metni giriniz: ")
    if len(inp) == 0:
        print("gecersiz!!")
        continue
    break
```
Bu döngüde sonsuz bir döngü, kullanıcıdan bir metin okuyup kontrol eder, eğer geçerli bir metin girdi ise (`len(inp) != 0`), döngüyü kırar, yoksa geçersiz uyarısı verir ve yine metin ister.

#### İşlem Türü Seçimi:
```python
while True:
    p_type = input("Yapilacak islem, Encoding/Decoding (E/D): ").upper()
    if p_type not in ['E', 'D']:
        print("Islem E/D olmalidir!!")
        continue
    else:
        break
```
Bu döngüde sonsuz bir döngü, kullanıcıdan işlem türü okuyup `[E/D]`, ve `.upper()` methodu ile her zaman büyük harfine çevirir kontrol etmek için. Girdiği e, E, d, D ise, döngüyü kırar, yoksa geçersiz uyarısı verir ve yine metin ister.

#### İşlem Yapma ve Sonuç:
```python
if p_type == 'E':
    result = encoder(inp)
else:
    result = decoder(inp)

print(result, end="")
if p_type == 'E':
    print(f"\nsikistirma orani: {round((1 - (len(result) / len(inp))) * 100, 2)}%")
```
- İşlem türüne göre fonksiyonu çağır
- Sonucu yazdır, `end=""` ile sonuna yeni satır eklemez
- Kodlama işlemi yapıldıysa sıkıştırma oranını yeni satırda yazdır

---

## Sıkıştırma Oranı Hesaplama
Encoding işlemi yapıldığında, sıkıştırma oranı şu formülle hesaplanır:

**Sıkıştırma Oranı** = `(1 - (sıkıştırılmış_uzunluk / orijinal_uzunluk)) × 100`

Sonuç yüzde olarak ve iki ondalık basamakla gösterilir.

---

## Kullanım Örnekleri

### Örnek 1: Encoding (Kodlama)
```
Lutfen metni giriniz: AAABB
Yapilacak islem, Encoding/Decoding (E/D): E
3A2B
sikistirma orani: 40.0%
```

### Örnek 2: Decoding (Kod Çözme)
```
Lutfen metni giriniz: 3A2B
Yapilacak islem, Encoding/Decoding (E/D): D
AAABB
```

### Örnek 3: Karmaşık Metin
```
Lutfen metni giriniz: AAAAABBBCCCCCCDDDEEE
Yapilacak islem, Encoding/Decoding (E/D): E
5A3B6C3D3E
sikistirma orani: 52.38%
```

---

## Proje Özellikleri
✅ Run-Length Encoding (RLE) algoritması  
✅ Encoding ve Decoding işlemleri  
✅ Sıkıştırma oranı hesaplama  
✅ Kullanıcı girdi doğrulama  
✅ Çok basamaklı sayıları destekleme  
✅ Hata yönetimi (try-except)

---

**Proje Tamamlanma Tarihi:** Ocak 2026
