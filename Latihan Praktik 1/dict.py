# Membuat dictionary
mahasiswa = {
    'nama': 'Andi',
    'nim': '12345',
    'ipk': 3.75,
    'random': True,
    'random2': False,
    'random3': {
        'hello': 1,
    },
    'random4': [1,2,3]
}

# Mengakses value berdasarkan key
# print(mahasiswa['nama'])   # Andi
# print(mahasiswa.get('nim'))# 12345

nama = mahasiswa.get('nama')
if nama == None:
    print("Gk ada")
else:
    print(nama)
    # Mengubah value
    mahasiswa['ipk'] = 3.80

    # Menambah key baru
    mahasiswa['jurusan'] = 'Informatika'

    # Menghapus key
    # del mahasiswa['nim']
    mahasiswa.pop('nim')

    # Perulangan
    for key, value in mahasiswa.items():
        print(f'{key}: {value}')