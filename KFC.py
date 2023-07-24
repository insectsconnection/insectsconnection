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
Total_Amount=0
item=0
items=0
Items=0
fee=0
a=0
b=0
print("                      MONTELLANO POS\n ")
operated_by=" BACHAO IMUS  CAVITE BUILDING \n                   ALONG BATANGAS ROAD, CITY OF NCR, \n                   THIRD DISTRICT(1264228)"
print(" OPERATED BY    :",operated_by)
print(" BRANCH CODE    : ", 28018)
PIN="MGT"
print(" MANAGER NAME   : "+manager_name)
print(" VAT Reg.TIN #  :  207-904-409-000")
prmt=" FP122021-116-0312000624-64637"
print(" Permit #       :  ", prmt)
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

#items=[" Atrophaneura semperi", " Attacus atlas"," Cethosia biblis", " #3 items", " #4 items", " #5 items", " #6 items", " #7 items", " #8 items", " #9 items"," #10 items"]

items=[" BATWING", " ATLAS MOTH"," RED LACEWING", " COMMON MIME"," PLAIN TIGER"," TAILED JAY"," COMMON JAY"," GREAT EGGFLY"," PAPER KITE"," PINK ROSE"," COMMON LIME"," EMERALD SWALLOWTAIL"," GREAT YELLOW MORMON"," COMMON MORMON"," SCARLET MORMON"," GIANT SILK MOTH","CLIPPER"," GOLDEN BIRDWING"
]
"""
items={1:"BATWING BUTTERFLY", 2:"ATLAS MOTH",3:"RED LACEWING", 4:"COMMON MIME",5:"PLAIN TIGER",6:"TAILED JAY BUTTERFLY",7:"COMMON JAY",8:"GREAT EGGFLY",9:"PAPER KITE",10:"PINK ROSE",11:"COMMON LIME",12:"EMERALD SWALLOWTAIL",13:"GREAT YELLOW MORMON",14:"COMMON MORMON",15:"SCARLET MORMON",16:"GIANT SILK MOTH",17:"CLIPPER",18:"GOLDEN BIRDWING"
 }
 """
#price=[23, 35,43,65,48,64,78,89,71,73,81]
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
price11=34
price12=39
price13=100
price14=85
price15=45
price16=75
price17=85
price18=80
price19=120
print("       \n  PURCHASED ITEMS ")
print(" ----------------------------------")
print(" DESCRIPTION ", "    PRICE AMOUNT")
print(" ----------------------------------")


