print("Program menampilkan bilangan terbesar dari n sebuah data yang di Inputkan")

R = 1
maximum = 0

while R !=0:

    if R > maximum:
        maximum = R

    R = int(input("Masukkan bilangan:"))

    if R == 0:
        break

print("Bilangan terbesar adalah:", maximum)
