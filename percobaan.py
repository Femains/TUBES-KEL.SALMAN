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
      print("")