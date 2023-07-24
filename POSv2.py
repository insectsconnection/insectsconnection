import datetime as dt
import random

branch_id=""
time=""
subtotal=0
cash=0
change=0
distance=""
manager_name=" Abner M. Montellano"
casher_name=" Janelly J. Gona"
card_name="00046788919"
card_type="Card/Cash"
balanced=float(20000)
reference_receipt=""
customer_service=int(9876553323)
type=0
amount=0
total_amount=0
item=0
Items=0
fee=0
a=0
b=0
print("              MONTELLANO POS\n ")
operated_by=" BACHAO IMUS  CAVITE BUILDING \n                   ALONG BATANGAS ROAD, CITY OF NCR, \n                   THIRD DISTRICT(1264228)"
print(" OPERATED BY    :",operated_by)
print(" BRANCH CODE    : ", 28018)
print(" MANAGER NAME   : "+manager_name)
print(" VAT Reg.TIN #  :  207-904-409-000")

print(" Permit #       :  ")
print(" Serial #       :  53R0585121")
print(" MIN #          :  ")
print(" ACCDTN #       :  053B2333910582015070363")

print(" BUYER - RECEIPT")
#today=dt.date.today()
#print(" DATE", today)
time=dt.datetime.now()
print(" ISSUED DATE/TIME :",time)

def id(tp):
	type=input(" PERSONNEL ID   :  ")
	if type=="0":
		print(" CASHER NAME    :", casher_name)
	
	elif type=="1":
		print(" ASST. MANAGER NAME :", manager_name)
	else:
		print(" None:")
ID=id(type)
# Items 

#items=[" #0 items", " #1 items"," #2 items", " #3 items", " #4 items", " #5 items", " #6 items", " #7 items", " #8 items", " #9 items"," #10 items"]
items=(
        (1,"Atrophaneura semperi"),
        (2,"Attacus atlas"),
        (3,"Cethosia biblis"),
        (4,"Chilasa clytia"),
        (5,"Danaus chrysippus"),
        (6,"Graphium agamemnon"),
        (7,"Graphium doson"),
        (8,"Hypolimnas bolina"),
        (9,"Idea leuconoe"), 
        (10,"Pachliopta kotzebuea"),
        (11,"Papilio demoleus"),
        (13,"Papilio palinurus"),
        (12,"Papilio lowi"),
        (14,"Papilio polytes"),
        (15,"Papilio rumanzovia"),
        (16,"Samia luzonica"),
        (17,"Parthenos sylvia"),
        (18,"Troides rhadamantus")
)

price=[23, 35,43,65,48,64,78,89,71,73,81]
price0=23
price1=35
price2=43
price3=65
price4=48
price5=64
price6=78
price7=89
price8=71
price9=73
price10=81
print("       \n  PURCHASED ITEMS ")
print(" ----------------------------------")
print(" DESCRIPTION ", "    AMOUNT")
print(" ----------------------------------")
"""
def ITEM():
	def add_item():
		
		Items=int(input(" How many items?:  "))
		#print(" NUMBER OF ITEMS: ",Items)
		item=int(input(" INPUT BAR CODE :  "))
		if item==0:
			print(items[0], "        ", price0)
			print(" TOTAL AMOUNT   : ",price0)
		elif item==1:
			print(items[1],"        ",price1)
			print(" TOTAL AMOUNT    : ",price1)
		elif item==2:
			print(items[2],"        ",price2)
			print( " TOTAL AMOUNT   : ", price2)
		elif item==3:
			print(items[3],"        ",price3)
			print( " TOTAL AMOUNT   : ", price3)
		elif item==4:
			print(items[4],"        ",price4)
			print(" TOTAL AMOUNT   : ",  price4)
		elif item==5:
			print(items[5],"        ",price5)
			print( " TOTAL AMOUNT   : ", price5)
		elif item==6:
			print(items[6],"        ",price6)
			print( " TOTAL AMOUNT   : ", price6)
		elif item==7:
			print(items[7],"        ",price7)
			print( " TOTAL AMOUNT   : ", price7)
		elif item==8:
			print(items[8],"        ",price8)
			print( " TOTAL AMOUNT   : ", price8)
		elif item==9:
			print(items[9],"        ",price9)
			print( " TOTAL AMOUNT   : ", price9)
		elif item==10:
			print(items[10],"         ",price10)
			print( " TOTAL AMOUNT   : ", price10)
		else:
			print(" No Item choose: ")
			print(exit())
			
	add_item()
	
			#Computation of the items
	#total_amount=int(item)*int(Items)
	#print(total_amount)
	#subtotal=total_amount
	print(" ----------------------------------")
	print(" Reference #    : ", random.randint(0,1000000000000000))
	print(" ********************************")
	amount=int(input(" SUBTOTAL       :  "))
	amount=int(item)*int(Items)
	print(" AMOUNT TO PAY  : " , amount)
	cash=int(input(" CASH           :  " ))
			#change=int(cash)-int(total_amount)
	change=int(cash-amount)
	print(" CHANGE         : " , change)
			#card_name=input("CARD NAME:")
	print(" CARD NAME      : ", card_name)
			#card_type=input("CARD TYPE:")
	print(" CARD TYPE      : ", card_type)
	print(" ----------------------------------")
ITEM()
"""

