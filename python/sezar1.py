# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:21:46 2022

@author: PC
"""


def Encrypt(text, key):
    SifreliMesaj = ""
    for i in text:
        SifreliMesaj = SifreliMesaj + chr(ord(i) + key)
    print("[+] Ofset>>",str(key) + " Şifreli Mesaj>>",SifreliMesaj)
def Decrypt(text, key):
    CozulecekMesaj = ""
    for i in text:
        CozulecekMesaj = CozulecekMesaj + chr(ord(i) - key)
    print("[+] Ofset>>",str(key) + " Çözülecek Mesaj>>",CozulecekMesaj)
def Brute(text):
    CozulecekMesaj = ""
    key = 1
    while key < 26:
        for i in text:
            CozulecekMesaj = CozulecekMesaj + chr(ord(i) - key)
        print("[+] Ofset>>",str(key) + " Çözülecek Mesaj>>",CozulecekMesaj)
        key += 1
        CozulecekMesaj = ""
print("""
[01] ŞifreliMesaj1
[02] ÇözülecekMesaj
[03] BruteforceİleÇözülecekMesaj
[99] Çıkış
""")
Secenek = int(input("Seçeneğiniz>> "))
if Secenek == 99:
    print("[-] Çıkış")
    exit
elif Secenek == 1:
    text = input("[+] Mesaj>> ")
    key = int(input("[+] Ofset>> "))
    Encrypt(text, key)
elif Secenek == 2:
    text = input("[+] Mesaj>> ")
    key = int(input("[+] Ofset>> "))
    Decrypt(text, key)
elif Secenek == 3:
    text = input("[+] Mesaj>> ")
    Brute(text)
else:
    print("[?] Seçenek Seçiniz !")
    exit