def ITEM():
	Items=0
	Items=int(input(" How many items?:  "))
	def add_item():
		
		#print(" NUMBER OF ITEMS: ",Items)
		item=input(" INPUT BAR CODE :  ")
		if item=="0":
			print(items[0],"    : ",price0)
			#amount=int(price0)
		elif item=="1":
			print(items[1],"    : ",price1)
			#amount=int(price0)
		elif item=="2":
			print(items[2],"    : ",price2)
		elif item=="3":
			print(items[3],"    : ",price3)
		elif item=="4":
			print(items[4],"    : ",price4)
		elif item=="5":
			print(items[5],"    : ",price5)
		elif item=="6":
			print(items[6],"    : ",price6)
		elif item=="7":
			print(items[7],"    : ",price7)
		elif item=="8":
			print(items[8],"    : ",price8)
		elif item=="9":
			print(items[9],"    : ",price9)
		elif item=="10":
			print(items[10],"    : ",price10)
		else:
			print(" No Item choose: ")
			print(exit())
	add_item()
	
	
			#Computation of the items
			#total_amount=int(item)*int(Items)
			#print(total_amount)
			
	print(" ----------------------------------")
	print(" Reference #    : ", random.randint(0,1000000000000000))
	print(" ********************************")
	sub_total=int(input(" SUBTOTAL       :  "))
	amount_pay=sub_total*int(Items)
	print(" AMOUNT TO PAY  : " , amount_pay)
	cash=int(input(" CASH           :  " ))
			#change=int(cash)-int(total_amount)
	change=int(cash-amount_pay)
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
			print(" PREDICTED PRICE: ",price0)
			total_amount=price0*Items
			print(" AMOUNT         : ", total_amount)
		elif itm=="1":
			print(items[1], "         ")
			print(" PREDICTED PRICE: ",price1)
			total_amount1=price1*Items
			print(" AMOUNT         : ", total_amount1)
		elif itm=="2":
			print(items[2], "         ",)
			print(" PREDICTED PRICE: ",price2)
			total_amount2=price2*Items
			print(" AMOUNT         : ", total_amount2)
		elif itm=="3":
			print(items[3], "         ")
			print(" PREDICTED PRICE: ",price3)
			total_amount3=price3*Items
			print(" AMOUNT         : ", total_amount3)
		if itm=="4":
			print(items[4], "         ")
			print(" PREDICTED PRICE: ",price4)
			total_amount4=price4*Items
			print(" AMOUNT         : ", total_amount4)
		elif itm=="5":
			print(items[5], "         ")
			print(" PREDICTED PRICE: ",price5)
			total_amount5=price5*Items
			print(" AMOUNT         : ", total_amount5)
		if itm=="6":
			print(items[6], "         ")
			print(" PREDICTED PRICE: ",price6)
			total_amount6=price6*Items
			print(" AMOUNT         : ", total_amount6)
		elif itm=="7":
			print(items[7], "         ")
			print(" PREDICTED PRICE: ",price7)
			total_amount7=price7*Items
			print(" AMOUNT         : ", total_amount7)
		if itm=="8":
			print(items[0], "         ")
			print(" PREDICTED PRICE: ",price8)
			total_amount8=price8*Items
			print(" AMOUNT         : ", total_amount8)
		elif itm=="9":
			print(items[9], "         ")
			print(" PREDICTED PRICE: ",price9)
			total_amount9=price9*Items
			print(" AMOUNT         : ", total_amount9)
		elif itm=="10":
			print(items[10], "         ")
			print(" PREDICTED PRICE: ",price10)
			total_amount10=price10*Items
			print(" AMOUNT         : ", total_amount10)
		elif itm=="11":
			print(items[11], "         ")
			print(" PREDICTED PRICE: ",price11)
			total_amount11=price11*Items
			print(" AMOUNT         : ", total_amount11)
		elif itm=="12":
			print(items[12], "         ")
			print(" PREDICTED PRICE: ",price12)
			total_amount12=price12*Items
			print(" AMOUNT         : ", total_amount12)
		elif itm=="13":
			print(items[13], "         ")
			print(" PREDICTED PRICE: ",price13)
			total_amount13=price13*Items
			print(" AMOUNT         : ", total_amount13)
		elif itm=="14":
			print(items[14], "         ")
			print(" PREDICTED PRICE: ",price14)
			total_amount14=price14*Items
			print(" AMOUNT         : ", total_amount14)
		elif itm=="15":
			print(items[15], "         ")
			print(" PREDICTED PRICE: ",price15)
			total_amount15=price15*Items
			print(" AMOUNT         : ", total_amount15)
		elif itm=="16":
			print(items[16], "         ")
			print(" PREDICTED PRICE: ",price16)
			total_amount16=price16*Items
			print(" AMOUNT         : ", total_amount16)
		elif itm=="17":
			print(items[17], "         ")
			print(" PREDICTED PRICE: ",price17)
			total_amount17=price17*Items
			print(" AMOUNT         : ", total_amount17)
		elif itm=="18":
			print(items[18], "         ")
			print(" PREDICTED PRICE: ",price18)
			total_amount18=price18*Items
			print(" AMOUNT         : ", total_amount18)
		elif itm=="":
			print(" Wrong PIN.. Call the", manager_name, "to,", PIN)
			exit()
	def receipt(i):
		print(" ----------------------------------")
		print(" Reference #    : ", random.randint(0,1000000000000000))
		print(" ********************************")
		total_amount=int(input(" SUBTOTAL       :  "))
		total_amount=total_amount*int(Items)
		total_amount1=total_amount1*int(Items)
		total_amount2=total_amount2*int(Items)
		total_amount3=total_amount3*int(Items)
		total_amount4=total_amount4*int(Items)
		total_amount5=total_amount5*int(Items)
		total_amount6=total_amount6*int(Items)
		total_amount7=total_amount7*int(Items)
		total_amount8=total_amount8*int(Items)
		total_amount9=total_amount9*int(Items)
		total_amount10=total_amount10*int(Items)
		total_amount11=total_amount11*int(Items)
		total_amount12=total_amount12*int(Items)
		total_amount13=total_amount13*int(Items)
		total_amount14=total_amount14*int(Items)
		total_amount15=total_amount15*int(Items)
		total_amount16=total_amount16*int(Items)
		total_amount17=total_amount17*int(Items)
		total_amount8=total_amount18*int(Items)
		Total_Amount=total_amount+total_amount1+total_amount2+total_amount3+total_amount4+total_amount5+total_amount6+total_amount7
	receipt(Total_Amount)

#adding items
add_item=""
add_item=input(" Would you like to add items?" "Y/N : ")
if add_item=="Y" or add_item=="y":
	buyer_id=0
	buyer_name=""
	buyer_id=int(input(" Buyer ID       :  "))
	buyer_name=input(" Name           :  ")
else:
	exit()
	print(" AMOUNT TO PAY  : " , amount)
	cash=int(input(" CASH           :  " ))
	#change=int(cash)-int(total_amount)
	change=int(cash-Total_Amount)
	print(" CHANGE         : " , change)
	#card_name=input("CARD NAME:")
	print(" CARD NAME      : ", card_name)
	#card_type=input("CARD TYPE:")
	print(" CARD TYPE      : ", card_type)
	print(" ----------------------------------")
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
			print(" Your discount is " +str(discount))
			amount_disSR=int(amount_disSR)-int(discount)
			amount_receiveSR=amount_disSR*new_amount-discount
			print(" AMOUNT RECEIVE DISCOUNTED  :  P ", amount_receiveSR)
			print("     For any concerns on our products and services, please ask our Store Manager. To replace/exchange merchandise present this receipt. Subject to standard provisions on consumer protection and product warranty.")
		else:
			exit()

add()
print("           THIS SERVES AS YOUR SALES INVOICE \n")
			
	
print("   WATSONS PERSONAL CARE STORES MANILA PHILPIINES INC \n 211 2/F  The Podium ADB Avenue Ortigas\n Wack-wack Greenhills, City of Mandaluyong \n ")
print("     For any concerns on our products and services, please ask our Store Manager. To replace/exchange merchandise present this receipt. Subject to standard provisions on consumer protection and product warranty. ")
buyitem()

#print(" ***********************")

"""	



	








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
	
"""
