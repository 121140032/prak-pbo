#Antonius Munthe
#121140032
#PBO Rb 

idcek = ("informatika")
passcek =("12345678")

i = int(1)

while(i <= 3):
        idin = input("Username anda: ")
        passin = input("Password anda: ")
        if (idin == idcek and passin == passcek):
            print ("Login Berhasil!")
            break
        elif(i == 3):
              print("Akun anda diblokir")
              break
        else:
            print ("Username atau Password salah coba lagi")
            i+= 1
        




