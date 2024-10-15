# Definisikan kelas Calculator
class Calculator:
    # Metode konstruktor (__init__) untuk menginisialisasi objek dengan dua angka
    def __init__(self, num1, num2):
        self.num1 = num1  # Inisialisasi angka pertama
        self.num2 = num2  # Inisialisasi angka kedua

    # Metode untuk menambah dua angka
    def add(self):
        return self.num1 + self.num2  # Mengembalikan hasil penjumlahan

    # Metode untuk mengurangkan dua angka
    def subtract(self):
        return self.num1 - self.num2  # Mengembalikan hasil pengurangan

    # Metode untuk mengalikan dua angka
    def multiply(self):
        return self.num1 * self.num2  # Mengembalikan hasil perkalian

    # Metode untuk membagi dua angka
    def divide(self):
        if self.num2 == 0:  # Cek apakah angka kedua adalah nol untuk menghindari pembagian dengan nol
            return "Error! Division by zero."  # Mengembalikan pesan error jika pembagian dengan nol
        return self.num1 / self.num2  # Mengembalikan hasil pembagian jika tidak nol

# Fungsi utama untuk menjalankan program
def main():
    # Minta pengguna untuk memasukkan angka pertama dan kedua
    num1 = float(input("Masukkan angka pertama: "))  # Input angka pertama dari pengguna
    num2 = float(input("Masukkan angka kedua: "))    # Input angka kedua dari pengguna

    # Buat objek Calculator dengan dua angka yang diinput oleh pengguna
    calc = Calculator(num1, num2)

    # Menampilkan menu operasi yang bisa dipilih pengguna
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    
    # Minta pengguna untuk memilih operasi yang diinginkan
    choice = input("Masukkan pilihan (1/2/3/4): ")

    # Menjalankan metode yang sesuai berdasarkan pilihan pengguna
    if choice == '1':
        print(f"Hasil: {calc.add()}")  # Jika pengguna memilih 1, lakukan penjumlahan
    elif choice == '2':
        print(f"Hasil: {calc.subtract()}")  # Jika pengguna memilih 2, lakukan pengurangan
    elif choice == '3':
        print(f"Hasil: {calc.multiply()}")  # Jika pengguna memilih 3, lakukan perkalian
    elif choice == '4':
        print(f"Hasil: {calc.divide()}")  # Jika pengguna memilih 4, lakukan pembagian
    else:
        print("Pilihan tidak valid!")  # Jika input pengguna tidak sesuai dengan pilihan yang ada

# Memastikan bahwa program berjalan ketika file ini dieksekusi
if __name__ == "__main__":
    main()  # Panggil fungsi main untuk memulai program
