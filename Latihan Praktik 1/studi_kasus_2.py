jadwal_ujian = (
    ('IF201', 'Algoritma dan Struktur Data 2', 'Senin', '08:00', 'Lab Komputer 1'),
    ('IF202', 'Basis Data', 'Selasa', '10:00', 'Lab Komputer 2'),
    ('IF203', 'Pemrograman Python', 'Rabu', '13:00', 'Lab Komputer 3')
)

print("Seluruh jadwal ujian:")
print(jadwal_ujian)

print("\nJadwal ujian pertama:")
print(jadwal_ujian[0])

print("\nData jadwal kedua:")
print("Nama Mata Kuliah :", jadwal_ujian[1][1])
print("Ruang            :", jadwal_ujian[1][4])

print("\nDaftar jadwal ujian:")
for jadwal in jadwal_ujian:
    kode, matkul, hari, jam, ruang = jadwal
    print(f"Kode  : {kode}")
    print(f"Matkul: {matkul}")
    print(f"Hari  : {hari}")
    print(f"Jam   : {jam}")
    print(f"Ruang : {ruang}")
    print("-" * 35)

#jadwal_ujian[0][3] = '09:00'
jadwal_lama = jadwal_ujian[0]
jadwal_baru = (jadwal_lama[0], jadwal_lama[1], jadwal_lama[2], '09:00', jadwal_lama[4])
jadwal_ujian = (jadwal_baru,) + jadwal_ujian[1:]

print("Jadwal setelah revisi:")
for jadwal in jadwal_ujian:
    print(jadwal)

print("=" * 30)
print("Created by HANIF DWY PUTRA S. (NIM: 10125905)")
print("Tgl pengerjaan: 05/04/2026")