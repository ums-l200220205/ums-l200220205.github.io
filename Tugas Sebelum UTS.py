class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.spp_dibayar = False
        self.kelas_terdaftar = None
        self.nilai_tugas = 0
        self.nilai_uts = 0
        self.nilai_uas = 0

    def bayar_spp(self):
        print(f"{self.nama} sedang membayar SPP...")
        self.spp_dibayar = True
        print("SPP berhasil dibayar!\n")

    def daftar_kelas(self, kelas):
        if self.spp_dibayar:
            self.kelas_terdaftar = kelas
            print(f"{self.nama} berhasil mendaftar ke kelas {self.kelas_terdaftar}.\n")
        else:
            print("Gagal mendaftar kelas! Anda harus membayar SPP terlebih dahulu.\n")

    def ikuti_perkuliahan(self):
        if self.kelas_terdaftar:
            print(f"{self.nama} mengikuti perkuliahan di kelas {self.kelas_terdaftar}.")
            print("Mengerjakan tugas, memahami materi, dan aktif di kelas.\n")
        else:
            print("Gagal mengikuti perkuliahan! Anda belum terdaftar di kelas mana pun.\n")

    def kerjakan_uts(self, nilai):
        print(f"{self.nama} mengerjakan Ujian Tengah Semester (UTS)...")
        self.nilai_uts = nilai
        print(f"Nilai UTS: {self.nilai_uts}\n")

    def kerjakan_uas(self, nilai):
        print(f"{self.nama} mengerjakan Ujian Akhir Semester (UAS)...")
        self.nilai_uas = nilai
        print(f"Nilai UAS: {self.nilai_uas}\n")

    def hitung_nilai_akhir(self, nilai_tugas):
        self.nilai_tugas = nilai_tugas
        print(f"{self.nama} mendapatkan nilai tugas: {self.nilai_tugas}.")
        nilai_akhir = (self.nilai_tugas * 0.3) + (self.nilai_uts * 0.3) + (self.nilai_uas * 0.4)
        print(f"Nilai akhir: {nilai_akhir:.2f}")
        if nilai_akhir >= 80:
            print("Selamat! Anda lulus mata kuliah dengan predikat Baik.\n")
        else:
            print("Anda belum lulus mata kuliah ini. Tetap semangat!\n")


# Simulasi proses kuliah
def simulasi_kuliah():
    print("=== Simulasi Proses Kuliah di Informatika ===\n")

    # Membuat objek Mahasiswa
    mahasiswa = Mahasiswa("Andi", "L200220214")

    # Proses perkuliahan
    mahasiswa.bayar_spp()
    mahasiswa.daftar_kelas("Algoritma dan Pemrograman")
    mahasiswa.ikuti_perkuliahan()
    mahasiswa.kerjakan_uts(88)
    mahasiswa.kerjakan_uas(90)
    mahasiswa.hitung_nilai_akhir(85)

    print("=== Simulasi Selesai ===")

# Panggil simulasi
if __name__ == "__main__":
    simulasi_kuliah()
