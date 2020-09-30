# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:04:30 2020

@author: Rizki-PC

Nama : Rizki Ashuri Pratama
NIM  : 190411100151
Kelas : 3C Pemrograman Desktop
Materi : Review Materi Python

"""
print("Review Materi Python")
print("Nomor 1 : Program menghitung rata-rata")
angka1,angka2,angka3,angka4,angka5=10,20,30,40,50
rata=(angka1+angka2+angka3+angka4+angka5)/5
print("Angka 1:", angka1)
print("Angka 2:", angka2)
print("Angka 3:", angka3)
print("Angka 4:", angka4)
print("Angka 5:", angka5)
print("Rata - Rata 5 angka :", rata)

print("Nomor 2 : Program luas dan keliling bangun datar Persegi Panjang")
panjang = int(input("Masukan Panjang : "))
lebar = int(input("Masukan Lebar : "))
luas = panjang*lebar
keliling=2*(panjang+lebar)
print("Luas Persegi panjang dengan panjang ", panjang," dan lebar ",lebar," adalah ",luas)
print("keliling Persegi panjang dengan panjang ", panjang," dan lebar ",lebar," adalah ",keliling)

print("Nomor 3 : Program hitung index masa tubuh")
berat = int(input("Masukan berat badan(Kg) :"))
tinggi = int(input("Masukkan tinggi badan(Cm) :"))
bmi = berat/((tinggi/100)**2)
print("BMI anda adalah ",bmi)
if bmi < 18.5:
    print("Berat badan kurang")
elif bmi >= 18.5 and bmi <= 22.9 :
    print("Berat badan normal")
elif bmi >= 23 and bmi<=29.9:
    print("Berat badan berlebih(kecenderungan obesitas)")
else:
    print("Obesitas")

print("Nomor 4 : Program menentukan nilai maximum dan minimum dari sejumlah nilai masukan N")
temp = []
ulang = int(input("Berapa data yang akan dimasukkan(angka) :"))
for i in range(ulang):
    data = int(input("Masukkan Angkanya : "))
    temp.append(data)
print("Nilai Maksimum : ",max(temp))
print("Nilai minimum : ",min(temp))

print("Nomor 5 : Program validasi username dan password")
username = "Rizki"
password = 13052001
for i in range(4, 0, -1):
    inputUsername = input("Silahkan Masukkan Username Anda : ")
    inputPassword = int(input("Silahkan Masukkan Password Anda : "))
    if inputUsername == username and inputPassword == password:
        print("Anda Berhasil Masuk")
        break
    else:
        print("Maaf Username dan Password Salah")
        print("Anda bisa mencoba lagi dalam ",i-1," kali lagi")

print("Nomor 6 : Program menghitung nilai IPS mahasiswa")
dataNama = []
dataNilai =[]
ips=0.00
jumlah = int(input("Masukkan Jumlah Mata Kuliah :"))
for i in range(jumlah):
    nama = input("Masukan Nama Mata Kuliah : ")
    nilai = input("Masukan Nilai Mata Kuliah(Dengan Abjad Kapital):")
    if nilai == "A":
        nilai = 4.00
    elif nilai == "B+":
        nilai = 3.50
    elif nilai == "B":
        nilai = 3.00
    elif nilai == "C+":
        nilai = 2.50
    elif nilai == "C":
        nilai = 2.00
    elif nilai == "D+":
        nilai = 1.50
    elif nilai == "D":
        nilai = 1.00
    else:
        nilai = 0.00
    dataNama.append(nama)
    dataNilai.append(nilai)
print("Data Mata Kuliah yang telah dimasukkan :")
print("Nomor", end="     ")
print("Nama Mata Kuliah", end="      ")
print("Nilai")
for i in range(len(dataNama)):
    print(i+1, end="              ")
    print(dataNama[i], end="               ")
    print(dataNilai[i],)
    ips+=dataNilai[i]
print("IPS = ", ips/len(dataNama))