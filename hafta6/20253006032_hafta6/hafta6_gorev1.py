# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 01/11/2026
# Açıklama: Üç kenar uzunluğundan üçgeni sınıflandırır; çevre, alan (Heron)
#            ve en büyük açıyı (math.acos/math.degrees) hesaplar.

import math

# --- Girdi ---
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# --- Doğrula ---
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Uyarı: Kenarlar pozitif olmalı ve üçgen eşitsizliğini sağlamalı.")
else:
    # --- İşle ---
    # Açı/alan formülünde 'a' en uzun kenarı temsil eder; girilen kenarlardan
    # en büyüğünü ve diğer ikisini buluyoruz.
    if a >= b and a >= c:
        en_uzun, kenar1, kenar2 = a, b, c
    elif b >= a and b >= c:
        en_uzun, kenar1, kenar2 = b, a, c
    else:
        en_uzun, kenar1, kenar2 = c, a, b

    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - en_uzun) * (u - kenar1) * (u - kenar2))

    cos_aci = (kenar1 ** 2 + kenar2 ** 2 - en_uzun ** 2) / (2 * kenar1 * kenar2)
    aci = math.degrees(math.acos(cos_aci))

    # Kenarlara göre tür
    if math.isclose(a, b) and math.isclose(b, c):
        kenar_turu = "Eşkenar"
    elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"

    # En büyük açıya göre tür (== yerine math.isclose)
    if math.isclose(aci, 90):
        aci_turu = "Dik açılı"
    elif aci > 90:
        aci_turu = "Geniş açılı"
    else:
        aci_turu = "Dar açılı"

    # --- Çıktı ---
    print(f"Tür: {kenar_turu}, {aci_turu}")
    print(f"Çevre: {cevre:.2f}  Alan: {alan:.2f}  En büyük açı: {aci:.2f}°")
