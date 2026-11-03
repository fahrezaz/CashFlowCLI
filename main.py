from akun import registrasi, login, profil, logout


def menu_awal():
    while True:
        print("\n=== CASHFLOW ===")
        print("Sistem Pengelolaan Keuangan Pribadi")
        print("\n1. Registrasi")
        print("2. Login")
        print("0. Keluar")

        pilihan = input("\nPilih menu : ")

        if pilihan == "1":
            registrasi()

        elif pilihan == "2":
            user = login()

            if user:
                menu_utama(user)

        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan CashFlow.")
            break

        else:
            print("Pilihan tidak tersedia!")


def menu_utama(user):
    while True:
        print("\n=== MENU UTAMA ===")
        print(f"Halo, {user['nama_user']}!")
        print("\n1. Profil")
        print("2. Logout")

        pilihan = input("\nPilih menu : ")

        if pilihan == "1":
            profil(user)

        elif pilihan == "2":
            logout()
            break

        else:
            print("Pilihan tidak tersedia!")


menu_awal()