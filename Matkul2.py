awal = int(input("Masukkan bilangan awal: "))
akhir = int(input("Masukkan bilangan akhir: "))

for i in range(awal, akhir + 1, 3):
    hasil = i * i
    print(f"{i} * {i} = {hasil}")