# A simple script 
from pywebio.input import input,FLOAT
from pywebio.output import put_text
import random
import datetime as dt
import csv


with open('buterflyDefects.csv',"w",newline="") as f:
	w=csv.writer(f)
	field=["Classification Defects Code","PREDICTED DEFECTS","Reference","HOURS","DATE/TIME","Classification of Butterfly","QUANTITY","Predicted Adult Butterfly","Percent"]
	w.writerow(field)
	ans="y"
	while ans=="y":
		adultDefects=["crumpled wings","torn wings","incomplete legs","unpaired antennae","broken thorax","cut proboscis","slashed abdomen","fractured wing veins"]
		items={1:" BATWING",2: " ATLAS MOTH",3:" RED LACEWING", 4:" COMMON MIME",5:" PLAIN TIGER",6:" TAILED JAY",7:" COMMON JAY",8:" GREAT EGGFLY",9:" PAPER KITE",10:" PINK ROSE",11:" COMMON LIME",12:" EMERALD SWALLOWTAIL",13:" GREAT YELLOW MORMON",14:" COMMON MORMON",15:" SCARLET MORMON",16:" GIANT SILK MOTH",17:" CLIPPER",18:" GOLDEN BIRDWING"}
		print("       \n  DEFECTS OF BUTTERFLY ")
		print(" ----------------------------------")
		print(" DESCRIPTION ", "        BUTTERFLY CLASS")
		print(" ----------------------------------")
		def butterflyDefects():
		  hour_in_a_day=""
		  days=""
		  percent=random.randint(0,100)
		  #days=input(" \n How many days past?")
		  qty=0
		  for x in items:
		      #itm=int(input(" Classification Image :   #"))
		      itm=random.randint(1,8)
		      #Items=int(input(" How many items?:  "))
		      today=dt.datetime.today().strftime('%A %B %d, %Y')
		      hour_in_a_day=24*int(itm)
		      print(" Last  "+str(hour_in_a_day)," hours ago.")
		      print(" Date:", today,"\n")
		      if itm>=0 and itm<=20:
		          print(" Classification of Butterfly   : ", items[itm])
		          print( " Predicted Adult Butterfly  :",items[itm], "  Percent :" , percent,"%")
		          #put_text("  Percent :", percent)
		          print(" Classification Defects Code   : #", itm)
		          print(" PREDICTED DEFECTS : ",adultDefects[itm])
		          print(" ----------------------------------")
		          print(" Reference #    : ", random.randint(0,1000000000000000))
		          print(" **********************************")
		      else:
		          print(" Wrong PIN..")
		butterflyDefects()		          
w.writerow([hour_in_a_day,today,items,itm,qty,adultDefects,percent])
ans=(" Do you want to enter more?")
	
f=open("butterflyDefects.csv","r")
reader=csv.reader(f)
for row in reader:
	print (row)
	f.closed()

"""
coices from field
items=[
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
]
"""

