'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 22/11/2026
Açıklama: Vigenère şifresi. Her harf anahtarın sıradaki harfi kadar kaydırılır,
yon=-1 verilirse çözülür. Harf olmayan karakterler olduğu gibi kalır.
'''

KUCUK = "abcdefghijklmnopqrstuvwxyz"
BUYUK = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere(metin, anahtar, yon=1):
    '''Metni şifreler (yon=1) ya da çözer (yon=-1).'''
    anahtar = anahtar.lower()
    sonuc = ""
    j = 0    # anahtar sayacı, sadece harflerde ilerliyor
    for harf in metin:
        kayma = KUCUK.find(anahtar[j % len(anahtar)]) * yon
        if KUCUK.find(harf) != -1:
            sonuc += KUCUK[(KUCUK.find(harf) + kayma) % 26]
            j += 1
        elif BUYUK.find(harf) != -1:
            sonuc += BUYUK[(BUYUK.find(harf) + kayma) % 26]
            j += 1
        else:
            sonuc += harf
    return sonuc


if __name__ == "__main__":
    sifreli = vigenere("Attack at dawn", "LEMON")
    print(sifreli)
    print(vigenere(sifreli, "LEMON", -1))
    print(vigenere("Merhaba, Dunya!", "Anahtar"))
    print(vigenere(vigenere("Merhaba, Dunya!", "Anahtar"), "Anahtar", -1))
