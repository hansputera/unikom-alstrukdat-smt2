# Membuat tuple
koordinat = (-6.2, 106.8)
hari_kerja = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat')

# Mengakses elemen
print(koordinat[0])    # -6.2
print(hari_kerja[2])   # Rabu

# Mencoba mengubah elemen (akan ERROR)
# koordinat[0] = 10
# TypeError: 'tuple' object does not support item assignment

# Solusi: buat tuple baru
koordinat_baru = (10, koordinat[1])
print(koordinat_baru)  # (10, 106.8)