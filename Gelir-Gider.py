def ana_menu():
    while True:
        print("\n***KİŞİSEL FİNANS TAKİP UYGULAMASI***\n")
        print("1. Giderleri kaydet")
        print("2. Gelirleri kaydet")
        print("3. Toplam giderleri ve gelirleri görüntüle")
        print("4. Belirli bir zaman dilimindeki giderleri veya gelirleri görüntüle")
        print("5. Çıkış\n")

        secim = input("Lütfen bir seçim yapınız (1-5): ")

        if secim == "1":
            gider_kaydet()
        elif secim == "2":
            gelir_kaydet()
        elif secim == "3":
            toplam_gider_geliri_goruntule()
        elif secim == "4":
            zaman_dilimindeki_gider_gelir_goruntule()
        elif secim == "5":
            print("Program sonlandırıldı.")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

def gider_kaydet():
    gider_miktari = float(input("Gider miktarı: "))
    gider_tarihi = input("Gider tarihi (yyyy-mm-dd): ")
    gider_aciklamasi = input("Gider açıklaması: ")
    with open("giderler.txt", "a") as file:
        file.write(f"{gider_tarihi},{gider_miktari},{gider_aciklamasi}\n")
    print("Gider kaydedildi.")

def gelir_kaydet():
    gelir_miktari = float(input("Gelir miktarı: "))
    gelir_tarihi = input("Gelir tarihi (yyyy-mm-dd): ")
    gelir_aciklamasi = input("Gelir açıklaması: ")
    with open("gelirler.txt", "a") as file:
        file.write(f"{gelir_tarihi},{gelir_miktari},{gelir_aciklamasi}\n")
    print("Gelir kaydedildi.")

def toplam_gider_geliri_goruntule():
    toplam_gider = 0
    toplam_gelir = 0
    with open("giderler.txt", "r") as file:
        for line in file:
            tarih, miktar, aciklama = line.strip().split(",")
            toplam_gider += float(miktar)
    with open("gelirler.txt", "r") as file:
