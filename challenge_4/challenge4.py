# Temel 4 işlem yapan program (+,-,*,/)
print("Lütfen iki sayı giriniz: ")

sayi1 = int(input())
sayi2 = int(input())

print("Hangi işlemi yapmak istiyorsunuz? (+, -, *, /): ")
islem = input()
if islem == '+':
    print(str(sayi1)+ " + " +str(sayi2)+ " = " +str(sayi1 + sayi2))
elif islem == '-':
    print(str(sayi1)+ " - " +str(sayi2)+ " = " +str(sayi1 - sayi2))
elif islem == '*':
    print(str(sayi1)+ " * " +str(sayi2)+ " = " +str(sayi1 * sayi2))
elif islem == '/':
    print(str(sayi1)+ " / " +str(sayi2)+ " = " +str(sayi1 / sayi2))
else:
    print("Hata!")