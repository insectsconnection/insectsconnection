import datetime as dt
import csv
import random
import time
from pywebio.input import input, FLOAT,file_upload
from pywebio.output import put_text,put_markdown,put_table,put_image,put_file
from pywebio. session import local
from PIL import Image
from colorama import Fore
#import pandas as pd


with open('buyItemPos.csv',"a", newline="") as f:
	w=csv.writer(f)
	field=['Date','OR','Image','Quantity', 'Classification Code','Predicted Butterfly', 'Predicted Percent','PREDICTED PRICE','AMOUNT','SUBTOTAL']
	w.writerow(field)
	ans="y"
	while ans=="y":
		card_num=random.randint(0,100000)
		card_type="Card/Cash"
		balanced=float(20000)
		today = dt.datetime.today()#.strftime('%A %B %d, %Y')
		qty=0
		sub_total=0
		total_amount=[]
		itm=0
		img=""
		percent=""
		OR=0
		price=[23,35,43,65,48,65,78,89,71,73,81,34,39,100,85,45,75,80,120]
		items={1:" BATWING",2: " ATLAS MOTH",3:" RED LACEWING", 4:" COMMON MIME",5:" PLAIN TIGER",6:" TAILED JAY",7:" COMMON JAY",8:" GREAT EGGFLY",9:" PAPER KITE",10:" PINK ROSE",11:" COMMON LIME",12:" EMERALD SWALLOWTAIL",13:" GREAT YELLOW MORMON",14:" COMMON MORMON",15:" SCARLET MORMON",16:" GIANT SILK MOTH",17:" CLIPPER",18:" GOLDEN BIRDWING"}
		def buyitem():
			for x in items:
				#itm=int(input(" Classification Code :   #"))
				itm=random.randint(1,18)
				
				OR=random.randint(1,2000)
				put_markdown( "##      PURCHASED ITEMS ")
				put_text(" --------------------------------------------------------------------")
				put_markdown("### DESCRIPTION      PRICE  AMOUNT")
				put_text(" --------------------------------------------------------------------")
				put_markdown('### Upload Image')
				put_image("# Choose file")
				img=file_upload("Select an image",  accept="image/*")
				qty=int(input(" How many items?:  "))
				#qty=random.randint(1,200)
				
				if itm>=0 and itm<=20:
					percent=random.randint(0,100)
					put_text(" Sales Invoice  :   ", OR)
					put_text(" Date           :  ",today)
					put_text(" Classification Code :  ", itm)
					put_text(" How many items      :  ", qty)
					put_text( " Predicted Butterfly   : ",items[itm], "    \n Predicted Percent    :  " , percent ,"%", " \n Predicted Price         :  ",price[itm])
					total_amount=price[itm]*qty
					put_text(" AMOUNT          :  ", total_amount)
					sub_total=total_amount
					put_text(" SUBTOTAL",sub_total)
					print("ITEMS PURCHASED TODAY  ",str(today),img,str(qty),str(items[itm]),str(price[itm]),str(total_amount))
					#data=total_amount
					#df=data.DataFrame(data)
					put_text(" ------------------------------------------------------------------------")
					put_text(" Reference #     : ", random.randint(0,1000000000000000))
					put_text(" ***********************************************")
				else:
					put_text(" Wrong PIN.. Call the", manager_name, "to,", PIN)
					print(" No Item choose: ")
					print(exit())
		buyitem()
		w.writerow([today,OR,img,qty,itm,items[0],price[0],percent,total_amount,sub_total])
		#put_file('purchased.text', 'Date','Image','Quantity', 'Predicted Butterfly','PREDICTED PRICE','AMOUNT')
		ans=(" Do you want to enter more?")
	img = Image.open('/storage/emulated/0/documents/butterfly/mango.jpg', 'r')
	img.show()
	# (x, y) position
	xy = (50, 100)
	# Get pixel value
	pixel_value = img.getpixel(xy)
	print(pixel_value)
	pixel_value = list(img.getdata())
#	pixel_value_flat = [x for sets in pixel_value for x in sets]
F=open("buyItemPos.csv","r")
reader=csv.reader(F)
for row in reader:
	print (row.append())
	F.closed()

"""
	def Total_amount():
					
		sub_total[0]=0
		if subtotal[0]>=0 or subtotal[0]<=18:
			subtotal=sub_total[0]+sub_total[0]
		else:
			subtotal=sub_total[0]+sub_total[0]
			put_text(" SUBTOTAL       :  ", subtotal)
			amount_pay=int(input(" AMOUNT TO PAY  : " ))
			cash=int(input(" CASH           :  " ))
			put_text(" CASH                      : ", cash)
			change=int(cash-amount_pay)
			put_text(" CHANGE                 : " , change)
			put_text(" CARD NUMBER      : ", int(card_num))
			put_text(" CARD TYPE             : ", card_type)
			put_text(" -----------------------------------------------------------------")
			
		Total_amount()
"""
"""
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
        (16,"Parthenos sylvia"),
        (17,"Samia luzonica"),
        (18,"Troides rhadamantus"),
        (19,"Paroparung bukid"),
)

put_table([['Classification Code','Quantity', 'Predicted Butterfly', 'Percent','PREDICTED PRICE','AMOUNT'],['itm','qty','items[itm]','percent','price[item]','total_amount']])
#put_text(f"total_amount([price[i[0]] * i[1] for i in total_amount[0]])")
"""