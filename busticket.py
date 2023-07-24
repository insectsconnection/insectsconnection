
import time
from pywebio.input import input, FLOAT,file_upload
from pywebio.output import put_text,put_markdown,put_table,put_image,put_file
from pywebio. session import local
import datetime as dt
import random

vehicle_id=""
time=""
from_place=""
to_place=""
from_place2=""
to_place2=""
distance=""
amount_receive=0
driv_name=" Abner M. Acoledo"
cond_name=" Joel J. Drillo"
card_name="00046788919"
card_type="Card/Cash"
balanced=float(20000)
reference_receipt=""
customer_service=int(9876553323)
type=0
operate=""
amount=0
fee=0
fees=0
a=0
b=0
print(" MONTELLANO BUS TICKETING")
print(" TIN # : 207-904-409-000")
print(" Machine:  #")
print(" Permit :  #")
print(" Serial :  #")
print(" ACCDTN # : 053B2333910582015070363")
print(" FARE/SOUTH")
print(" PASSENGER - TICKET")

print(" ERJOHN15-0092286")
#today=dt.date.today()
#print(" DATE", today)
time=dt.datetime.now()
print(" ISSUED DATE/TIME :",time)
#time=input("TIME:")
print(" VEHICLE NO :", 28018)
#driv_name=input("DRIV NAME:")
print(" DRIVER NAME : "+driv_name)
#cond_name=input("COND NAME:")

def id(type):
	type=input(" ASSIGNED PERSONNEL ID : ")
	if type=="0":
		print(" CONDUCTOR NAME : ", cond_name)
	
	elif type=="1":
		print(" OPERATOR:", operate)
	else:
		print(" None:")
ID=id(type)
#Open to Fair South
print(" Line1: LAWTON TO MENDEZ")
put_markdown("## Line1: LAWTON TO MENDEZ")
put_text(" Line1: LAWTON TO MENDEZ")

"""
Open to Fair North
print(" Line2: MENDEZ TO LAWTON")
from_place2=input(" km: " )
distance2=input(" km: " )
"""		
#TERMINAL LINE DESTINATION
terminal=[" 0 Lawton Terminal", " 1 Kalaw"," 2 UN Ave", " 3 Quirino Ave", " 4 Buendia", " 5 Baclaran", " 6 Bacoor", " 7 Imus", " 8 Dasma", " 9 Silang"," 10 Mendez Terminal"]
distination=[ " 0 Lawton Terminal"," 1Kalaw","2 UN Ave", "3 Quirino Ave", "4 Buendia", "5 Baclaran", "6 Bacoor", "7 Imus", "8 Dasma", "9 Silang","10 Mendez Terminal"]
terminal2=[ "0 Mendez Terminal"," 1 Silang"," 2 Dasma", " 25 ANABU coastal/Yasaki, Imus", " 4 Bacoor", " 5 Baclaran", " 6 Buendia", " 7 Quirino", " 8 UN Avenue", " 9 National Library Museum", " 10 Lawton Terminal"]
distination2=[ "0 Mendez Terminal","1 Silang","2 Dasma", "3 Imus", "4 Bacoor", " 5 Baclaran", "6 Buendia", "7 Quirino", "8 UN Avenue", "9 National Library Museum", "10 Lawton Terminal"]
fee=["0","25","30","35","40","45","50","61","70","79","90","115","120"]
ter=0
ter2=0


def start():
		ter=int(input(" Kilometer start : " ))
		ter=ter
		if ter==0:
			print(" FROM: ",terminal[0])
			put_text(" FROM: ",terminal[0])
		elif ter>=2 and ter<=4:
			print(" FROM:", terminal[1])
			put_text(" FROM:", terminal[1])
		elif ter>=5 and ter<=9:
			print(" FROM:", terminal[2])
			put_text(" FROM:", terminal[2])
		elif ter>=10 and ter<=14:
			print(" FROM:", terminal[3])
			put_text(" FROM:", terminal[3])
		elif ter>=15 and ter<=19:
			print(" FROM:", terminal[4])
			put_text(" FROM:", terminal[4])
		elif ter>=20 and ter<=24:
			print(" FROM:", terminal[5])
			put_text(" FROM:", terminal[5])
		elif ter>=25 and ter<=29:
			print(" FROM:", terminal[6])
			put_text(" FROM:", terminal[6])
		elif ter>=30 and ter<=39:
			print(" FROM:", terminal[7])
			put_text(" FROM:", terminal[7])
		elif ter>=40 and ter<=49:
			print(" FROM:", terminal[8])
			put_text(" FROM:", terminal[8])
		elif ter>=50 or ter<=59:
			print(" FROM:", terminal[9])
			put_text(" FROM:", terminal[9])
		elif ter>=60 or ter<=70:
			print(" FROM:", terminal[10])
			put_text(" FROM:", terminal[10])
		else:
			print(" FROM:", terminal[11])
			put_text(" FROM:", terminal[11])
