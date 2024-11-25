a = int(input("Masukan nilai a: "))
b = int(input("Masukan nilai b: "))
c = int(input("Masukan nilai c: "))

if a > b:
    if a > c:
        print("a terbesar")
    else:
        print("c terbesar")
else:
    if b > c:
        print("b terbesar")
    else:
        print("c terbesar")