## NIM: 10125905
## Nama: HANIF DWY PUTRA S.
## Kelas: IF-10K
## Matkul: Algoritma Struktur Data 2
## Case: Kalkulator dan Simulasi Investasi dan Bunga

print('=' * 30)
print("  APLIKASI KALKULATOR KEUANGAN & INVESTASI  ")
print('=' * 30)
print("  1. Bunga Tabungan Sederhana (Simple Interest)")
print("  2. Bunga Majemuk (Compound Interest)")
print("  3. Simulasi Cicilan KPR / Kredit")
print("  4. Estimasi Dana Pensiun")
print("  0. Keluar")
print('=' * 30)
pilihan = int(input("Pilihan Anda ? "))

def simpInterest(pokok, rate, tahun):
    return pokok * (rate / 100) * tahun

def simpTotal(pokok, rate, tahun):
    return pokok + simpInterest(pokok, rate, tahun)

def showSimpInterest(pokok, rate, tahun):
    print("\n--- Hasil Simulasi Bunga Sederhana ---")
    print(f"  Modal Awal          : Rp {pokok:,.0f}")
    print(f"  Suku Bunga / Tahun  : {rate}%")
    print(f"  Durasi              : {tahun} tahun")
    print(f"  Total Bunga         : Rp {simpInterest(pokok, rate, tahun):,.2f}")
    print(f"  Total Akhir         : Rp {simpTotal(pokok, rate, tahun):,.2f}")


def compTotal(pokok, rate, tahun, freq):
    return pokok * ((1 + (rate / 100) / freq) ** (freq * tahun))

def compProfit(pokok, rate, tahun, freq):
    return compTotal(pokok, rate, tahun, freq) - pokok

def showCompInterest(pokok, rate, tahun, freq):
    labels = {1: "Tahunan", 2: "Semesteran", 4: "Kuartalan", 12: "Bulanan"}
    label  = labels.get(freq, f"{freq}x/tahun")
    print("\n--- Hasil Simulasi Bunga Majemuk ---")
    print(f"  Modal Awal          : Rp {pokok:,.0f}")
    print(f"  Suku Bunga / Tahun  : {rate}%")
    print(f"  Durasi              : {tahun} tahun")
    print(f"  Frekuensi Bunga     : {label}")
    print(f"  Total Keuntungan    : Rp {compProfit(pokok, rate, tahun, freq):,.2f}")
    print(f"  Total Akhir         : Rp {compTotal(pokok, rate, tahun, freq):,.2f}")


def calcInstallment(harga, dp, rate, tahun):
    principal    = harga - (harga * dp / 100)
    monthlyRate  = (rate / 100) / 12
    n            = tahun * 12
    cicilan      = principal * (monthlyRate * (1 + monthlyRate)**n) / \
                   ((1 + monthlyRate)**n - 1)
    return cicilan, principal

def calcTotalPay(cicilan, tahun):
    return cicilan * tahun * 12

def showKPR(harga, dp, rate, tahun):
    cicilan, principal = calcInstallment(harga, dp, rate, tahun)
    totalPay           = calcTotalPay(cicilan, tahun)
    uangMuka           = harga * dp / 100
    print("\n--- Hasil Simulasi KPR / Kredit ---")
    print(f"  Harga Properti      : Rp {harga:,.0f}")
    print(f"  Uang Muka ({dp}%)     : Rp {uangMuka:,.0f}")
    print(f"  Pokok Pinjaman      : Rp {principal:,.0f}")
    print(f"  Bunga / Tahun       : {rate}%")
    print(f"  Tenor               : {tahun} tahun ({tahun*12} bulan)")
    print(f"  Cicilan / Bulan     : Rp {cicilan:,.2f}")
    print(f"  Total Pembayaran    : Rp {totalPay:,.2f}")
    print(f"  Total Bunga Dibayar : Rp {totalPay - principal:,.2f}")


def calcRetireFV(monthly, rate, tahun):
    r  = (rate / 100) / 12
    n  = tahun * 12
    fv = monthly * (((1 + r)**n - 1) / r)
    return fv

def calcTotalDeposit(monthly, tahun):
    return monthly * tahun * 12

def showRetire(monthly, rate, tahun):
    fv      = calcRetireFV(monthly, rate, tahun)
    deposit = calcTotalDeposit(monthly, tahun)
    print("\n--- Hasil Simulasi Dana Pensiun ---")
    print(f"  Tabungan / Bulan    : Rp {monthly:,.0f}")
    print(f"  Imbal Hasil / Tahun : {rate}%")
    print(f"  Jangka Waktu        : {tahun} tahun")
    print(f"  Total Uang Disetor  : Rp {deposit:,.0f}")
    print(f"  Keuntungan Investasi: Rp {fv - deposit:,.2f}")
    print(f"  Dana Pensiun Akhir  : Rp {fv:,.2f}")


while pilihan > 0:
    print()
    if pilihan == 1:
        pokok = float(input("  Masukkan Modal Awal (Rp)        : "))
        rate  = float(input("  Masukkan Suku Bunga per Tahun % : "))
        tahun = int(input  ("  Masukkan Durasi (tahun)         : "))
        showSimpInterest(pokok, rate, tahun)

    elif pilihan == 2:
        pokok = float(input("  Masukkan Modal Awal (Rp)        : "))
        rate  = float(input("  Masukkan Suku Bunga per Tahun % : "))
        tahun = int(input  ("  Masukkan Durasi (tahun)         : "))
        print("  Frekuensi Penghitungan Bunga:")
        print("   [1] Tahunan  [2] Semesteran  [4] Kuartalan  [12] Bulanan")
        freq  = int(input  ("  Pilih Frekuensi                 : "))
        showCompInterest(pokok, rate, tahun, freq)

    elif pilihan == 3:
        harga = float(input("  Masukkan Harga Properti (Rp)    : "))
        dp    = float(input("  Masukkan Uang Muka (%)          : "))
        rate  = float(input("  Masukkan Bunga KPR per Tahun %  : "))
        tahun = int(input  ("  Masukkan Tenor (tahun)          : "))
        showKPR(harga, dp, rate, tahun)

    elif pilihan == 4:
        monthly = float(input("  Tabungan Rutin per Bulan (Rp)   : "))
        rate    = float(input("  Imbal Hasil per Tahun %         : "))
        tahun   = int(input  ("  Jangka Waktu (tahun)            : "))
        showRetire(monthly, rate, tahun)

    else:
        print("  Pilihan tidak tersedia!")

    print()
    print('='*45)
    print("  APLIKASI KALKULATOR KEUANGAN & INVESTASI  ")
    print('='*45)
    print("  1. Bunga Tabungan Sederhana (Simple Interest)")
    print("  2. Bunga Majemuk (Compound Interest)")
    print("  3. Simulasi Cicilan KPR / Kredit")
    print("  4. Estimasi Dana Pensiun")
    print("  0. Keluar")
    print('='*45)
    pilihan = int(input("Pilihan ? "))

else:
    print()
    print(" Terima kasih telah menggunakan program :)")