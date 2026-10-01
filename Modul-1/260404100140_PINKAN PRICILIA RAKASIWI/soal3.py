jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga = 10000

jarak_pulang_pergi = jarak * 2
kebutuhan_bensin = jarak_pulang_pergi / konsumsi
bensin_dibeli = kebutuhan_bensin - sisa_bensin
biaya = bensin_dibeli * harga

print("Jarak pulang-pergi =", jarak_pulang_pergi, "km")
print("Kebutuhan bensin =", kebutuhan_bensin, "liter")
print("Bensin yang harus dibeli =", bensin_dibeli, "liter")
print("Biaya bensin = Rp", biaya)