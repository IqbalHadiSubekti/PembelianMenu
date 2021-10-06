from datetime import datetime

print()
print("=====Program Pembelian Makanan dan Minuman=====")
print()

total1 = 0
jenis1 = ""
porsi = 0

total2 = 0
jenis2 = ""
gelas = 0

pilihan = "beli"

while pilihan == "beli":

	def fungsimakanan():
		global total1
		global porsi
		global jenis1
		print("~Menu Makanan~")
		print()
		print("1. Bakso - Rp15000")
		print("2. Seblak - Rp12000")
		print("3. Siomay - Rp10000")
		print("4. Batagor - Rp18000")
		print()

		nomor = int(input("Masukan Pilihan (Berupa Angka): "))
		porsi = int(input("Berapa Porsi (Berupa Angka): "))

		if nomor == 1:
			total1 = porsi * 15000
			print(porsi, " porsi Bakso = Rp", total1)
			jenis1 = ("Bakso")
		elif nomor == 2:
			total1 = porsi * 12000
			print(porsi, " porsi Seblak = Rp", total1)
			jenis1 = ("Seblak")
		elif nomor == 3:
			total1 = porsi * 10000
			print(porsi, " porsi Siomay = Rp", total1)
			jenis1 = ("Siomay")
		elif nomor == 4:
			total1 = porsi * 18000
			print(porsi, " porsi Batagor = Rp", total1)
			jenis1 = ("Batagor")
		else:
			print("Pilihan tidak ada, silahkan masukan")
	fungsimakanan()

	def fungsiminuman():
		global total2
		global jenis2
		global gelas
		print("~Menu Minuman~")
		print("1. Es Teh - Rp2000")
		print("2. Es Jeruk - Rp3500")
		print("3. Es Kopi - Rp4000")
		print("4. Es Coklat - Rp5000")
		print()

		nomor = int(input("Masukan Pilihan (Berupa Angka): "))
		gelas = int(input("Berapa Gelas (Berupa Angka): "))
		
		if nomor == 1:
			total2 = gelas * 2000
			print(gelas, " Es Teh = Rp", total2)
			jenis2 = ("Es Teh")
		elif nomor == 2:
			total2 = gelas * 3500
			print(gelas, " Gelas Es Jeruk = Rp", total2)
			jenis2 = ("Es Jeruk")
		elif nomor == 3:
			total2 = gelas * 4000
			print(gelas, " Gelas Es Kopi = Rp", total2)
			jenis2 = ("Es Kopi")
		elif nomor == 4:
			total2 = gelas * 5000
			print(gelas, " Gelas Es Coklat = Rp", total2)
			jenis2 = ("Es Coklat")
		else:
			print("Pilihan tidak ada, silahkan masukan lagi!!")
			fungsiminuman()

	fungsiminuman()

	totalsemua = 0
	totalsemua = total1 + total2

	print()
	print("Total harus Dibayar: Rp", totalsemua)
	print()
	uang = int(input("Uang Tunai Pembeli: Rp."))
	kembalian = int(uang - totalsemua)
	print("Kembalian :", kembalian)

	print("=======================================")
	print("==========S T R U K   B E L I==========")
	print("=======================================")
	print(" Makanan    : ", porsi, jenis1, "-", total1)
	print(" Minuman    : ", gelas, jenis2, "-", total2)
	print(" Tagihan    : Rp.", totalsemua)
	print(" Uang       : Rp.", uang)
	print(" Kembalian  : Rp.", kembalian)
	print("	Tanggal	   : ",datetime.now())
	print("=======================================")

	beli = str(input("Apakah anda akan membeli lagi? [ya/tidak] : "))

	if beli == "ya":
		pass
	elif beli == "tidak":
		break