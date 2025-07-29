#!/usr/bin/env python3

"""Basit bir hesap makinesi.

Bu program toplama, çıkarma, çarpma ve bölme işlemeleri yapabilir.
Kullanıcıdan iki sayı ve yapmak istediği işlemi seçmesi istenir.
"""


def add(a, b):
    """a ile b'nin toplamını döndürür."""
    return a + b


def subtract(a, b):
    """a eksi b'nin sonucunu döndürür."""
    return a - b


def multiply(a, b):
    """a ile b'nin çarpımını döndürür."""
    return a * b


def divide(a, b):
    """a'yı b'ye bölerek sonucu döndürür.

    Sıfıra bölme durumunda `ZeroDivisionError` hatası fırlatır.
    """
    return a / b


if __name__ == "__main__":
    print("Hesap makinesine hoş geldiniz!")
    try:
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        raise SystemExit(1)

    print("\nYapmak istediğiniz işlem:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    choice = input("Seçiminiz (1/2/3/4): ")

    try:
        if choice == "1":
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"
        elif choice == "4":
            result = divide(num1, num2)
            op = "/"
        else:
            print("Geçersiz seçim yapıldı.")
            raise SystemExit(1)

    except ZeroDivisionError:
        print("Sıfıra bölme hatası!")
        raise SystemExit(1)

    print(f"\nSonuç: {num1} {op} {num2} = {result}")
