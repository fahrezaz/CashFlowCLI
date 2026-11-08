from utils import baca_data, simpan_data


FILE_USERS = "data/users.json"


def registrasi():
    users = baca_data(FILE_USERS)

    print("\n===== REGISTRASI =====")

    nama = input("Nama lengkap : ")
    username = input("Username     : ")
    password = input("Password     : ")
    email = input("Email        : ")

    for user in users:
        if user["username"] == username:
            print("Username sudah digunakan!")
            print("Silahkan lakukan registrasi ulang!")
            return

    if len(users) == 0:
        id_user = 1
    else:
        id_user = users[-1]["id_user"] + 1

    user_baru = {
        "id_user": id_user,
        "nama_user": nama,
        "username": username,
        "password": password,
        "email": email
    }

    users.append(user_baru)
    simpan_data(FILE_USERS, users)

    print("Registrasi berhasil!")
    print("Silahkan untuk login di menu Login")


def login():
    users = baca_data(FILE_USERS)

    print("\n===== LOGIN =====")

    username = input("Username : ")
    password = input("Password : ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Login berhasil. Selamat datang, {user['nama_user']}!")
            return user

    print("Username atau password salah!")
    return None


def profil(user):
    print("\n===== PROFIL =====")
    print(f"ID User  : {user['id_user']}")
    print(f"Nama     : {user['nama_user']}")
    print(f"Username : {user['username']}")
    print(f"Email    : {user['email']}")


def logout():
    print("\nLogout berhasil.")