start()
def end():
		ter2=int(input(" Kilometer end : " ))
		ter2=ter2
		if ter2==0:
			print(" TO    : ",terminal[0])
			put_text(" TO    : ",terminal[0])
		elif ter2>=2 and ter2<=4:
			print(" TO    :", terminal[1])
			put_text(" TO    :", terminal[1])
		elif ter2>=5 and ter2<=9:
			print(" TO    :", terminal[2])
			put_text(" TO    :", terminal[2])
		elif ter2>=10 and ter2<=14:
			print(" TO    :", terminal[3])
			put_text(" TO    :", terminal[3])
		elif ter2>=15 and ter2<=19:
			print(" TO    :", terminal[4])
			put_text(" FROM:", terminal[4])
		elif ter2>=20 and ter2<=24:
			print(" TO    :", terminal[5])
			put_text(" TO    :", terminal[5])
		elif ter2>=25 and ter2<=29:
			print(" TO    :", terminal[6])
			put_text(" TO    :", terminal[6])
		elif ter2>=30 and ter2<=39:
			print(" TO    :", terminal[7])
			put_text(" TO    :", terminal[7])
		elif ter2>=40 and ter2<=49:
			print(" TO    :", terminal[8])
			put_text(" TO    :", terminal[8])
		elif ter2>=50 or ter2<=59:
			print(" TO    :", terminal[9])
			put_text(" TO    :", terminal[9])
		elif ter2>=60 or ter2<=70:
			print(" TO    :", terminal[10])
			put_text(" TO    :", terminal[10])
		else:
			print(" TO    :", terminal[11])
			put_text(" TO    :", terminal[11])
end()


"""
def km(distance):
		if distance>="0" and distance<="3":
			print(" TO  :", distination[0])
		elif distance>="4" and distance<="6":
			print(" TO  : ", distination[1])
		elif distance>="7" and distance<="9":
			print(" TO  : ", distination[2])
		elif distance>="10" and distance<="12":
			print(" TO  : ", distination[3])
		elif distance>="13" and distance<="15":
			print(" TO  : ", distination[4])
		elif distance>="16" and distance<="18":
			print(" TO  : ", distination[5])
		elif distance=="19":
			print(" TO  : ", distination[6])
		elif distance>="22" and distance<="23":
			print(" TO  : ", distination[7])
		elif distance>="28" and distance<="31":
			print(" TO  : ", distination[8])
		elif distance>="32" and distance<="35":
			print(" TO  : ", distination[9])
		elif distance>="36" and distance<="100":
			print(" TO  : ", distination[10])
		else:
			print(" Line : 0  Mendez to Lawton Terminal")
km(distance)

"""

# DASMA
"""
def line3(term):
		if from_place2=="0":
			print(" FROM: ",terminal2[0])
		elif from_place2=="1":
			print(" FROM:", terminal2[1])
		elif from_place2=="2":
			print(" FROM:", terminal2[2])
		elif from_place2=="3":
			print(" FROM:", terminal2[3])
		elif from_place2=="4":
			print(" FROM:", terminal2[4])
		elif from_place2=="5":
			print(" FROM:", terminal2[5])
		elif from_place2=="6":
			print(" FROM:", terminal2[6])
		elif from_place2=="7":
			print(" FROM:", terminal2[7])
		elif from_place2=="8":
			print(" FROM:", terminal2[8])
		elif from_place2=="9":
			print(" FROM:", terminal2[9])
		elif from_place2=="10":
			print(" FROM:", terminal2[10])
		else:
			print(" Line : 0 Lawton Terminal to Mendez")
			
line3=line3(float(from_place2))

def line4(dis):
		if distance2=="1":
			print(" TO  : ",distination2[1])
		elif distance2=="2":
			print(" TO  : ", distination2[2])
		elif distance2=="3":
			print(" TO  : ", distination2[3])
		elif distance2=="4":
			print(" TO  : ", distination2[4])
		elif distance2=="5":
			print(" TO  : ", distination2[5])
		elif distance2=="6":
			print(" TO  : ", distination2[6])
		elif distance=="7":
			print(" TO  : ", distination2[7])
		elif distance2=="8":
			print(" TO  : ", distination2[8])
		elif distance2=="9":
			print(" TO  : ", distination2[9])
		elif distance2=="10":
			print(" TO  : ", distination2[10])
		else:
			print(" Line : 0  Mendez to Lawton Terminal")
line4=line4(float(distance2))
"""
print(" PASSENGER BUS TICKET NUMBER: " , random.randint(0,10000000000000000))
put_text(" PASSENGER BUS TICKET NUMBER: " , random.randint(0,10000000000000000))

