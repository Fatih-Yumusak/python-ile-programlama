# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 01/11/2026
# Açıklama: Adam asmaca oyunu. Denenen harfler bir karakter dizisinde birikir;
#            6 hata dolmadan kelime tamamlanırsa break, dolarsa while...else
#            ile kelime açıklanır.

gizli_kelime = "KOŞUL"
tahminler = ""
hata = 0

while hata < 6:
    # --- Çıktı: mevcut durum ---
    goster = ""
    tamamlandi = True
    for harf_k in gizli_kelime:
        if harf_k in tahminler:
            goster += harf_k + " "
        else:
            goster += "_ "
            tamamlandi = False
    if tamamlandi:
        print(f"{goster.strip()}  (hata: {hata}/6)   Kazandınız!")
        break
    print(f"{goster.strip()}  (hata: {hata}/6)")

    # --- Girdi ---
    harf_girisi = input("Harf: ")

    # --- Doğrula ---
    if len(harf_girisi) != 1 or not harf_girisi.isalpha():
        continue

    # "i".upper() Türkçe "İ" değil "I" verdiği için özel durumları elden çeviriyoruz
    if harf_girisi == "i":
        harf = "İ"
    elif harf_girisi == "ı":
        harf = "I"
    else:
        harf = harf_girisi.upper()

    if harf in tahminler:
        print("Bu harfi zaten denediniz.")
        continue

    # --- İşle ---
    tahminler += harf
    if harf not in gizli_kelime:
        hata += 1
else:
    print(f"Kaybettiniz! Kelime: {gizli_kelime}")
