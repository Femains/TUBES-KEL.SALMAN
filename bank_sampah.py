
kecamatan = ["Ajibarang", "Banyumas", "Baturaden", "Cilongok", "Purwokerto Barat", "Purwokerto Selatan", "Purwokerto Timur", "Sokaraja"]

plastik = [160, 225, 135, 190, 255, 320, 245, 180]
logam =[237, 183, 329, 158, 274, 195, 321, 276]
kaca = [146, 83, 101, 58, 219, 155, 213, 180]
elektronik = [14, 56, 120, 90, 75, 65, 78, 25]
karet = [114, 210, 78, 98, 153, 79, 82, 126]

sisa_makanan = [78, 58, 12, 36, 69, 45, 87, 20]
kotoran_hewan = [38, 92, 14, 69, 80, 24, 56, 73]
dedaunan = [53, 21, 84, 10, 76, 33, 95, 47]

def home():
    #while True:
        print("BANK SAMPAH YANG ADA DI KABUPATEN BANYUMAS")
        print ("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
        for i in range(len(kecamatan)) :
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

def tampilkanMenu():
    while True:
        for t in range(1):
            print(f"{t+1} Jenis Sampah")
            print(f"{t+2} KEMBALI")
            print(f"{t+3} KELUAR")
            print("─━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━──━─")
            
home()

