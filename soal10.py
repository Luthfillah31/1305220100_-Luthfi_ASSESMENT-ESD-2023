pembayaran = [10000, 5000, 178000]
belanja = [7500, 1100, 90500]

mataUang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

def kembalian(bayar, dibelanja):
    kembali = bayar - dibelanja
    uangKembalian = {}
    for i in mataUang:
        while (kembali >= i):
            if f"{i}" not in uangKembalian:
                uangKembalian[f"{i}"] = 1
                kembali -= i
            else: 
                uangKembalian[f"{i}"] += 1
                kembali -= i
    return dict(reversed(list(uangKembalian.items())))

for p,b in zip(pembayaran,belanja):
    print(kembalian(p,b))
        
