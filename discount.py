def discount():
	if add_item=="Y" or add_item=="y":
		buyitem()
		pas=0
		if pas=="0":
			new_amount=0
			new_amount=amount
			amount_received=0
			myName=""
			student=""
			senior=""
			PWD=""
			pas=""
			age=""
			pas=input("\n            Discount Type : ")
			print(" \n Senior Citizen Info")
			myName=input(" NAME:")
			senior=int(input(" AGE: "))
			discount=.20
			id_number=input(" SCID:")
			amount_disSR=int(input(" PRICE VALUE     : "))
			discount=float(discount)*float(amount_disSR)
			print(" Your discount is " +str(discount))
			amount_disSR=int(amount_disSR)-int(discount)
			amount_receiveSR=amount_disSR*new_amount-discount
			print(" AMOUNT RECEIVE DISCOUNTED  :  P ", amount_receiveSR)
			print("           THIS SERVES AS YOUR SALES INVOICE \n")
			print("   WATSONS PERSONAL CARE STORES MANILA PHILPIINES INC \n 211 2/F  The Podium ADB Avenue Ortigas\n Wack-wack Greenhills, City of Mandaluyong \n ")
			print("     For any concerns on our products and services, \n please ask our Store Manager. To replace exchange\n merchandise present this receipt. Subject to standard\n provisions on consumer protection and product\n warranty. ")
		else:
			exit()
			print(" You are not senior citizen "+myName.upper()+" and you are not yet\n qualified for the DSWD Pension because you  still \n have "+str(60-int(senior)) + " years before you can avail the discount.")
		print(exit())
	elif pas=="1":
			print(" PWD Information")
			myName=input(" NAME:")
			PWD=int(input(" AGE: "))
			id_number=input(" PWD ID:")
			print(" You are "+myName.upper()+" with ID number "+id_number+ " and\n you can avail discount.")
			discount=.20
			amount_disSR=int(input(" TRIP FARE      :    "))
			discount=float(discount)*float(amount_disSR)
			print(" Your discount is " +str(discount))
			amount_disSR=int(amount_disSR)-int(discount)
			amount_receiveSR=amount_disSR*tickets-discount
			print(" AMOUNT RECEIVE DISCOUNTED  : P  ", amount_receiveSR)
			new_balanced=float(balanced)-int(amount_disSR)-float(amount_receiveSR)
			print("        \n  YOUR NEW GCASH BALANCE IS : P ", new_balanced,"\n")
			print("           THIS SERVES AS YOUR SALES INVOICE \n")
			print("   WATSONS PERSONAL CARE STORES MANILA PHILPIINES INC \n 211 2/F  The Podium ADB Avenue Ortigas\n Wack-wack Greenhills, City of Mandaluyong \n ")
			print("     For any concerns on our products and services, \n please ask our Store Manager. To replace exchange\n merchandise present this receipt. Subject to standard\n provisions on consumer protection and product\n warranty. ")
			print(exit())
	elif pas=="2":
		print(" Student Info. ")
		myName=input(" NAME:")
		student=int(input(" AGE: "))
		id_number=input(" Student ID:")
		print(" You are "+myName.upper()+" with ID number "+id_number+ " and\n you can avail discount.")
		discount=.20
		amount_disSR=int(input(" TRIP FARE      :    "))
		discount=float(discount)*float(amount_disSR)
		print(" Your discount is " +str(discount))
		amount_disSR=int(amount_disSR)-int(discount)
		amount_receiveSR=amount_disSR*tickets-discount
		print(" AMOUNT RECEIVE DISCOUNTED  : P  ", amount_receiveSR)
		new_balanced=float(balanced)
		int(amount_disSR)-float(amount_receiveSR)
		print("        \n  YOUR NEW GCASH BALANCE IS : P ", new_balanced,"\n")
		print("           THIS SERVES AS YOUR SALES INVOICE \n")
		print("   WATSONS PERSONAL CARE STORES MANILA PHILPIINES INC \n 211 2/F  The Podium ADB Avenue Ortigas\n Wack-wack Greenhills, City of Mandaluyong \n ")
		print("     For any concerns on our products and services, \n please ask our Store Manager. To replace exchange\n merchandise present this receipt. Subject to standard\n provisions on consumer protection and product\n warranty. ")
		print(exit())
	else:
		print("           THIS SERVES AS YOUR SALES INVOICE \n")
		print("   WATSONS PERSONAL CARE STORES MANILA PHILPIINES INC \n 211 2/F  The Podium ADB Avenue Ortigas\n Wack-wack Greenhills, City of Mandaluyong \n ")
		print("     For any concerns on our products and services, \n please ask our Store Manager. To replace exchange\n merchandise present this receipt. Subject to standard\n provisions on consumer protection and product\n warranty.. ")
discount()