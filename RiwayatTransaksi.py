import json
import os
 
FILE_TRANSAKSI = "data/transaksi.json"
FILE_KATEGORI = "data/kategori.json"
 
 
def baca_data(nama_file):
    if not os.path.exists(nama_file):
        return []
    with open(nama_file, "r") as f:
        return json.load(f)
 
 
def format_rupiah(angka):
    # 1500000 -> Rp1.500.000
    return "Rp" + format(angka, ",").replace(",", ".")
 
 
def cari_nama_kategori(id_kategori):
    semua = baca_data(FILE_KATEGORI)
    for k in semua:
        if k["id_kategori"] == id_kategori:
            return k["nama_kategori"]
    return "-"
 
 
def ambil_transaksi_user(user, jenis=None):
    # jenis = None (semua), "pemasukan", atau "pengeluaran"
    semua = baca_data(FILE_TRANSAKSI)
    hasil = []
    for t in semua:
        if t["id_user"] == user["id_user"]:
            if jenis is None or t["jenis_transaksi"] == jenis:
                hasil.append(t)
 
    # urutkan dari tanggal terbaru
    hasil.sort(key=lambda x: x["tanggal_transaksi"], reverse=True)
    return hasil
 
 
def tampilkan_riwayat(daftar, judul):
    print("\n--- " + judul + " ---")
 
    if len(daftar) == 0:
        print("Belum ada transaksi.")
        return
 
    print("Tanggal    | Jenis       | Kategori        | Nominal        | Keterangan")
    print("-" * 80)
 
    total = 0
    for t in daftar:
        nama_kategori = cari_nama_kategori(t["id_kategori"])
        print(t["tanggal_transaksi"].ljust(10), "|",
              t["jenis_transaksi"].ljust(11), "|",
              nama_kategori.ljust(15), "|",
              format_rupiah(t["nominal"]).ljust(14), "|",
              t["keterangan"])
        total += t["nominal"]
 
    print("-" * 80)
    print("Jumlah transaksi :", len(daftar))
    print("Total nominal    :", format_rupiah(total))
 
 
def riwayat_semua(user):
    daftar = ambil_transaksi_user(user)
    tampilkan_riwayat(daftar, "Semua Transaksi")
 
 
def riwayat_pemasukan(user):
    daftar = ambil_transaksi_user(user, "pemasukan")
    tampilkan_riwayat(daftar, "Riwayat Pemasukan")
 
 
def riwayat_pengeluaran(user):
    daftar = ambil_transaksi_user(user, "pengeluaran")
    tampilkan_riwayat(daftar, "Riwayat Pengeluaran")
 
 
def menu_riwayat(user):
    while True:
        print("\n========== RIWAYAT TRANSAKSI ==========")
        print("1. Semua Transaksi")
        print("2. Pemasukan")
        print("3. Pengeluaran")
        print("4. Kembali")
 
        pilih = input("Pilih: ")
 
        if pilih == "1":
            riwayat_semua(user)
        elif pilih == "2":
            riwayat_pemasukan(user)
        elif pilih == "3":
            riwayat_pengeluaran(user)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")

 
if __name__ == "__main__":
    user_coba = {"id_user": 1, "nama_user": "Fahreza Zulfaqi"}
    menu_riwayat(user_coba)