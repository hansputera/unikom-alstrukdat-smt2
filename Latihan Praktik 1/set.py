# Membuat set (duplikat otomatis dihapus)
hadir = {'Andi', 'Budi', 'Citra', 'Andi'}
print(hadir)  # {'Andi', 'Budi', 'Citra'}

terdaftar = {'Budi', 'Citra', 'Dewi'}

# Operasi himpunan
print(hadir | terdaftar)  # Gabungan
print(hadir & terdaftar)  # Irisan: {'Budi', 'Citra'}
print(hadir - terdaftar)  # Selisih: {'Andi'}

# Menambah dan menghapus elemen
hadir.add('Eka')
hadir.discard('Budi')

# Akses via index TIDAK BISA
# hadir[0]  # TypeError: 'set' object is not subscriptable