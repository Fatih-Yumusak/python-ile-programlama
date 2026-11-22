'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 22/11/2026
Açıklama: E-posta doğrulayıcı. Kurallar sırayla denetlenir, ilk hatalı
kuralın mesajı döndürülür. Hepsi geçerse "Geçerli" döner.
'''

IZINLI_OZEL = "._-"


def eposta_denetle(adres):
    '''Adresi kurallara göre denetler ve sonucu mesaj olarak döndürür.'''
    # tam olarak bir @ olmalı
    if adres.count("@") != 1:
        return "Tam olarak bir @ olmalı"

    # find ile @ yerini bulup dilimle iki parçaya ayırıyoruz
    konum = adres.find("@")
    kullanici = adres[:konum]
    alan = adres[konum + 1:]

    # kullanıcı adı boş olmamalı, sadece harf, rakam, . _ - olabilir
    if kullanici == "":
        return "Kullanıcı adı boş olamaz"
    for harf in kullanici:
        if not harf.isalnum() and IZINLI_OZEL.find(harf) == -1:
            return "Geçersiz karakter: '" + harf + "'"

    # kullanıcı adı nokta ile başlayıp bitmemeli
    if kullanici.startswith(".") or kullanici.endswith("."):
        return "Nokta ile başlayamaz/bitemez"

    # alan adında nokta olmalı, başta ve sonda olmamalı
    if alan.find(".") == -1 or alan.startswith(".") or alan.endswith("."):
        return "Alan adı hatalı"

    # ardışık iki nokta olmamalı
    if adres.find("..") != -1:
        return "Ardışık nokta olamaz"

    return "Geçerli"


if __name__ == "__main__":
    for adres in ("ece.yilmaz@nisantasi.edu.tr", "ece@@mail.com",
                  "ece yilmaz@mail.com", ".ece@mail.com", "ece@mail",
                  "ece..y@mail.com", "@mail.com"):
        print(adres.ljust(28), eposta_denetle(adres))
