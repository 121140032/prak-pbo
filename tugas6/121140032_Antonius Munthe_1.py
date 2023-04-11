class Operasi:
    def tambah(self, a, b):
        return a + b
    
    def kurang(self, a, b):
        return a - b
    
    def kali(self, a, b):
        return a * b
    
    def bagi(self, a, b):
        return a / b
    

class Tampilan:
    def tampilkan_hasil(self, hasil):
        print("Hasil perhitungan: ", hasil)


class Kalkulator(Operasi, Tampilan):
    def hitung(self, operasi, a, b):
        if operasi == "+":
            hasil = self.tambah(a, b)
        elif operasi == "-":
            hasil = self.kurang(a, b)
        elif operasi == "*":
            hasil = self.kali(a, b)
        elif operasi == "/":
            hasil = self.bagi(a, b)
        else:
            print("Operasi tidak valid")
            return
        
        self.tampilkan_hasil(hasil)


# contoh penggunaan
kalkulator = Kalkulator()
a = float(input("Masukkan bilangan: "))
operasi = input("Masukkan jenis operasi (+,-,*, atau /): ")
b = float(input("Masukkan bilangan: "))

kalkulator.hitung(operasi, a, b)
