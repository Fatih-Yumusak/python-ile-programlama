'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 22/11/2026
Açıklama: Taban dönüştürücü. onluktan() sayıyı 2-16 arası tabana çevirir,
onluga() Horner yöntemiyle geri çevirir.
'''

RAKAM = "0123456789ABCDEF"


def onluktan(n, taban):
    '''Onluk n sayısını verilen tabana çevirip metin döndürür.'''
    if n == 0:
        return "0"
    sonuc = ""
    while n > 0:
        sonuc = RAKAM[n % taban] + sonuc   # kalan başa eklenir
        n = n // taban
    return sonuc


def onluga(metin, taban):
    '''Verilen tabandaki metni Horner yöntemiyle onluk sayıya çevirir.'''
    metin = metin.upper()    # küçük harf de kabul
    sonuc = 0
    for harf in metin:
        sonuc = sonuc * taban + RAKAM.find(harf)
    return sonuc


if __name__ == "__main__":
    print("2026 -> ikilik", onluktan(2026, 2), "sekizlik", onluktan(2026, 8),
          "onaltılık", onluktan(2026, 16))
    print(onluga("7ea", 16), onluga("11111101010", 2), onluga("3752", 8))
    # sonucu hazır fonksiyonlarla kontrol
    print(onluktan(2026, 2) == bin(2026)[2:], onluktan(2026, 16) == hex(2026)[2:].upper())
    print(onluktan(0, 5), onluga(onluktan(12345, 13), 13))
