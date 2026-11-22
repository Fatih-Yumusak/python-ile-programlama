# Hafta 8 – UML Sınıf Diyagramı (Fatih Yumuşak – 20253006032)

```mermaid
classDiagram
    class TrKelime {
        +str metin
        +__init__(metin)
        +__str__() str
        +__len__() int
        +__getitem__(indeks) str
        +__contains__(parca) bool
        +__eq__(diger) bool
        +__lt__(diger) bool
        +buyuk() str
    }
    class Kesir {
        +int pay
        +int payda
        +__init__(pay, payda)
        +__str__() str
        +__add__(diger) Kesir
        +__sub__(diger) Kesir
        +__mul__(diger) Kesir
        +__truediv__(diger) Kesir
        +__eq__(diger) bool
        +__lt__(diger) bool
        +__le__(diger) bool
        +__float__() float
    }
```

`TrKelime` sabit `ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"` değerini kullanır;
`Kesir` sadeleştirme için `ebob(a, b)` fonksiyonunu kullanır.
