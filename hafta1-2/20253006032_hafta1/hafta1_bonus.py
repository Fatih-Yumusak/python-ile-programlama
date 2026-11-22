'''
Ad Soyad: Fatih Yumuşak
Öğrenci No: 20253006032
Tarih: 04/10/2026
Açıklama: Turtle ile olimpiyat halkalarını (beş daire) çizer.
Liste ve döngü kullanılmadı, her halka ayrı çizildi.
'''

import turtle

turtle.width(4)

# üst sıra: mavi, siyah, kırmızı
turtle.penup()
turtle.goto(-110, 0)
turtle.pendown()
turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(110, 0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

# alt sıra: sarı, yeşil
turtle.penup()
turtle.goto(-55, -50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(55, -50)
turtle.pendown()
turtle.color("green")
turtle.circle(50)

turtle.hideturtle()
turtle.done()
