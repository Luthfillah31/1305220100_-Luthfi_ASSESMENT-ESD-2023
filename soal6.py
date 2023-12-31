menu = {
    "nama" : ["ayam goreng krispi", "ayam puk puk", "ayam bakar", "es teh", "es jeruk"],
    "tipe" : ["makanan", "makanan", "makanan", "minuman", "minuman"],
    "harga" : [15000,13000,20000,5000,7000]
}

rehan = ["ayam bakar" , "ayam bakar" , "es teh"]
amba = ["ayam puk puk", "es teh", "es teh", "es teh"]
faiz = ["ayam goreng krispi", "ayam puk puk", "ayam bakar", "es teh", "es jeruk"]

def prosesPrice(person):
    price = 0
    for i in person:
        index = person.index(i)
        if menu["tipe"][index] == "makanan":
            price += menu["harga"][index] * ((12/10))
        elif menu["tipe"][index] == "minuman":
            price += menu["harga"][index] * (118/100)
    return price

print("Total biaya Rehan Whangsap :",prosesPrice(rehan))
print("Total biaya Amba roni :",prosesPrice(amba))
print("Total biaya Faiz ngawi :",prosesPrice(faiz))

