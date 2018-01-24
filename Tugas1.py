def array (nama):
	signGirl="aeiutlAEIUTL"
	signBoy="bdoBDO"
	sumBoy=0
	sumGirl=0

	for huruf in nama:
		if huruf == " ":
			break
		else :
			if huruf in signGirl:
				sumGirl+=1
			if huruf in signBoy:
				sumBoy+=1
	
	print("Jenis Kelamin adalah :")
	print("indikasi cowok = ",sumBoy)
	print("indikasi cewek = ",sumGirl)

	if sumBoy > sumGirl:
		print ("Laki Laki")
	elif sumBoy < sumGirl:
		print ("Perempuan")
	else :
		print ("Tidak Diketahui")

nama = "Mochamad Agusta Naofal Hakim"
array(nama)