print(" -------------------------------------------------")
put_text(" -------------------------------------------------")
print("         PURCHASED TICKET ")
put_text("         PURCHASED TICKET ")
print(" -------------------------------------------------")
put_text(" -------------------------------------------------")
print(" DESCRIPTION ", "      AMOUNT")
put_text(" DESCRIPTION ", "      AMOUNT")
print(" -------------------------------------------------")
put_text(" -------------------------------------------------")



"""
def p(fee):
	if a==1:
		print(" Passenger Fare   :   ", fee[1])
	elif a==2:
		print(" Passenger Fare   :   ", fee[2])
	elif a==3:
		print(" Passenger Fare   :   ", fee[3])
	elif a==4:
		print(" Passenger Fare   :   ", fee[4])
	elif a==5:
		print(" Passenger Fare   :   ", fee[5])
	elif a==6:
		print(" Passenger Fare   :   ", fee[6])
	elif a==7:
		print(" Passenger Fare   :   ", fee[7])
	elif a==8:
		print(" Passenger Fare   :   ", fee[8])
	elif a==9:
		print(" Passenger Fare   :   ", fee[9])
	elif a==10:
		print(" Passenger Fare   :   ", fee[10])
	else:
		print(" Passenger Fare List :   ", fee)
		print(exit())
fee1=p(fee)
"""
tickets=0
km=int(ter2)-int(ter)


put_text(" Total kilometers :   ",a)


print(" Total kilometers :   ",km)
def fare(fees):
	
	tickets=int(input(" NUMBER OF TICKETS:    "))
	put_text(" Price list : ", fee)
	if a>=0 and a<=13:
		
		print(" TRIP FARE        :   ", fee[tickets])
		put_text(" TRIP FARE        :   ", fee[tickets])
		put_text(" NUMBER OF TICKETS:    ", tickets)
		amount=int(input(" TICKET FARE        :    "))
		amount_receive=amount*tickets
		new_balanced=float(balanced)-float(amount)*int(tickets)
		print(" --------------------------------------------")
		print(" AMOUNT  TO PAY   :  P",
		amount_receive,"\n")
		put_text(" AMOUNT TO PAY    :  P",amount_receive,"\n")
		print(" AMOUNT RECEIVE   :  P", amount_receive)
		put_text(" AMOUNT RECEIVE   :  P", amount_receive)
		print(" --------------------------------------------")
		put_text(" --------------------------------------------")
		#card_name=input("CARD NAME:")
		print(" CARD NAME:",card_name)
		put_text(" CARD NAME:",card_name)
		#card_type=input("CARD TYPE:")
		print(" CARD TYPE: "+card_type)
		put_text(" CARD TYPE: "+card_type)
		print(" CARD TYPE: "+card_type)
		print("        \n  YOUR NEW GCASH BALANCE IS : P", new_balanced)
		put_text("        \n  YOUR NEW GCASH BALANCE IS : P", new_balanced)
	else:
		print("   Number only   ")
		put_text("   Number only   ")
		print(exit())
Fare=fare(fees)

myName=""
student=""
senior=""
PWD=""
pas=""
age=""
disc=0
#pass=["student","senior"]

if pas=="SR":
	disc=input("\n            Discount Type : ")
	discount_fare=fare(amount)
	print(" \n Senior Citizen Info")
	myName=input(" NAME:")
	senior=int(input(" AGE: "))
	if senior>=60:
		print(" You are a senior citizen "+myName.upper()+ " and qualified for DSWD\n pension "+str(int(senior)-60)+ " years ago.")
		discount=.20
		id_number=input(" SCID:")
		amount_disSR=int(input(" TRIP FARE      :    "))
		discount=float(discount)*float(amount_disSR)
		print(" Your discount is " +str(discount))
		amount_disSR=int(amount_disSR)-int(discount)
		amount_receiveSR=amount_disSR*tickets-discount
		print(" AMOUNT RECEIVE DISCOUNTED  :  P ", amount_receiveSR)
		new_balanced=float(balanced)-int(amount_disSR)-float(amount_receiveSR)
		print("        \n  YOUR NEW GCASH BALANCE IS : P", new_balanced,"\n")
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
		print(" You are not senior citizen "+myName.upper()+" and you are not yet\n qualified for the DSWD Pension because you  still \n have "+str(60-int(senior)) + " years before you can avail the discount.")
		print(exit())
elif pas=="PWD":
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
	
elif pas=="STD":
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
	

