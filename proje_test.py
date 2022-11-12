from libary import *

print("""
*******************************************************
      
    Kütüphane Programına Hoşgeldiniz.
        
    1. Kitapları Göster
    
    2. Kitap Sorgulama
    
    3.Kitap Ekle
    
    4.Kitap Sil
    
    5.Baskı Yükselt
    
    Çıkmak için 'q' ya basın.
        
        
*******************************************************""")

libary = Libary()

while False:  # TODO: open loop when gui ready
    islem = input("Yapıcağınız İşlem: ")
    if islem == "q":
        print("Program sonlandırılıyor....")
        print("Yine Bekleriz...")
        break

    elif islem == "1":
        print("Kitaplar Gösteriliyor...")
        time.sleep(2)
        print("Kitaplarlar.")
        libary.show_books()

    elif islem == "2":
        name = input("Kitap ismi giriniz.")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        libary.question_book(name)
        print("Kitap sorgulandı.")

    elif islem == "3":
        name = input("Kitap ismi giriniz.")
        writer = input("Kitap yazarı giriniz.")
        publisher = input("Kitap yayın evi giriniz.")
        category = input("Kitap tür giriniz.")
        oppression = int(input("Kitap baskı sayısı giriniz."))
        book = Book(name, writer, publisher, category, oppression)

        print("Kitap ekleniyor...")
        time.sleep(2)

        libary.create_book(book)
        print("Kitap eklendi.")

    elif islem == "4":
        name = input("Hangi kitabı silmek istiyorsunuz ?")

        answer = input("Emin Misiniz : (E/h)")
        if answer == "E":
            print("Kitap siliniyor...")
            time.sleep(2)
            libary.delete_book(name)
            print("Kitap silindi.")
        else:
            print("Kitap silme işlemi iptal edildi.")

    elif islem == "5":
        name = input("Kitap ismi giriniz.")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        libary.oppression_increase(name)
        print("Baskı yükseltildi.")
    else:
        print("Geçersiz İşlem")
