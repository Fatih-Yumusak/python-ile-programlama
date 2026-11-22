'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 22/11/2026
Açıklama: TrKelime sınıfı. Python harfleri Unicode koduna göre sıraladığı için
"çay" < "dağ" yanlış çıkıyor. Bu sınıf ALFABE sırasına göre karşılaştırır.
'''

ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"


class TrKelime:
    '''Türkçe kurallarına göre küçültülen ve sıralanan kelime.'''

    def __init__(self, metin):
        '''Metni küçültür, önce I -> ı ve İ -> i çevrilir.'''
        self.metin = metin.replace("I", "ı").replace("İ", "i").lower()

    def __str__(self):
        '''Küçültülmüş kelimeyi verir.'''
        return self.metin

    def __repr__(self):
        '''Kelimenin kod gösterimi.'''
        return "TrKelime('" + self.metin + "')"

    def __len__(self):
        '''Harf sayısı.'''
        return len(self.metin)

    def __getitem__(self, indeks):
        '''İndeks ya da dilimle harf döndürür.'''
        return self.metin[indeks]

    def __contains__(self, parca):
        '''Parça kelimenin içinde geçiyor mu.'''
        return TrKelime(parca).metin in self.metin

    def __eq__(self, diger):
        '''Küçültülmüş halleri aynıysa eşittir.'''
        return self.metin == diger.metin

    def __lt__(self, diger):
        '''Harfleri ALFABE.find ile karşılaştırır, ön ekse kısa olan küçüktür.'''
        kisa = min(len(self.metin), len(diger.metin))
        for i in range(kisa):
            a = ALFABE.find(self.metin[i])
            b = ALFABE.find(diger.metin[i])
            if a != b:
                return a < b
        return len(self.metin) < len(diger.metin)

    def buyuk(self):
        '''Türkçe büyük harfli halini verir (i -> İ, ı -> I).'''
        return self.metin.replace("i", "İ").replace("ı", "I").upper()


if __name__ == "__main__":
    for a, b in (("çay", "dağ"), ("ılık", "iğne"), ("ördek", "pasta")):
        print(a, "<", b, "Türkçe:", TrKelime(a) < TrKelime(b), "Python str:", a < b)
    print(TrKelime("Işık") == TrKelime("ışık"))
    k = TrKelime("İSTANBUL")
    print(k, len(k), "tan" in k, k.buyuk(), k[0], k[2:5])
    print(TrKelime("ev") < TrKelime("evim"), TrKelime("evim") < TrKelime("ev"))
