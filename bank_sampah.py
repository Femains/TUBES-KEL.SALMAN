import sys

kecamatan = ["Ajibarang", "Banyumas", "Baturaden", "Cilongok", "Purwokerto Barat", "Purwokerto Selatan", "Purwokerto Timur", "Sokaraja"]

plastik = [160, 225, 135, 190, 255, 320, 245, 180]
logam =[237, 183, 329, 158, 274, 195, 321, 276]
kaca = [146, 83, 101, 58, 219, 155, 213, 180]
elektronik = [14, 56, 120, 90, 75, 65, 78, 25]
karet = [114, 210, 78, 98, 153, 79, 82, 126]

sisa_makanan = [78, 58, 12, 36, 69, 45, 87, 20]
kotoran_hewan = [38, 92, 14, 69, 80, 24, 56, 73]
dedaunan = [53, 21, 84, 10, 76, 33, 95, 47]
gabung = []

def home():
    print("BANK SAMPAH YANG ADA DI KABUPATEN BANYUMAS")
    print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    print("1. List Bank Sampah")
    print("2. Sortir Sampah")
    menu_pilih = int(input("Masukan menu yang diinginkan : "))
    if menu_pilih == 1:
        list_kecamatan()
    elif menu_pilih == 2:
        tampilkanSortir()

def list_kecamatan():
    for i in range(len(kecamatan)):
        print(f"{i+1} {kecamatan[i]}")
    kembali()

def kembali():
    print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    Pemilihan = int(input("PILIH KECAMATAN YANG ADA DI KABUPATEN BANYUMAS => "))
    print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    if Pemilihan == 1:
        print("--KECAMATAN AJIBARANG--")
        print(f"ORGANIK =  {sisa_makanan[0]+kotoran_hewan[0]+dedaunan[0]}Kg" )
        print(f"NON-ORGANIK = {plastik[0]+logam[0]+kaca[0]+elektronik[0]+karet[0]}Kg " )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
        tampilkanMenu()
    elif Pemilihan == 2:
        print("KECAMATAN BANYUMAS : ")
        print(f"ORGANIK = {plastik[1]+logam[1]+kaca[1]+elektronik[1]+karet[1]} Kg" )
        print("NON-ORGANIK = 400 kg" )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    elif Pemilihan == 3:
        print("KECAMATAN BATURADEN : ")
        print(f"ORGANIK = {plastik[2]+logam[3]+kaca[3]+elektronik[3]+karet[3]} Kg" )
        print("NON-ORGANIK = 400 kg" )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    elif Pemilihan == 4:
        print("KECAMATAN CILONGOK : ")
        print(f"ORGANIK = {plastik[4]+logam[4]+kaca[4]+elektronik[4]+karet[4]} Kg" )
        print("NON-ORGANIK = 400 kg" )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    elif Pemilihan == 5:
        print("KECAMATAN PURWOKERTO BARAT : ")
        print(f"ORGANIK = {plastik[5]+logam[5]+kaca[5]+elektronik[5]+karet[5]} Kg" )
        print("NON-ORGANIK = 400 kg" )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    elif Pemilihan == 6:
        print("KECAMATAN PURWOKERTO SELATAN : ")
        print(f"ORGANIK = {plastik[6]+logam[6]+kaca[6]+elektronik[6]+karet[6]} Kg" )
        print("NON-ORGANIK = 400 kg" )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    elif Pemilihan == 7:
        print("KECAMATAN PURWOKERTO TIMUR : ")
        print(f"ORGANIK = {plastik[7]+logam[7]+kaca[7]+elektronik[7]+karet[7]} Kg" )
        print("NON-ORGANIK = 400 kg" )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    elif Pemilihan == 8:
        print("KECAMATAN SOKARAJA : ")
        print(f"ORGANIK = {plastik[8]+logam[8]+kaca[8]+elektronik[8]+karet[8]} Kg" )
        print("NON-ORGANIK = 400 kg" )
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    else:
        print("TOLONG MASUKAN ANGKA SESUAI DENGAN YANG TERSEDIA!") 
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
        home()

def tampilkanMenu():
        for t in range(1):
            print(f"{t+1}. Jenis Sampah")
            print(f"{t+2}. KEMBALI")
            print(f"{t+3}. KELUAR")
            print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
            
        pilihan = int(input("MASUKKAN PILIHAN => "))
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
        if pilihan == 1:
            tampilkanSampah()
        elif pilihan == 2:
            home()
        elif pilihan == 3:
            sys.exit("Keluar dari program, terima kasih telah menggunakan program kami")
        else:
            print("Input yang dimasukan invalid, harap coba kembali")

def tampilkanSampah():
    print("---ORGANIK---")
    print(f"SISA MAKANAN = {sisa_makanan[0]} Kg")
    print(f"KOTORAN HEWAN = {kotoran_hewan[0]} Kg")
    print(f"DEDAUNAN = {dedaunan[0]} Kg")
    print("─━──━──━──━──━──━──━──━──━──━─")
    print("--NON-ORGANIK--")
    print(f"PLASTIK = {plastik[0]} Kg")
    print(f"LOGAM = {logam[0]} Kg")
    print(f"KACA = {kaca[0]} Kg")
    print(f"ELEKTRONIK = {elektronik[0]} Kg")
    print(f"KARET = {karet[0]} Kg")
    print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")

    while True:
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
        print("1. KEMBALI KE LIST KECAMATAN")
        print("2. HOME")
        print("3. KELUAR")
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")

        pilihan1 = int(input("MASUKKAN PILIHAN => "))
        print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
        if pilihan1 == 1:
            list_kecamatan()
        elif pilihan1 == 2:
            home()
        elif pilihan1 == 3:
            sys.exit("Keluar dari program, terima kasih telah menggunakan program kami")
        else:
            print("Input yang dimasukan invalid, harap coba kembali")

def semua(jenis):
    for i in range(len(kecamatan)):
        gabung.append((kecamatan[i], jenis[i]))
    
def insertion_sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while j >= 0 and array[j][1] < item[1]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item
    return array

def tampilkanSortir():
    jenis_sampah = ["Plastik", "Logam", "Kaca", "Elektronik", "Karet", "Sisa Makanan", "Kotoran Hewan", "Dedaunan"]


    print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    print("Pilih jenis sampah untuk disortir:")
    print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
    for i in range(len(jenis_sampah)) :
        print(f"{i+1} {jenis_sampah[i]} ")

    pilihan = int(input("MASUKKAN PILIHAN => "))
    
home()

