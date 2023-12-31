rekomendasiAndi = {
    "produk" : ["TV", "headphone" , "baju", "gitar", "sepatu", "kamera"],
    "kategori" : ["elektronik" , "elektronik", "fashion", "musik", "olahraga", "elektronik"],
    "harga" : [1000, 200, 50, 300, 80, 600]
}

data_pelanggan = {
    "nama" : ["Rina", "Budi", "hartono"],
    "minat" : [["elektronik", "musik"],["fashion", "musik"],["olahraga", "elektronik"]],
    "beli" : [["TV", "headphone"],["baju","gitar"],["olahraga", "elektronik"]]
}

def proses(name):
    nameIndex = data_pelanggan["nama"].index(name)
    rekomendasiList = []
    for j in data_pelanggan["minat"][nameIndex]:
        kategoriIndex = 0
        for k in rekomendasiAndi["kategori"]:
            if j == k:
                rekomendasiList.append(rekomendasiAndi["produk"][kategoriIndex])
            kategoriIndex += 1
    return rekomendasiList

for n in data_pelanggan["nama"]:
    print("Rekomendasi item untuk", n, "=", proses(n))