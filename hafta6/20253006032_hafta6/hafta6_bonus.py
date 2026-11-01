# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 01/11/2026
# Açıklama: Luhn algoritmasıyla 15 haneli numaranın geçerli kontrol hanesini bulur.

numara_15 = "453914880343646"

for kontrol in range(10):
    tam_numara = numara_15 + str(kontrol)
    ters_numara = tam_numara[::-1]
    toplam = 0

    for i in range(len(ters_numara)):
        rakam = int(ters_numara[i])
        if i % 2 == 1:          # sağdan 2., 4., 6. ... haneler ikiye katlanır
            rakam *= 2
            if rakam > 9:
                rakam -= 9
        toplam += rakam

    if toplam % 10 == 0:
        print(f"Kontrol hanesi: {kontrol}")
        break
