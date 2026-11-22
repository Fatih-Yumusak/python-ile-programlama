'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 22/11/2026
Açıklama: Bonus. Onluk sayıyı Roma rakamına, Roma rakamını onluğa çevirir.
'''


def roma_yaz(n):
    '''1-3999 arası sayıyı basamak basamak Roma rakamına çevirir.'''
    sonuc = ""
    # her basamak için bir, beş ve on sembolleri
    for bir, bes, on, basamak in (("M", "", "", 1000), ("C", "D", "M", 100),
                                  ("X", "L", "C", 10), ("I", "V", "X", 1)):
        d = n // basamak % 10
        if d <= 3:
            sonuc += bir * d
        elif d == 4:
            sonuc += bir + bes
        elif d <= 8:
            sonuc += bes + bir * (d - 5)
        else:
            sonuc += bir + on
    return sonuc


def roma_deger(harf):
    '''Tek bir Roma harfinin değerini verir.'''
    if harf in "IXC":
        return 10 ** "IXC".find(harf)
    if harf in "VLD":
        return 5 * 10 ** "VLD".find(harf)
    return 1000


def roma_oku(metin):
    '''Roma rakamını onluğa çevirir, küçük harf büyüğün önündeyse çıkarılır.'''
    toplam = 0
    for i in range(len(metin)):
        d = roma_deger(metin[i])
        if i + 1 < len(metin) and d < roma_deger(metin[i + 1]):
            toplam -= d
        else:
            toplam += d
    return toplam


if __name__ == "__main__":
    for n in (2026, 1994, 42, 4, 9, 3999):
        print(n, roma_yaz(n), roma_oku(roma_yaz(n)))
    print(roma_oku("XLII"))
