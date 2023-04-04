yemek_tarifleri = {}
yemek_planlari = {}

def ana_menu():
    while True:
        print("\n***GÜNLÜK YEMEK PLANLAMA UYGULAMASI***\n")
        print("1. Yemek tarifi ekle")
        print("2. Yemek tarifi kategorize et")
        print("3. Günlük yemek planı oluştur")
        print("4. Günlük yemek planlarını görüntüle")
        print("5. Çıkış\n")

        secim = input("Lütfen bir seçim yapınız (1-5): ")

        if secim == "1":
            yemek_tarifi_ekle()
        elif secim == "2":
            yemek_tarifi_kategorize_et()
        elif secim == "3":
            gunluk_yemek_plani_olustur()
        elif secim == "4":
            gunluk_yemek_planlarini_goruntule()
        elif secim == "5":
            print("Program sonlandırıldı.")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

def yemek_tarifi_ekle():
    yemek_adi = input("Yeni yemek adı: ")
    yemek_tarifi = input("Yemek tarifi: ")
    yemek_tarifleri[yemek_adi] = yemek_tarifi
    print(f"{yemek_adi} tarifi başarıyla eklendi!")

def yemek_tarifi_kategorize_et():
    yemek_adi = input("Kategorize edilecek yemek adı: ")
    kategori = input("Kategori adı: ")
    yemek_tarifleri[yemek_adi]["kategori"] = kategori
    print(f"{yemek_adi} tarifi başarıyla kategorize edildi!")

def gunluk_yemek_plani_olustur():
    tarih = input("Yemek planı tarihi (yyyy-mm-dd): ")
    gunluk_yemek_plani = []
    while True:
        yemek_adi = input("Eklemek istediğiniz yemek adı (Çıkmak için 'q'): ")
        if yemek_adi == "q":
            break
        if yemek_adi not in yemek_tarifleri:
            print("Yemek tarifi bulunamadı.")
            continue
        gunluk_yemek_plani
