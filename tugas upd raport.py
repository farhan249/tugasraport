print ("*****************************")
nis = int (input("Masukan Nis : "))
nama = str (input("Masukan Nama :"))
JK = str (input("Jenis Kelamin : "))
rombel = str (input("Masukan Rombel : "))
rayon = str (input("masukan rayon : "))
nilaiindo = int (input("Masukan Nilai Bahasa Indonesia : "))
nilaimtk = int (input("Masukan Nilai Matematika : "))
nilaiing = int (input("Masukan Bahasa Inggris : "))
print ("******************************")
print("SMK WIKRAMA BOGOR")
print("------- DATA DIRI -------")
print("NIS           : ", nis)
print("Nama          :", nama)
print("Jenis Kelamain:", JK)
print("Rombel        :", rombel)
print("Rayon         :", rayon)
print("------- NILAI -------")
print("B.Indonesis   :", nilaiindo)
print("Matematika    :", nilaimtk)
print("B.Inggris     :", nilaiing)
rata = (nilaiindo + nilaimtk + nilaiing) /3
print("Nilai Rata-rata:", rata)
ket = str
if rata >= 75:
    ket = "Lulus"
else:
    ket = "Tidak Lulus"
print ("Kriteria kelulusan :", ket)
