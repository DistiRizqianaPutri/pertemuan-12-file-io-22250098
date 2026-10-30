
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                try:
                    nilai = float(baris.strip())

                    if 0 <= nilai <= 100:
                        data.append(nilai)
                    else:
                        print(f"Nilai tidak valid: {baris.strip()}")

                except ValueError:
                    print(f"Data bukan angka: {baris.strip()}")

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI\n")
        file.write("================\n")

        if len(data) == 0:
            file.write("Tidak ada data nilai yang valid.\n")
        else:
            rata_rata = sum(data) / len(data)

            file.write(f"Jumlah data: {len(data)}\n")
            file.write(f"Nilai tertinggi: {max(data)}\n")
            file.write(f"Nilai terendah: {min(data)}\n")
            file.write(f"Rata-rata: {rata_rata:.2f}\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

# Jalankan alur utama
data_nilai = baca_data(input_file)
tulis_rekap(output_file, data_nilai)

print("Rekap berhasil dibuat.")
