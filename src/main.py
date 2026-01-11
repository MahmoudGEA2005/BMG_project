# Kodlama yapan fonksyinu, ornek: AAABB -> 3A2B
def encoder(text):
    # su andkai sayildigimiz harfi
    current = ''
    # her harf kac kere yazildigi sayan degiskeni
    counter = 0
    # sonuc tutan degiskeni
    result = ""
    # kullancinin girdigi metni tek tek dolas
    for i in text:
        # current harfi i ile ayni ise, demek hala sayaci artiyoruz
        if i == current:
            counter += 1
        else:
            # farkli ise, iki durumu olabilir
            # ya counter > 0, demek ki daha once saydigimiz harf var, onu sonucu ekle
            if (counter > 0):
                """ 
                    countr > 0  ise, demek ki daha once saydigimiz harf var, ve bu itersayonda farkliu bir harf ile karsilastik, dolaysiyla sonuca ekleme yapmaliyiz
                """
                result += f"{counter}{current}"
            # yoksaa birnci harf demektir ve hala her hangi bir sayma islemi yapmadik

            # (i == current) degil ise, demek yeni bir harf ile karsilastik
            # counter 1 olur, simdiki harfi sayilmak icin
            counter = 1
            # current i olur, yani bit harf ile sayma islemi basladik
            current = i
        """
            bu satir debugging icin kullanildi
            print(f"i is {i}, current is {current}, counter is {counter}")
        """
    """
        son harftan sonra baska bir iterasyonu olmayacagi icin, son harfi ve sayisini eklememiz lazim, cunku her zaman ekleme islemi sonraki iterasyonda olur
        kullandigim deekleme yontem f-string ile yapildi
    """
    result += f"{counter}{current}"
    return result


# Kod cozme fonksiyonu, ornek: 3A2B -> AAABB
def decoder(text):
    # sonuc tutan degiskeni
    result = ""
    """
        sayac degiskeni, ve string olarak baslatildi cunku birden fazla basamakli sayilar olabilir, ve o  durumda sayiyi string olarak tutup sonra inte cevircegiz
    """
    count = ""
    # kullanicinin girdigi metni tek tek dolas
    for i in text:
        """
            isDigit fonksyonu bir karakter sayi olup olmadigini belirtiren bir methodtur
            Ayrica kednimiz fonksiyonumuz da olusturabilirz try, except ve int() kullnarak
        """
        if i.isdigit():
            # i'ninci karakteri sayi ise, count degiskenine ekle (string concatenation)
            count += i
        else:
            """
                yoksa, count degiskenini inte cevir ve i karakteri ile carp,
                ama burada try, except kullaildi, cunku brinici itersayonda eger i'ninci karakter sayi degil ise, count hala bos string olacak ve int("") hata verecek
            """
            try:
                count = int(count)
            except ValueError:
                """
                hata verdi ise, demek ki bu birinci karakter ve count hala bos ve sadece bir kes yazmak istemis, once 1 yazmaya untulmus ve o andda count 1 tamamlaniyoruz
                ornek, girdigi metin: A3B, sonuc ABBB olmali
                """
                count = 1
            # sonucu guncelle
            result += i * count
            count = ""
    return result

"""
    Bu donguda sonsuz bir dongusu, kullancidan bir metin okuyup kontrol eder, eger gecerli bir metin girdi ise, len(inp) == 0, donguyu kirar, yoksa gecersiz uyarisi verir, ve yine metin ister
"""
while True:
    inp = input("Lutfen metni giriniz: ")
    if len(inp) == 0:
        print("gecersiz!!")
        continue
    break
"""
    Bu donguda sonsuz bir dongusu, kullancidan islem turu okuyup [E/D], ve .upper methodu ile her zaman buyuk harfini cevirir kontrol etmek icin, girdigi e, E, d, D ise, donguyu kirar, yoksa gecersiz uyarisi verir, ve yine metin ister
"""
while True:
    p_type = input("Yapilacak islem, Encoding/Decoding (E/D): ").upper()
    if p_type not in ['E', 'D']:
        print("Islem E/D olmalidir!!")
        continue
    else:
        break
# islem turune gore fonksiyonu cagir
if p_type == 'E':
    result = encoder(inp)
else:
    result = decoder(inp)
# sonucu yazdir, end="" ile sonuna yeni satir eklemez
print(result, end="")
if p_type == 'E':
    # kodalam islemi yapildiysa sikistirma oranini yeni satirda yazdir
    print(f"\nsikistirma orani: {round((1 - (len(result) / len(inp))) * 100, 2)}%")