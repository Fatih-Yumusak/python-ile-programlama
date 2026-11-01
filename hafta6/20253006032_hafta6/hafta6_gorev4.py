# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 01/11/2026
# Açıklama: Collatz dizisinin adım sayısını ve en yüksek değerini bulur;
#            iç içe döngüyle belirli bir aralıktaki en uzun zinciri arar.

# --- Girdi (a) ---
n = int(input("n: "))

# --- Doğrula ---
if n <= 0:
    print("Uyarı: n pozitif bir tam sayı olmalı.")
else:
    # --- İşle (a) ---
    baslangic = n
    deger = n
    adim = 0
    en_yuksek = n

    while deger != 1:
        deger = deger // 2 if deger % 2 == 0 else 3 * deger + 1
        adim += 1
        if deger > en_yuksek:
            en_yuksek = deger

    # --- Çıktı (a) ---
    print(f"{baslangic} → 1: {adim} adım, en yüksek değer {en_yuksek}")

    # --- Girdi (b) ---
    ust_sinir = int(input("Üst sınır: "))

    if ust_sinir < 1:
        print("Uyarı: Üst sınır pozitif bir tam sayı olmalı.")
    else:
        # --- İşle (b) ---
        en_uzun_baslangic = 1
        en_uzun_adim = 0

        for aday in range(1, ust_sinir + 1):
            deger = aday
            adim_sayisi = 0
            while deger != 1:
                deger = deger // 2 if deger % 2 == 0 else 3 * deger + 1
                adim_sayisi += 1
            if adim_sayisi > en_uzun_adim:
                en_uzun_adim = adim_sayisi
                en_uzun_baslangic = aday

        # --- Çıktı (b) ---
        print(f"1–{ust_sinir} arasında en uzun zincir: {en_uzun_baslangic} ({en_uzun_adim} adım)")
