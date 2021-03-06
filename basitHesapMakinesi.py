def Islem(operator, a, b): #Parametre alan ve değer döndüren bir fonksiyon ile, işlem türü ve hesaplamaları fonksiyon içinde çözdüm.
    if operator == "1":
        return a + b
    elif operator == "2":
        return a - b
    elif operator == "3":
        return a * b
    elif operator == "4":
        return a / b
    else:
        return "" #İşlem türü seçiminde, "sonuc" değişkenine, fonksiyonun "None" değer döndürmesi gibi durumları engelledim. Bkz:(1)


i = 0
cikisMi = True
while cikisMi == True: #Burda ki döngü ile en altta ki "cevap" değişkeni ve karar yapısını bağlayarak çıkış tercihinin yapılabilmesini sağladım. Bkz:(2)
    while i <= 4:
        s1 = input("ilk sayı: ")
        s2 = input("ikinci sayı: ")
        if s1.isdigit() and s2.isdigit(): # Girilen sayıların rakam mı? olduğunu kontrol ettim.
            s1, s2 = int(s1), int(s2) #Girilen değerler sayıysa, bug oluşmaması için tip dönüşümü ile int yaptım.
            secim = input(""" 
-----------------------
İŞLEM TÜRÜ:
[1]         : Topla
[2]         : Çıkar
[3]         : Çarp
[4]         : Böl 
Seçiminiz?: """)
            sonuc = Islem(secim, s1, s2)
            print("-----------------------")
            print("İşlem Sonucu: ", sonuc) #(1)
            print("-----------------------")
            i = 5
        else:
            print("Hatalı Seçim!") #İşlem türü seçiminde ve sayı girişinde manipülasyonu önlemiş oldum.
    cevap = input("Çıkmak İster misiniz(e/h)?:\t")
    if cevap.lower() == "e": # Çıkış seçiminde "lower()" fonksiyonu ile case sensetive sorununu ortadan kaldırdım. aynı şekilde "h" içinde uygulandı.
        cikisMi = False #"e" seçilmesi takdirde en dışda ki döngüyü durdurur.
    elif cevap.lower() == "h":   # (2)
        cikisMi = True #"h" seçilmesi takdirde en dışda ki döngüyü devam ettirir.
        i = 0 # İçteki döngünün tekrar baştan dönebilmesi için "i" yi sıfırladım.
    else:
        print("Hatalı Seçim!") #Çıkış tercihinde "e" ve ya "h" dışında tercih yapılmasına karşın manipülasyonu önlemiş oldum.
