import datetime
import csv

vehicle_id=""
date=""
time=""
from_place=""
to_place=""
distance=""
driv_id=""
driv_name=""
cond_id=""
cond_name=""
card_name=""
card_type=""
balance=float(20000)
newbalanced=""
reference_receipt=""
customer_service=int(9876553323)

print("  MONTELLANO BUS TICKETING")
print("  FARE/SOUTH")

vehicle_id=int(input("  VEHICLE NO:"))
date=input("  DATE:")
time=input("  TIME:")
from_place=input("  FROM:")
distance=input("  DISTANCE:")
driv_id=input("  DRIVER ID:")
driv_name=input("  DRIVER NAME:")
cond_id=input("  CONDONDUCTOR ID:")
cond_name=input("  CONDONDUCTOR NAME:")
card_name=input("  CARD NAME:")
card_type=input("  CARD TYPE:")
for i in range(1,2):
	#balance=20000
	amount=float(input("  Enter amount: "))
	if balance>=20000:
		balanced=balance-float(amount)
		print("  The balanced in your account is  " +str(balance))
		
		if balance>0:
			print("  Negative please fund your account.")
		else:
			exit()
	elif balance<=0:
		def fare():
			print("  RECEIPT\n")
			print("  VEHICLE ID:"+str(vehicle_id))
			print("  DATE:"+date)
			print("  TIME:"+time)
			print("  FROM:"+from_place)
			print("  DISTANCE:"+distance)
			print("DRIVER ID:"+driv_id)
			print("DRIVER NAME:"+driv_name)
			print("CONDUCTOR ID:"+cond_id)
			print("CONDUCTOR NAME:"+cond_name)
			print("CARD NAME:"+card_name)
			print("CARD TYPE:"+card_type)
		fare=fare()
		print(fare)
		amount=int(input("AMOUNT: "))
		balanced=balance-float(amount)
		print("BALANCE:", balanced)
		print("\nThis is not an official receipt")
		print("This ticket is not refundable")
		print(customer_service,"\n")
	else:
		def fare1():
			print("RECEIPT\n")
			print("VEHICLE ID:"+str(vehicle_id))
			print("DATE:"+date)
			print("TIME:"+time)
			print("FROM:"+from_place)
			print("DISTANCE:"+distance)
			print("DRIVER ID:"+driv_id)
			print("DRIVER NAME:"+driv_name)
			print("COND ID:"+cond_id)
			print("COND NAME:"+cond_name)
			print("CARD NAME:"+card_name)
			print("CARD TYPE:"+card_type)
		fare1()
		fare1=fare1()
		print(fare1)
		print("BALANCE:", new_balanced)
		print("\nThis is not an official receipt")
		print("This ticket is not refundable\n")
		print(customer_service,"\n")
		i=i
newbalanced=balance-float(amount)
print(newbalanced)
		