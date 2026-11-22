'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 22/11/2026
Açıklama: Kesir sınıfı v2. Özel metotlarla toplama, çıkarma, çarpma, bölme
ve karşılaştırma yapılır. İşlemler yeni ve sade bir Kesir döndürür.
'''


def ebob(a, b):
    '''Öklid algoritmasıyla en büyük ortak böleni bulur.'''
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


class Kesir:
    '''Pay ve paydadan oluşan, her zaman sade tutulan kesir.'''

    def __init__(self, pay, payda=1):
        '''Kesri sadeleştirir, paydayı pozitif yapar, payda 0 ise hata verir.'''
        if payda == 0:
            raise ZeroDivisionError("Payda sıfır olamaz")
        if payda < 0:
            pay, payda = -pay, -payda
        b = ebob(pay, payda)
        if b == 0:
            b = 1
        self.pay = pay // b
        self.payda = payda // b

    def __str__(self):
        '''Kesri metin olarak verir, payda 1 ise sadece pay yazılır.'''
        if self.payda == 1:
            return str(self.pay)
        return str(self.pay) + "/" + str(self.payda)

    def __repr__(self):
        '''Kesrin kod gösterimi.'''
        return "Kesir(" + str(self.pay) + ", " + str(self.payda) + ")"

    def __add__(self, diger):
        '''Toplama, yeni Kesir döndürür.'''
        return Kesir(self.pay * diger.payda + diger.pay * self.payda,
                     self.payda * diger.payda)

    def __sub__(self, diger):
        '''Çıkarma, yeni Kesir döndürür.'''
        return Kesir(self.pay * diger.payda - diger.pay * self.payda,
                     self.payda * diger.payda)

    def __mul__(self, diger):
        '''Çarpma, yeni Kesir döndürür.'''
        return Kesir(self.pay * diger.pay, self.payda * diger.payda)

    def __truediv__(self, diger):
        '''Bölme, yeni Kesir döndürür.'''
        return Kesir(self.pay * diger.payda, self.payda * diger.pay)

    def __eq__(self, diger):
        '''Eşitlik, çapraz çarpımla bakılır.'''
        return self.pay * diger.payda == diger.pay * self.payda

    def __lt__(self, diger):
        '''Küçüktür, çapraz çarpımla bakılır.'''
        return self.pay * diger.payda < diger.pay * self.payda

    def __le__(self, diger):
        '''Küçük eşittir, çapraz çarpımla bakılır.'''
        return self.pay * diger.payda <= diger.pay * self.payda

    def __float__(self):
        '''Ondalık karşılığını verir.'''
        return self.pay / self.payda


if __name__ == "__main__":
    # (a) 2'den 10'a kadar (1 - 1/n) çarpımı
    carpim = Kesir(1)
    for n in range(2, 11):
        carpim = carpim * (Kesir(1) - Kesir(1, n))
    print("Çarpım:", carpim)

    # (b) en büyük kesir, sadece < kullanarak
    en_buyuk = Kesir(3, 7)
    for aday in (Kesir(5, 12), Kesir(2, 5), Kesir(4, 9), Kesir(3, 8)):
        if en_buyuk < aday:
            en_buyuk = aday
    print("En büyük:", en_buyuk)

    print(Kesir(6, 8) == Kesir(3, 4))
    print(Kesir(3, 4) / Kesir(3, 8))
    print(Kesir(1, 2) + Kesir(1, 3), Kesir(1, 2) - Kesir(1, 3), float(Kesir(1, 4)))
    print(Kesir(1, 3) <= Kesir(2, 6), Kesir(-1, -2))
