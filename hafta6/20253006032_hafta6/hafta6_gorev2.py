# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 01/11/2026
# Açıklama: Bir cümledeki harf, sesli, sessiz, rakam ve kelime sayısını bulur;
#            cümleyi tersten yazar ve palindrom olup olmadığını kontrol eder.

SESLI_HARFLER = "aeıioöuüAEIİOÖUÜ"

# --- Girdi ---
cumle = input("Cümle: ")

# --- İşle (tek for döngüsü) ---
harf = sesli = sessiz = rakam = kelime = 0
kelime_icinde = False
kucuk_harfler = ""

for karakter in cumle:
    if karakter.isalpha():
        harf += 1
        if karakter in SESLI_HARFLER:
            sesli += 1
        else:
            sessiz += 1
        kucuk_harfler += karakter.lower()
    elif karakter.isdigit():
        rakam += 1

    if karakter != " ":
        if not kelime_icinde:
            kelime += 1
            kelime_icinde = True
    else:
        kelime_icinde = False

ters = cumle[::-1]
palindrom = kucuk_harfler == kucuk_harfler[::-1]

# --- Çıktı ---
print(f"Harf: {harf}  Sesli: {sesli}  Sessiz: {sessiz}  Rakam: {rakam}  Kelime: {kelime}")
print("Ters:", ters)
print("Palindrom" if palindrom else "Palindrom değil")
