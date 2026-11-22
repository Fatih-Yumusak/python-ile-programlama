'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 04/10/2026
Açıklama: Turtle ile kare + üçgenden oluşan ev çizer ve adı yazar.
Döngü bu haftanın konusu olmadığı için komutlar tek tek yazıldı.
'''

import turtle

# kare (gövde), sol alt köşeden başlıyor
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

# sol üst köşeye çık
turtle.left(90)
turtle.forward(100)
turtle.right(90)

# eşkenar üçgen (çatı), her dönüş 120 derece
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)

# evin yanına ad yaz
turtle.penup()
turtle.goto(130, 0)
turtle.write("Fatih Yumuşak", font=("Arial", 16, "normal"))
turtle.hideturtle()
turtle.done()
