from abc import ABC, abstractmethod

class AkunBank(ABC):
    def _init_(self, nama, tahun_daftar, saldo_pelanggan):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo_pelanggan = saldo_pelanggan

    def lihat_saldo(self):
        print(f"Saldo {self.nama}: Rp {self.saldo_pelanggan}")

    @abstractmethod
    def transfer_saldo(self, jumlah_transfer):
        pass

    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def transfer_saldo(self, jumlah_transfer):
        biaya_administrasi = 0
        usia_akun = 2023 - self.tahun_daftar
        
        if jumlah_transfer > 100000:
            if usia_akun >= 3:
                biaya_administrasi = 0
            else:
                biaya_administrasi = 2000
        
        self.saldo_pelanggan -= jumlah_transfer + biaya_administrasi
        print(f"Transfer saldo sebesar Rp {jumlah_transfer} berhasil dilakukan. Biaya administrasi: Rp {biaya_administrasi}")
        self.lihat_saldo()
        
    def lihat_suku_bunga(self):
        usia_akun = 2023 - self.tahun_daftar
        
        if self.saldo_pelanggan >= 1000000000:
            if usia_akun >= 3:
                bunga = 0.01
            else:
                bunga = 0.02
        else:
            bunga = 0.03
            
        print(f"Suku bunga akun {self.nama}: {bunga*100}% per bulan")
        
class AkunSilver(AkunBank):
    def transfer_saldo(self, jumlah_transfer):
        biaya_administrasi = 0
        usia_akun = 2023 - self.tahun_daftar
        
        if jumlah_transfer > 100000:
            if usia_akun >= 3:
                biaya_administrasi = 2000
            else:
                biaya_administrasi = 5000
        
        self.saldo_pelanggan -= jumlah_transfer + biaya_administrasi
        print(f"Transfer saldo sebesar Rp {jumlah_transfer} berhasil dilakukan. Biaya administrasi: Rp {biaya_administrasi}")
        self.lihat_saldo()
        
    def lihat_suku_bunga(self):
        usia_akun = 2023 - self.tahun_daftar
        
        if self.saldo_pelanggan >= 10000000:
            if usia_akun >= 3:
                bunga = 0.01
            else:
                bunga = 0.02
        else:
            bunga = 0.03
            
        print(f"Suku bunga akun {self.nama}: {bunga*100}% per bulan")
        

