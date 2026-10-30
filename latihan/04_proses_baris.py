
with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for nomor, baris in enumerate(file, start=1):
        baris = baris.strip()

        if not baris:
            continue

        try:
            nim, teks_nilai = baris.split(",")
            print(nim, float(teks_nilai))

        except ValueError:
            print(f"Baris {nomor} tidak valid: {baris}")

