# Program Manajemen Peminjaman dan Pengembalian Buku

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return f"Buku '{self.judul}' berhasil dipinjam."
        return f"Buku '{self.judul}' sedang dipinjam."

    def kembalikan(self):
        if not self.tersedia:
            self.tersedia = True
            return f"Buku '{self.judul}' telah dikembalikan."
        return f"Buku '{self.judul}' tidak sedang dipinjam."

    def status(self):
        return f"{self.judul} oleh {self.penulis} - {'Tersedia' if self.tersedia else 'Dipinjam'}"


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = {}

    def tambah_buku(self, judul, penulis):
        self.daftar_buku[judul] = Buku(judul, penulis)

    def tampilkan_buku(self):
        print("\nDaftar Buku di Perpustakaan:")
        for buku in self.daftar_buku.values():
            print(buku.status())

    def pinjam_buku(self, judul):
        if judul in self.daftar_buku:
            print(self.daftar_buku[judul].pinjam())
        else:
            print("Buku tidak ditemukan.")

    def kembalikan_buku(self, judul):
        if judul in self.daftar_buku:
            print(self.daftar_buku[judul].kembalikan())
        else:
            print("Buku tidak ditemukan.")

    def cek_status(self, judul):
        if judul in self.daftar_buku:
            print(self.daftar_buku[judul].status())
        else:
            print("Buku tidak ditemukan.")


def main():
    perpustakaan = Perpustakaan()


    perpustakaan.tambah_buku("Pangeran Kecil", "Antoine de Saint-Exupéry")
    perpustakaan.tambah_buku("Sangkuriang", "Yuliadi Soekardi")
    perpustakaan.tambah_buku("Sang Pemimpi", "Andrea Hirata")

    while True:
        print("\nMenu Manajemen Buku:")
        print("1. Tampilkan Daftar Buku")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Cek Status Buku")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            perpustakaan.tampilkan_buku()
        elif pilihan == "2":
            judul = input("Masukkan judul buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(judul)
        elif pilihan == "3":
            judul = input("Masukkan judul buku yang ingin dikembalikan: ")
            perpustakaan.kembalikan_buku(judul)
        elif pilihan == "4":
            judul = input("Masukkan judul buku yang ingin dicek: ")
            perpustakaan.cek_status(judul)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem manajemen buku.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()