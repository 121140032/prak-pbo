class Siswa:
    #variable kelas untuk hitung jumlah karyawan
    jumlah_siswa = 0

    #inisiasi var objek
    def __init__(self, nama, no_urut, kelas):
        self.nama = nama
        self.no_urut = no_urut
        self.kelas = kelas
        #tambah jumlah karyawan +1
        Siswa.jumlah_siswa += 1

    # nambah nama Siswa    
    def get_nama(self):
        return self.nama

    # ubah nama Siswa
    def set_nama(self, nama_baru):
        self.nama = nama_baru

    # no urut awal   
    def get_no_urut(self):
        return self.no_urut

    # no urut baru
    def set_no_urut(self, no_urut_baru):
        self.no_urut = no_urut_baru

    # Kelas awal    
    def get_kelas(self):
        return self.kelas

    #Kelas baru
    def set_kelas(self, kelas_baru):
        self.kelas = kelas_baru

    #output
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Kelas: {self.kelas}")
        print(f"No Urut: {self.no_urut}")
        print()
# membuat objek Siswa pertama
siswa1 = Siswa("Antonius Munthe", 1, "Mawar")
siswa1.info()

# mengubah nama Siswa pertama
siswa1.set_nama("ANTONIUS MUNTHE")
print(f"Nama Siswa 1 setelah diubah:", siswa1.get_nama())
print()

# membuat objek Siswa kedua
siswa2 = Siswa(f"Ayda Mariyani", 2, "Melati")
siswa2.info()

# mengubah kelas siswa kedua
siswa2.set_kelas("Mawar")
print("Kelas Siswa 2 setelah diubah:", siswa2.get_kelas())
print()

# membuat objek Siswa ketiga
siswa3 = Siswa(f"Ansel", 2, "Mawar")
siswa3.info()

# mengubah no urut siswa ketiga
siswa3.set_no_urut(3)
print("Nomor Urut siswa 3 setelah diubah:", siswa3.get_no_urut())
print()

# mencetak jumlah siswa yang telah dibuat
print("Jumlah Siswa:", Siswa.jumlah_siswa)
