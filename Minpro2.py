# nama  : Muhammad Islami Pasya
# NIM   : 2509116108    
# Kelas : Sistem Informasi C
# Tugas : MINPRO 2 - Sistem Pembayaran Tagihan Listrik

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "user": {"password": "user123", "role": "User"}
}

tagihan_db = {}

def login():
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    user = users.get(username)
    if user and user["password"] == password:
        print(f"Login berhasil sebagai {user['role']}\n")
        return user["role"]
    else:
        print("Login gagal! Username atau password salah.\n")
        return None

# CRUD untuk ADMIN
def create_tagihan():
    try:
        id_pelanggan = input("ID Pelanggan: ")
        nama = input("Nama Pelanggan: ")
        bulan = input("Bulan Tagihan: ")
        jumlah = float(input("Jumlah Tagihan (Rp): "))
        tagihan_db[id_pelanggan] = {
            "nama": nama,
            "bulan": bulan,
            "jumlah": jumlah,
            "status": "Belum Lunas"
        }
        print("Data tagihan berhasil ditambahkan\n")
    except Exception as e:
        print(f"Terjadi kesalahan input Karna harus angka bukan huruf: {e}\n")

def read_tagihan():
    if not tagihan_db:
        print("Belum ada data tagihan.\n")
        return
    for id_pelanggan, data in tagihan_db.items():
        print(f"ID: {id_pelanggan}, Nama: {data['nama']}, Bulan: {data['bulan']}, "
                    f"Jumlah: Rp{data['jumlah']}, Status: {data['status']}")
    print()

def update_tagihan():
    id_pelanggan = input("Masukkan ID Pelanggan yang ingin diupdate: ")
    if id_pelanggan in tagihan_db:
        try:
            nama = input("Nama baru: ")
            bulan = input("Bulan baru: ")
            jumlah = float(input("Jumlah baru (Rp): "))
            status = input("Status (Lunas/Belum Lunas): ")
            tagihan_db[id_pelanggan] = {
                "nama": nama,
                "bulan": bulan,
                "jumlah": jumlah,
                "status": status
            }
            print("Data tagihan berhasil diupdate\n")
        except Exception as e:
            print(f"Terjadi kesalahan input: {e}\n")
    else:
        print("ID Pelanggan tidak ditemukan\n")

def delete_tagihan():
    id_pelanggan = input("Masukkan ID Pelanggan yang ingin dihapus: ")
    if id_pelanggan in tagihan_db:
        del tagihan_db[id_pelanggan]
        print("Data tagihan berhasil dihapus\n")
    else:
        print("ID Pelanggan tidak ditemukan\n")

# Fitur untuk USER
def bayar_tagihan():
    id_pelanggan = input("Masukkan ID Pelanggan: ")
    if id_pelanggan in tagihan_db:
        if tagihan_db[id_pelanggan]["status"] == "Lunas":
            print("Tagihan sudah lunas.\n")
        else:
            print(f"Tagihan {tagihan_db[id_pelanggan]['nama']} "
                f"bulan {tagihan_db[id_pelanggan]['bulan']} "
                f"sebesar Rp{tagihan_db[id_pelanggan]['jumlah']}")
            konfirmasi = input("Bayar sekarang? (y/n): ")
            if konfirmasi.lower() == "y":
                tagihan_db[id_pelanggan]["status"] = "Lunas"
                print("Pembayaran berhasil! Tagihan sudah Lunas.\n")
            else:
                print("Pembayaran dibatalkan.\n")
    else:
        print("ID Pelanggan tidak ditemukan.\n")

def main():
    role = None
    while not role:
        role = login()

    while True:
        print("=== MENU ===")
        if role == "Admin":
            print("1. Tambah Tagihan")
            print("2. Lihat Data Tagihan")
            print("3. Update Data Tagihan")
            print("4. Hapus Data Tagihan")
            print("5. Logout")
            print("6. Keluar")
        elif role == "User":
            print("1. Lihat Data Tagihan")
            print("2. Bayar Tagihan")
            print("3. Logout")
            print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if role == "Admin":
            if pilihan == "1":
                create_tagihan()
            elif pilihan == "2":
                read_tagihan()
            elif pilihan == "3":
                update_tagihan()
            elif pilihan == "4":
                delete_tagihan()
            elif pilihan == "5":
                print("Logout...\n")
                role = None
                while not role:
                    role = login()
            elif pilihan == "6":
                print("Terima Kasih Sudah Menggunakan Program Kami.")
                break
            else:
                print("Pilihan tidak valid\n")

        elif role == "User":
            if pilihan == "1":
                read_tagihan()
            elif pilihan == "2":
                bayar_tagihan()
            elif pilihan == "3":
                print("Logout...\n")
                role = None
                while not role:
                    role = login()
            elif pilihan == "4":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid\n")

if __name__ == "__main__":
    main()