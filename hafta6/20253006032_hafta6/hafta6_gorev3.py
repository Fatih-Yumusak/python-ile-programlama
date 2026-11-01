# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 01/11/2026
# Açıklama: T.C. kimlik numarasının biçimini ve kontrol hanelerini doğrular.
#            Test amaçlı numaralar kullanılmıştır, gerçek kişiye ait değildir.

# --- Girdi ---
tc = input("T.C. kimlik no: ")

# --- Doğrula (biçim) ---
if len(tc) != 11 or not tc.isdigit() or tc[0] == "0":
    print("Uyarı: 11 haneli, yalnızca rakamlardan oluşan ve 0 ile başlamayan bir numara giriniz.")
else:
    # --- İşle ---
    tek_toplam = 0   # 1., 3., 5., 7., 9. haneler (T)
    cift_toplam = 0  # 2., 4., 6., 8. haneler (Ç)

    for i in range(9):
        rakam = int(tc[i])
        if (i + 1) % 2 == 1:
            tek_toplam += rakam
        else:
            cift_toplam += rakam

    h10 = (7 * tek_toplam - cift_toplam) % 10
    h11 = (tek_toplam + cift_toplam + h10) % 10

    gecerli = h10 == int(tc[9]) and h11 == int(tc[10])

    # --- Çıktı ---
    sonuc = "GEÇERLİ" if gecerli else "GEÇERSİZ"
    print(f"Tek: {tek_toplam}  Çift: {cift_toplam}  10. hane: {h10}  11. hane: {h11} → {sonuc}")
