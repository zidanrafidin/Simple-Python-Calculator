print("=== Kalkulator Sederhana ===")

# Input angka pertama
angka1 = float(input("Masukkan angka pertama: "))

# Input operator (+, -, *, /)
operator = input("Pilih operator (+, -, *, /): ")

# Input angka kedua
angka2 = float(input("Masukkan angka kedua: "))

# Proses perhitungan
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Tidak bisa dibagi dengan nol!"
else:
    hasil = "Operator tidak dikenali."

# Menampilkan hasil
print("Hasil:", hasil)