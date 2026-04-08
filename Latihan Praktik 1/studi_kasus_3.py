peserta_seminar = {'Dewi', 'Andi', 'Citra', 'Budi', 'Andi'}
pendaftar_baru = {'Fajar', 'Eka'}
peserta_hadir = {'Andi', 'Citra', 'Eka', 'Gina'}

print("Peserta seminar awal:")
print(peserta_seminar)

peserta_seminar.add('Hani')
print("\nSetelah tambah Hani:")
print(peserta_seminar)

peserta_seminar.update(pendaftar_baru)
print("\nSetelah update pendaftar baru:")
print(peserta_seminar)

peserta_seminar.discard('Dewi')
print("\nSetelah hapus Dewi:")
print(peserta_seminar)

print("\nDaftar peserta seminar:")
for nama in peserta_seminar:
    print(nama)

gabungan = peserta_seminar | peserta_hadir
print("\nGabungan peserta seminar dan hadir:")
print(gabungan)

irisan = peserta_seminar & peserta_hadir
print("\nIrisan peserta seminar dan hadir:")
print(irisan)

terdaftar_tidak_hadir = peserta_seminar - peserta_hadir
print("\nPeserta terdaftar tetapi tidak hadir:")
print(terdaftar_tidak_hadir)

hadir_tidak_terdaftar = peserta_hadir - peserta_seminar
print("\nPeserta hadir tetapi tidak ada di daftar seminar:")
print(hadir_tidak_terdaftar)

# print(peserta_seminar[0])

print("=" * 30)
print("Created by HANIF DWY PUTRA S. (NIM: 10125905)")
print("Tgl pengerjaan: 05/04/2026")
