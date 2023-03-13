class Etol:
    list_pelanggan = []

    def __init__(self, no_seri_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_seri_pelanggan = no_seri_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.__class__.list_pelanggan.append(self)

    def lihat_menu(self):       
        print("Selamat Datang di Layanan E-Tol")     
        print("Pilihan Menu:")
        print("1. Lihat Saldo")
        print("2. Bayar Tol")
        print("3. Transfer Saldo")
        print("4. Keluar")


    def lihat_saldo(self):
        print(f"Saldo Anda saat ini: {self.__jumlah_saldo:,}")

    def bayar_tol(self, jumlah):
        if jumlah > self.__jumlah_saldo:
            print("Saldo Anda tidak cukup")
        else:
            self.__jumlah_saldo -= jumlah
            print(f"Berhasil melakukan pembayaran tol {jumlah:,}")
            print(f"Saldo Anda saat ini adalah {self.__jumlah_saldo:,}")

    def transfer_saldo(self, no_seri_pelanggan_tujuan, jumlah):
        seri_pelanggan_tujuan = None
        for pelanggan in self.__class__.list_pelanggan:
            if pelanggan._Etol__no_seri_pelanggan == no_seri_pelanggan_tujuan:
                seri_pelanggan_tujuan = pelanggan
                break
        if seri_pelanggan_tujuan is None:
            print("Nomor seri tujuan tidak ditemukan")
        elif jumlah > self.__jumlah_saldo:
            print("Saldo Anda tidak cukup")
        else:
            self.__jumlah_saldo -= jumlah
            seri_pelanggan_tujuan._Etol__jumlah_saldo += jumlah
            print(f"Transfer sebesar Rp{jumlah:,} berhasil dilakukan ke nomor seri tujuan {no_seri_pelanggan_tujuan}")
            print(f"Saldo Anda saat ini adalah Rp{self.__jumlah_saldo:,}")

    def main_menu(self):
        while True:
            self.lihat_menu()
            input_menu = input('Masukkan nomor input: ')
            if input_menu == '1':
                self.lihat_saldo()
            elif input_menu == '2':
                self.bayar_tol()
            elif input_menu == '3':
                self.transfer_saldo()
            elif input_menu == '4':
                break
            else:
                print('Nomor seri tidak ditemukan')

#  instansi E-tol
Akun1 = Etol(121140032, "Antonius Munthe", 500000)
Akun2 = Etol(121140033, "Antonius", 400000)
Akun3 = Etol(121140034, "Munthe", 300000)

# penggunaan fungsi
Akun1.main_menu()