#with iteration
def buyitem():
	for x in items:
		Items=0
		Items=int(input(" How many items?:  "))
		itm=input(" Enter the code :  ")
		if itm=="0":
			print(items[0], "         ")
			print(" PRICE          : ",price0)
		elif itm=="1":
			print(items[1], "         ")
			print(" PRICE          : ",price1)
		elif itm=="2":
			print(items[2], "         ",)
			print(" PRICE          : ",price2)
		elif itm=="3":
			print(items[3], "         ")
			print(" PRICE          : ",price3)
		if itm=="4":
			print(items[4], "         ")
			print(" PRICE          : ",price4)
		elif itm=="5":
			print(items[5], "         ")
			print(" PRICE          : ",price5)
		if itm=="6":
			print(items[6], "         ")
			print(" PRICE          : ",price6)
		elif itm=="7":
			print(items[7], "         ")
			print(" PRICE          : ",price7)
		if itm=="8":
			print(items[0], "         ")
			print(" PRICE          : ",price8)
		elif itm=="9":
			print(items[9], "         ")
			print(" PRICE          : ",price9)
		elif itm=="10":
			print(items[10], "         ")
			print(" PRICE          : ",price10)
			
		elif itm=="":
			print(" Wrong PIN.. Call the manager to ")
			exit()
			def receipt():
				print(" ----------------------------------")
				print(" Reference #    : ", random.randint(0,1000000000000000))
				print(" ********************************")
				amount=int(input(" SUBTOTAL       :  "))
				amount=amount*int(Items)
				print(" AMOUNT TO PAY  : " , amount)
				cash=int(input(" CASH           :  " ))
				#change=int(cash)-int(total_amount)
				change=int(cash-amount)
				print(" CHANGE         : " , change)
				#card_name=input("CARD NAME:")
				print(" CARD NAME      : ", card_name)
				#card_type=input("CARD TYPE:")
				print(" CARD TYPE      : ", card_type)
				print(" ----------------------------------")
				add_item=input(" Would you like to add items?" "Y/N : ")
				#print(" ***********************")	
				def add():
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
							#print(" Your discount is " ,str(discount))
			amount_disSR=int(amount_disSR)-int(discount)
			            amount_receiveSR=amount_disSR*new_amount-discount
			              print(" AMOUNT RECEIVE DISCOUNTED  :  P ", amount_receiveSR)
		else:
			exit()
			add()
	receipt()
	
buyitem()


	
	
	




	








"""	
	else:
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
	print("\n This is not an official receipt. ")
	print(" This ticket is not refundable. ")
	print(" You can call our customer service. \n Telephone number: ",customer_service,"\n")
	txt="NOTICE\n"
	new_notice=txt.center(60)
	print(new_notice)
	print("     Montellano Land Transport Bus Co Inc. assumes no\n responsibility for loss or damage of effects,luggage\n or belongings carried by passengers unless these are  \n declared and shown to, and a list thereof is given    \n and freight charges are paid thereon to the shipping \n clerk or conductor , and passenger complies with the\n instructions of the shipping clerk or conductor \n relative to their care and safekeeping.\n")
	text2="THE MANAGEMENT"
	new_tm=text2.center(60)
	print(new_tm)
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
	new_balanced=float(balanced)-int(amount_disSR)-float(amount_receiveSR)
	print("        \n  YOUR NEW GCASH BALANCE IS : P ", new_balanced,"\n")
	print("\n This is not an official receipt. ")
	print(" This ticket is not refundable. ")
	print(" You can call our customer service. \n Telephone number: ",customer_service,"\n")
	txt="NOTICE\n"
	new_notice=txt.center(60)
	print(new_notice)
	print("     Montellano Land Transport Bus Co Inc. assumes no\n responsibility for loss or damage of effects,luggage\n or belongings carried by passengers unless these are  \n declared and shown to, and a list thereof is given    \n and freight charges are paid thereon to the shipping \n clerk or conductor , and passenger complies with the\n instructions of the shipping clerk or conductor \n relative to their care and safekeeping.\n")
	text2="THE MANAGEMENT"
	new_tm=text2.center(60)
	print(new_tm)
	print(exit())
else:
	print("\n This is not an official receipt. ")
	print(" This ticket is not refundable. ")
	print(" You can call our customer service. \n Telephone number: ",customer_service,"\n")
	txt="NOTICE\n"
	new_notice=txt.center(60)
	print(new_notice)
	print("     Montellano Land Transport Bus Co Inc. assumes no\n responsibility for loss or damage of effects,luggage\n or belongings carried by passengers unless these are  \n declared and shown to, and a list thereof is given    \n and freight charges are paid thereon to the shipping \n clerk or conductor , and passenger complies with the\n instructions of the shipping clerk or conductor \n relative to their care and safekeeping.\n")
	text2="THE MANAGEMENT"
	new_tm=text2.center(60)
	print(new_tm)
	print("Not this time",exit())
"""
