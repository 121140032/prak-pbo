class Bio:

    def __init__(self, nama, nim, prodi, kelas, sks):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kelas = kelas
        self.sks = sks

    def Bio(self):
        print("Nama Mahasiswa: ", self.nama)
        print("NIM Mahasiswa: ", self.nim)
        print("Prodi Mahasiswa: ", self.prodi)
        print("Kelas Mahasiswa: ", self.kelas)
        print("Jumlah SKS Mahasiswa: ", self.sks)

biodata1 = Bio("Antonius Munthe", 121140032, "Teknik Informatika", "RB", 23)

biodata1.Bio()
