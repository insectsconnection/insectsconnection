from pywebio.input import input, FLOAT,select
from pywebio.output import put_text,put_markdown,put_table,put_processbar,set_processbar
from pywebio. session import local
import datetime as dt
import csv
import random
import time

with open('buspos.csv',"w",newline="") as f:
	w=csv.writer(f)
	field=["VEHICLE NO","DATE/TIME","FROM","DISTANCE","DRIVER ID","DRIVER NAME","CONDUCTOR ID","CONDUCTOR NAME","CARD NAME","CARD TYPE","AMOUNT","The balanced in your account is  ", "YOUR NEW GCASH BALANCE","REFERENCE","TICKETS","TRIP FARE"]
	w.writerow(field)
	ans="y"
	while ans=="y":
		vehicle_id=52
		today=dt.datetime.today()
		location=""
		location2=""
		driv_name=" Abner M. Acoledo"
		driv_id="2446"
		cond_name=" Joel J. Drillo"
		cond_id="8919"
		card_name="00046788919"
		card_type="Card/Cash"
		balance=float(20000)
		balanced=0
		new_balanced=0
		sub_total=0
		tickets=0
		amount=0
		price=[23,35,43,65,48,65,78,89,95,100]
		reference_receipt=random.randint(0,10000000000000000)
		customer_service=" 9876553323"
		put_markdown('## Welcome to MONTELLANO BUS TICKETING')
		print(" TIN # : 207-904-409-000")
		print(" Machine:  #")
		print(" Permit :  #")
		print(" Serial :  #")
		print(" ACCDTN # : 053B2333910582015070363")
		print(" FARE/SOUTH")
		print(" PASSENGER - TICKET")
		print(" ERJOHN15-0092286")
		put_text("  VEHICLE NO:     ", vehicle_id)
		put_text("  DATE / TIME   :  ",today)
		print("  DATE / TIME   :  ",today)
		print("  DRIVER ID:     ", driv_id)
		put_text("  DRIVER NAME:    ", driv_name)
		print("  CONDUCTOR ID:", cond_id)
		put_text("  CONDUCTOR NAME:", cond_name)
		put_text("  FARE/SOUTH")
		put_table([['Location','Destination','Price'],['Lawton', 'UN Avenue',20],['UN Avenue','Baclaran' ,25], ['Baclaran','Bacoor',55]])
		
		for j in location:
			if j[0]<=0 or j[0]<=10:
				j=location2-location
				print(price[j])
			else:
				j=location-location2
				print(price[j])
		for k in location2:
			if k[0]>=0 or k[0]<=10:
				j=location2-location
				print(price[k])
			else:
				j=location-location2
				print(price[k])
				
		location=select(" STATION", options=[
 " 0 Lawton Terminal", " 1 Kalaw"," 2 UN Ave", " 3 Quirino Ave", " 4 Buendia", " 5 Baclaran", " 6 Bacoor", " 7 Imus", " 8 Dasma", " 9 Silang"," 10 Mendez Terminal"])
		put_text(f"You chose {location} ticket. Please wait until it is served!")
		put_processbar('bar')
		for i in range(1, 1):
		   	set_processbar('bar', i / 10)
		   	time.sleep(0.05)
		   	put_markdown(f"Here is your {location} ticket! Enjoy!")
		location2=select(" STATION",options=[
" 0 Lawton Terminal", " 1 Kalaw"," 2 UN Ave", " 3 Quirino Ave", " 4 Buendia", " 5 Baclaran", " 6 Bacoor", " 7 Imus", " 8 Dasma", " 9 Silang"," 10 Mendez Terminal"])
		put_text(f"You chose {location} ticket. Please wait until it is served!")
		put_processbar('bar')
		for i in range(1, 1):
		   	set_processbar('bar', i / 10)
		   	time.sleep(0.05)
		   	put_markdown(f"Here is your {location} ticket! Enjoy!")  
		
		
		if balance>=20000:
			balanced=balance-float(amount)
			put_text("   The balanced in your account is  " +str(balance))
		elif balance>0:
			print("  Negative please fund your account.")
		def fare(balance,new_balanced,amount,sub_total):
			print(f"  FROM: {location}")
			print(f"  DISTANCE: {location2}")
			
			tickets=int(input("  NUMBER OF TICKETS:    ",placeholder="Tickets Total"))
			print("  TOTAL NUMBER OF TICKETS:", tickets)
			put_text("  TOTAL NUMBER OF TICKETS:", tickets)
			put_text("  CARD NAME:", card_name)
			print("  CARD NAME:", card_name)
			put_text("  CARD TYPE:",card_type)
			print("  CARD TYPE:",card_type)
			amount=int(input("  AMOUNT: "))
			put_text("  AMOUNT  : ",amount)
			print("  AMOUNT  : ",amount)
			put_text("  TRIP FARE        :    ",amount)
			print("  TRIP FARE        :    ",amount)
			sub_total=int(amount)*int(tickets)
			put_text("  SUB TOTAL        :   ", sub_total)
			print("  TOTAL  AMOUNT      :   ", sub_total)
			new_balanced=float(balance)-float(sub_total)
			
			put_text("        \n  YOUR NEW GCASH BALANCE IS : P", new_balanced)
			put_text("        \n  YOUR CURRENT GCASH BALANCE IS : P", new_balanced)
			
			put_text("  REFERENCE #:  ", reference_receipt)
			put_text("\n  This is not an official receipt")
			put_text("  This ticket is not refundable. Visit our customer service or call our number to ",customer_service,"\n")
			return new_balanced
		fare(20000,new_balanced,amount,sub_total)
	
		w.writerow([vehicle_id,today,location,location2,driv_id,driv_name,cond_id,cond_name,card_name,card_type,amount,balance,new_balanced,reference_receipt,tickets,amount])
	
F=open("buspos.csv","r")
reader=csv.reader(F)
for row in reader:
	print (row)
	F.closed()
	ans=(" Do you want to enter more?")
	new_balanced=balance
	
	
"""	
		if distance>=2 and distance<=2:
			print(a,"lawton to ",b)
		elif distance
"""