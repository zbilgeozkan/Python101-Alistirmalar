dogru_sifre = "qwert123"
girilen_sifre = input("Lütfen şifrenizi giriniz: ")

if girilen_sifre == "qwert123":
    print("Hoş geldiniz!")
else:
    girilen_sifre = input("Şifreniz yanlıştır, lütfen şifrenizi tekrar giriniz: ")
    
    if girilen_sifre == "qwert123":
        print("Hoş geldiniz!")
    else:
        print("Yanlış şifre girdiniz.")