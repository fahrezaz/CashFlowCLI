import json

def baca_data(nama_file):
    with open(nama_file, "r") as file:
        return json.load(file)


def simpan_data(nama_file, data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)