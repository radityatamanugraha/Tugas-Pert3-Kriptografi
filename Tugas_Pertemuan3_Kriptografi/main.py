def enkripsi(teks, shift):
    hasil = ""
    for char in teks:
        if char.isalpha():
            kode = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char) - kode + shift) % 26 + kode)
        else:
            hasil += char
    return hasil

def dekripsi(teks, shift):
    return enkripsi(teks, -shift)

teks = input("Masukkan teks: ")
shift = int(input("Masukkan jumlah pergeseran (shift): "))

hasil_enkripsi = enkripsi(teks, shift)
hasil_dekripsi = dekripsi(hasil_enkripsi, shift)

print("\nHasil Enkripsi :", hasil_enkripsi)
print("Hasil Dekripsi :", hasil_dekripsi)
