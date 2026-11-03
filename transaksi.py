from datetime import datetime
from utils import baca_data, simpan_data

FILE_TRANSAKSI = "data/transaksi.json"

def tambah_transaksi(id_user, jenis_transaksi):
    print(f"\n--- TAMBAH {jenis_transaksi.upper()} ---")

    while True:
        try:
            nominal = int(input("Masukkan nominal uang: "))
            if nominal <= 0:
                print("Nominal kurang dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid!")

    kategori = input("Masukkan nama kategori (cth: makanan, gaji, belanja dll): ").strip()

    keterangan = input("Masukkan keterangan: ").strip()

    tanggal_sekarang = datetime.now().strftime("%Y-%m-%d")

    try:
        daftar_transaksi = baca_data(FILE_TRANSAKSI)
    except:
        daftar_transaksi = []

    transaksi_baru = {
        "id_transaksi": len(daftar_transaksi) + 1,
        "id_user": id_user,
        "jenis_transaksi": jenis_transaksi,
        "nominal": nominal,
        "kategori": kategori,
        "keterangan": keterangan,
        "tanggal_transaksi": tanggal_sekarang
    }

    daftar_transaksi.append(transaksi_baru)
    simpan_data(FILE_TRANSAKSI, daftar_transaksi)
    print(f"\n Berhasil mencatat {jenis_transaksi} baru.")

def menu_transaksi(id_user):
    while True:
        print("\n======= MENU TRANSAKSI =======")
        print("1. Tambah Pemasukan Uang")
        print("2. Tambah Pengeluaran Uang")
        print("3. Kembali")
        
        pilihan = input("Silahkan pilih 1-3: ").strip()
        
        if pilihan == "1":
            tambah_transaksi(id_user, "Pemasukan")
        elif pilihan == "2":
            tambah_transaksi(id_user, "Pengeluaran")
        elif pilihan == "3":
            print("Kembali ke menu")
            break
        else:
            print("Pilihan tidak valid, silahkan masukkan pilihan menu dengan benar")

