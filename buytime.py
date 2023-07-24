import datetime as dt
import csv
import random
import time
from pywebio.input import input, FLOAT,file_upload
from pywebio.output import put_text,put_markdown,put_table,put_image,put_file
from pywebio. session import local

with open('buytimePos.csv',"w") as f:
	w=csv.writer(f)
	field=["DATE","BAR CODE","REFERENCE NO","ITEMS","SUBTOTAL","AMOUNT TO PAY","CASH","CHANGE","CARD TYPE","CARD NAME","CHANGE"]

	card_num="00046788919"
	card_type="Card/Cash"
	balanced=float(20000)
	sub_total=0
	amount=0
	cash=0
	amount_pay=0
	change=0
	qty=0
	today = dt.date.today()
	ref_number=random.randint(0,1000000000000000)
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
	items=[" BATWING", " ATLAS MOTH"," RED LACEWING", " COMMON MIME"," PLAIN TIGER"," TAILED JAY"," COMMON JAY"," GREAT EGGFLY"," PAPER KITE"," PINK ROSE"," COMMON LIME"," EMERALD SWALLOWTAIL"," GREAT YELLOW MORMON"," COMMON MORMON"," SCARLET MORMON"," GIANT SILK MOTH","CLIPPER"," GOLDEN BIRDWING"]
	put_markdown('## PURCHASED ITEMS ',today)
	put_text(" -------------------------------------------------------")
	put_text(" DESCRIPTION ", "    PRICE AMOUNT")
	put_text(" --------------------------------------------------------")
	put_markdown('### Upload Image')
	put_image("# Choose file")
	img=file_upload("Select an image",  accept="image/*")
	
	w.writerow([today,img,qty,ref_number,sub_total,items,amount,cash,card_type,card_num,amount_pay,cash,change])
	w.writerow(field)

def ITEM():
	
	qty=0
	qty=int(input(" How many items?:  "))
	def add_item():
		
		#print(" NUMBER OF ITEMS: ",Items)
		item=input(" INPUT BAR CODE :  ")
		
		if item=="0":
			put_text(items[0],"    : ",price0)
			#amount=int(price0)
		elif item=="1":
			put_text(items[1],"    : ",price1)
			#amount=int(price0)
		elif item=="2":
			put_text(items[2],"    : ",price2)
		elif item=="3":
			put_text(items[3],"    : ",price3)
		elif item=="4":
			put_text(items[4],"    : ",price4)
		elif item=="5":
			put_text(items[5],"    : ",price5)
		elif item=="6":
			put_text(items[6],"    : ",price6)
		elif item=="7":
			put_text(items[7],"    : ",price7)
		elif item=="8":
			put_text(items[8],"    : ",price8)
		elif item=="9":
			put_text(items[9],"    : ",price9)
		elif item=="10":
			put_text(items[10],"    : ",price10)
		elif item=="11":
			put_text(items[11],"    : ",price11)
			#amount=int(price0)
		elif item=="12":
			put_text(items[12],"    : ",price12)
		elif item=="13":
			put_text(items[13],"    : ",price13)
		elif item=="14":
			put_text(items[14],"    : ",price14)
		elif item=="15":
			put_text(items[15],"    : ",price15)
		elif item=="16":
			put_text(items[16],"    : ",price16)
		elif item=="17":
			put_text(items[7],"    : ",price17)
		elif item=="18":
			put_text(items[18],"    : ",price18)
		else:
			print(" No Item choose: ")
			print(exit())
	add_item()
	
	
			#Computation of the items
			#total_amount=int(item)*int(Items)
			#print(total_amount)
			
	put_text(" ----------------------------------")
	put_text(" Reference #    : ", ref_number)
	put_text(" ********************************")
	sub_total=int(input(" SUBTOTAL       :  "))
	amount_pay=sub_total*int(qty)
	put_text("QUANTITY        :  ", qty)
	put_text(" AMOUNT TO PAY  : " , amount_pay)
	cash=int(input(" CASH           : " ))
	#change=int(cash)-int(total_amount)
	put_text(" CASH                : ", cash)
	change=int(cash-amount_pay)
	put_text(" CHANGE           : " , change)
			#card_name=input("CARD NAME:")
	put_text(" CARD NAME    : ", card_num)
			#card_type=input("CARD TYPE:")
	put_text(" CARD TYPE      : ", card_type)
	put_text(" ----------------------------------")
		
ITEM()
"""
ans="y"
while ans=="y":
	ans=(" Do you want to enter more?")
	F=open("buytimePos.csv","r")
	reader=csv.reader(F)
for row in reader:
	print (row)
F.closed()
"""
"""
items={1:"BATWING BUTTERFLY", 2:"ATLAS MOTH",3:"RED LACEWING", 4:"COMMON MIME",5:"PLAIN TIGER",6:"TAILED JAY BUTTERFLY",7:"COMMON JAY",8:"GREAT EGGFLY",9:"PAPER KITE",10:"PINK ROSE",11:"COMMON LIME",12:"EMERALD SWALLOWTAIL",13:"GREAT YELLOW MORMON",14:"COMMON MORMON",15:"SCARLET MORMON",16:"GIANT SILK MOTH",17:"CLIPPER",18:"GOLDEN BIRDWING"
 }
 """
#price=[23, 35,43,65,48,64,78,89,71,73,81]
