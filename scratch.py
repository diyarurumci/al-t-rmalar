# 1.soru
a = 0
for i in range(19, 203, 3):
    a += i

print(a)
----------------------
# 2.soru
a = 0
for i in range(1, 10000):
    a += 1 / (i ** 2)

print((6 * a) ** 0.5)

# 4.soru
1.
yol(liste
yardımı
ile
çözmek)
a = []
for i in range(100, 1000):
    if int(str(i)[0]) == int(str(i)[2]):
        a.append(i)
print(a)
2.
yol(liste
yardımı
ile
ama
tersten
ilerleme
metodu
ile)
a = []
for i in range(100, 1000):
    if int(str(i)[::-1]):
        a.append(i)
print(a)
3.
yol(daha
fazla
değişken
kullanarak
listesiz
çözüm(aslında
mantığı
2.
yol
ile
aynı))
for i in range(100, 1000):
    s = str(i)
    f = s[::-1]
    if f == s:
        print(s)

# 5.soru
for i in range(1000, 10000):
    s = str(i)
    f = s[::-1]
    if f == s:
        print(s)

# 6.soru
liste = []
for i in range(1000, 10000):
    f = int(str(i)[0])
    a = int(str(i)[3])
    if f > a:
        liste.append(i)
print(len(liste))

# 7soru
liste = []
for i in range(100, 1000):
    f = int(str(i)[0])
    t = int(str(i)[1])
    a = int(str(i)[2])
    if f + t == a:
        liste.append(i)
print(len(liste))
print(liste)
# 8
liste = []
for i in range(100, 1000, 2):
    a = int(str(i)[0])
    b = int(str(i)[1])
    c = int(str(i)[2])
    if a == b or a == c or b == c:
        liste.append(i)
print(len(liste))
# 9
for i in range(1, 1000):
    b = 0
    for c in range(len(str(i))):
        b += int(str(i)[c])
        if b < 9:
            print(i, end=" ")
# 10
liste = []
for i in range(10000, 100000):
    a = int(str(i)[0:2])
    b = int(str(i)[3:5])
    if a == b:
        liste.append(i)
print(len(liste))

# 11
liste = []
for x in range(1, 350):
    if 125 % x == 200 % x == 350 % x:
        liste.append(x)
print(max(liste))

# 12
i = 0
for i in range(1800, 2100):
    if int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) == (2005 - i):
        print(i)
# 13
for i in range(10, 100):
    for a in range(10, 100):
        if int(str(i) + str(a)) == 11 * (a + i):
            print(i, a)
    # 14soru (semihin icadı)
a = []
b = []
for i in range(1, 1000):
    for j in range(1, 1000):
        if i < j and i * j == 121212:
            a += [i]
            b += [j]

print(max(a), min(b))
# 15.soru
for i in range(10000, 100000):
    a = 0
    for b in range(2, int(i ** 0.5) + 1):
        if i % b == 0:
            a += 1
    if a == 0:
        print(i)
# 16.soru
a = 0
sayi = int(input("sayıyı giriniz:"))
for i in range(2, sayi):
    if (sayi % i == 0):
        a += 1
if a == 0:
    print("sayı asaldır")
else:
    print("değildir")


    # 17soru
    def palinmi(x):
        if x == int(str(x)[::-1]):
            print("girdiğiniz sayı palindiromiktir")

sayi = int(input("sayı giriniz"))
if sayi in range(100, 10000):
    palinmi(sayi)
else:
    print("lütfen 3 veya 4 basamaklı bir sayı giriniz)

