def calculate_final_price():
    member = input("Masukan Identitas (M untuk member): ")
    
    try:
        harga = float(input("Masukan Harga: "))
        if harga < 0:
            print("Harga tidak boleh negatif.")
            return
        
        harga_asli = harga
        hargaakhir = harga

        if member == "M":
            hargaakhir -= harga * 0.02
            print("Anda mendapatkan tambahan diskon sebesar 2%")
        else:
            print("Tidak mendapatkan diskon tambahan dari member atau anda bukanlah member")

        if harga_asli >= 200000:
            hargaakhir -= harga_asli * 0.04
            print("Anda berhak mendapatkan diskon sebesar 4%")
        elif harga_asli >= 100000:
            hargaakhir -= harga_asli * 0.03
            print("Anda berhak mendapatkan diskon sebesar 3%")

        print(f"Total yang harus dibayar adalah: {hargaakhir:.2f}")

    except ValueError:
        print("Input tidak valid. Pastikan untuk memasukkan angka untuk harga.")

calculate_final_price()