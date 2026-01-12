# ===== MODEL =====
class Mahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def nilai_akhir(self):
        return (self.tugas * 0.3) + (self.uts * 0.3) + (self.uas * 0.4)


# ===== CONTROLLER =====
class MahasiswaController:
    def proses(self, nama, nim, tugas, uts, uas):
        mhs = Mahasiswa(nama, nim, tugas, uts, uas)

        print("\n=== DATA MAHASISWA ===")
        print("Nama        :", mhs.nama)
        print("NIM         :", mhs.nim)
        print("Nilai Tugas :", mhs.tugas)
        print("Nilai UTS   :", mhs.uts)
        print("Nilai UAS   :", mhs.uas)
        print("Nilai Akhir :", mhs.nilai_akhir())


# ===== VIEW =====
class MenuView:
    def tampilkan_menu(self):
        print("INPUT DATA MAHASISWA")

        nama = input("Nama  : ")
        nim = input("NIM   : ")

        try:
            tugas = float(input("Nilai Tugas : "))
            uts = float(input("Nilai UTS   : "))
            uas = float(input("Nilai UAS   : "))
        except ValueError:
            print("Input nilai harus angka!")
            return

        controller = MahasiswaController()
        controller.proses(nama, nim, tugas, uts, uas)


# ===== MAIN =====
if __name__ == "__main__":
    menu = MenuView()
    menu.tampilkan_menu()