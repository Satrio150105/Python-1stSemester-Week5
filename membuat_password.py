def buat_user_baru():
    username = input("Masukkan Username: ")
    email = input("Masukkan Email: ")
    password = input("Masukkan Password: ")    
    
    if not username:
        print("Username tidak boleh kosong.")
        return    
    if "@" not in email:
        print("Email harus mengandung '@'.")
        return    
    if len(password) <= 8:
        print("Password harus lebih dari 8 karakter.")
        return
    
    print("User  baru berhasil dibuat!")

buat_user_baru()