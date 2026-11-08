import json
import os
 
FILE_KATEGORI = "data/kategori.json"
FILE_TRANSAKSI = "data/transaksi.json"
 
 
def baca_data(nama_file):
    if not os.path.exists(nama_file):
        return []
    with open(nama_file, "r") as f:
        return json.load(f)
 
 
def simpan_data(nama_file, data):
    with open(nama_file, "w") as f:
        json.dump(data, f, indent=4)
 
 
def buat_id_baru(data):
    if len(data) == 0:
        return 1
    id_terbesar = 0
    for item in data:
        if item["id_kategori"] > id_terbesar:
            id_terbesar = item["id_kategori"]
    return id_terbesar + 1
 
 
def ambil_kategori_user(user):
    semua = baca_data(FILE_KATEGORI)
    hasil = []
    for k in semua:
        if k["id_user"] == user["id_user"]:
            hasil.append(k)
    return hasil
 
 
def pilih_jenis():
    print("Jenis kategori:")
    print("1. Pemasukan")
    print("2. Pengeluaran")
    pilihan = input("Pilih jenis (1/2): ")
    if pilihan == "1":
        return "pemasukan"
    elif pilihan == "2":
        return "pengeluaran"
    else:
        return None
 
 
def tambah_kategori(user):
    print("\n--- Tambah Kategori ---")
    nama = input("Nama kategori: ").strip()
    if nama == "":
        print("Nama kategori tidak boleh kosong!")
        return
 
    jenis = pilih_jenis()
    if jenis is None:
        print("Pilihan jenis tidak valid!")
        return
 
    semua = baca_data(FILE_KATEGORI)
 
    # cek kategori
    for k in semua:
        if (k["id_user"] == user["id_user"]
                and k["nama_kategori"].lower() == nama.lower()
                and k["jenis_kategori"] == jenis):
            print("Kategori tersebut sudah ada!")
            return
 
    kategori_baru = {
        "id_kategori": buat_id_baru(semua),
        "id_user": user["id_user"],
        "nama_kategori": nama,
        "jenis_kategori": jenis
    }
    semua.append(kategori_baru)
    simpan_data(FILE_KATEGORI, semua)
    print("Kategori berhasil ditambahkan!")
 
 
def lihat_kategori(user):
    print("\n--- Daftar Kategori ---")
    daftar = ambil_kategori_user(user)
 
    if len(daftar) == 0:
        print("Belum ada kategori.")
        return
 
    print("ID  | Nama Kategori        | Jenis")
    print("-" * 42)
    for k in daftar:
        print(str(k["id_kategori"]).ljust(3), "|",
              k["nama_kategori"].ljust(20), "|",
              k["jenis_kategori"])
 
 
def ubah_kategori(user):
    print("\n--- Ubah Kategori ---")
    lihat_kategori(user)
    if len(ambil_kategori_user(user)) == 0:
        return
 
    try:
        id_ubah = int(input("\nMasukkan ID kategori yang diubah: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
 
    semua = baca_data(FILE_KATEGORI)
    for k in semua:
        # pastikan kategori ini milik user yang login
        if k["id_kategori"] == id_ubah and k["id_user"] == user["id_user"]:
            nama_baru = input("Nama baru (kosongkan jika tidak diubah): ").strip()
            if nama_baru != "":
                k["nama_kategori"] = nama_baru
            simpan_data(FILE_KATEGORI, semua)
            print("Kategori berhasil diubah!")
            return
 
    print("Kategori tidak ditemukan!")
 
 
def kategori_dipakai(id_kategori):
    # cek apakah kategori sudah dipakai di transaksi
    transaksi = baca_data(FILE_TRANSAKSI)
    for t in transaksi:
        if t["id_kategori"] == id_kategori:
            return True
    return False
 
 
def hapus_kategori(user):
    print("\n--- Hapus Kategori ---")
    lihat_kategori(user)
    if len(ambil_kategori_user(user)) == 0:
        return
 
    try:
        id_hapus = int(input("\nMasukkan ID kategori yang dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
 
    if kategori_dipakai(id_hapus):
        print("Kategori tidak bisa dihapus karena sudah dipakai di transaksi!")
        return
 
    semua = baca_data(FILE_KATEGORI)
    for k in semua:
        if k["id_kategori"] == id_hapus and k["id_user"] == user["id_user"]:
            yakin = input("Yakin hapus '" + k["nama_kategori"] + "'? (y/n): ")
            if yakin.lower() == "y":
                semua.remove(k)
                simpan_data(FILE_KATEGORI, semua)
                print("Kategori berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
            return
 
    print("Kategori tidak ditemukan!")
 
 
def menu_kategori(user):
    # dipanggil dari main.py, user = data user yang sedang login
    while True:
        print("\n========== KATEGORI ==========")
        print("1. Tambah Kategori")
        print("2. Lihat Kategori")
        print("3. Ubah Kategori")
        print("4. Hapus Kategori")
        print("5. Kembali")
 
        pilih = input("Pilih: ")
 
        if pilih == "1":
            tambah_kategori(user)
        elif pilih == "2":
            lihat_kategori(user)
        elif pilih == "3":
            ubah_kategori(user)
        elif pilih == "4":
            hapus_kategori(user)
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid!")
 
 
if __name__ == "__main__":
    user_coba = {"id_user": 1, "nama_user": "Fahreza Zulfaqi"}
    menu_kategori(user_coba)
 