'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

harga_awal = 370000
diskon = 15
def harga_akhir(harga_awal, diskon):
    harga_diskon = (15 / 100) * 370000
    harga_akhir = harga_awal - harga_diskon
    return harga_akhir

harga_awal = float(input("Input Harga: "))
diskon = float(input("Input Diskon: "))

harga_setelah_diskon = harga_akhir(harga_awal, diskon)
print("Harga yang harus dibayar setelah diskon:", harga_setelah_diskon);

