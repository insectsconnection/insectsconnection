import random
import datetime as dt
import csv
from pywebio.input import input, FLOAT,file_upload
from pywebio.output import put_text,put_markdown,put_table,put_image,put_file
from pywebio. session import local
from PIL import Image
from colorama import Fore
#import pandas as pd

with open('buterflyDefects.csv',"w",newline="") as f:
	w=csv.writer(f)
	field=["Classification Defects Code","PREDICTED DEFECTS","Reference","HOURS","DATE/TIME","Classification of Butterfly","Predicted Adult Butterfly","Percent"]
	w.writerow(field)
	ans="y"
	while ans=="y":
		
		#butterflyIdentifier=["english_name","scientific_name,description","year_discovered","name","broken thorax","cut proboscis","slashed abdomen","fractured wing veins"]
		items={0:"none",1:" BATWING",2: " ATLAS MOTH",3:" RED LACEWING", 4:" COMMON MIME",5:" PLAIN TIGER",6:" TAILED JAY",7:" COMMON JAY",8:" GREAT EGGFLY",9:" PAPER KITE",10:" PINK ROSE",11:" COMMON LIME",12:" EMERALD SWALLOWTAIL",13:" GREAT YELLOW MORMON",14:" COMMON MORMON",15:" SCARLET MORMON",16:" GIANT SILK MOTH",17:" CLIPPER",18:" GOLDEN BIRDWING", 19:"Gray Glassy Tiger"}
		print("       \n  BUTTERFLY IDENTIFICATION ")
		print(" -------------------------------------------------")
		print(" DESCRIPTION ", "        BUTTERFLY CLASS")
		print(" -------------------------------------------------")
		put_text("       \n  BUTTERFLY IDENTIFICATION ")
		put_text(" -------------------------------------------------")
		put_text(" DESCRIPTION ", "        BUTTERFLY CLASS")
		put_text(" -------------------------------------------------")
		def butterflyId():
		  hour_in_a_day=""
		  days=""
		  scientific_name=""
		  size=""
		  color=""
		  dosposition=""
		  color_11=""
		  nasal_11=""
		  posterior_11=""
		  subspecies10=""
		  name10=""
		  yr_discovered10=""
		  subspecies10=""
		  place10=""
		  descriptions="annotations of image"
		  #Buttetfly 
		  adult_butterfly= ['fat','orange', 'loud',' Pachliopta kotzebuea deseileus','Fruhstorfer','1911','Papilionidae; Papilioninae; Troidini','Bago, Neg. Occ.']
		  size = adult_butterfly[0]
		  color = adult_butterfly[1]
		  disposition = adult_butterfly[2]
		  species10=adult_butterfly[3]
		  name10= adult_butterfly[4]
		  yr_discovered10=adult_butterfly[4]
		  subspecies10=adult_butterfly[5]
		  place10=adult_butterfly[6]
		  today=dt.datetime.today().strftime('%A %B %d, %Y')
		  larvae_demoleus=["coffee-colored"," nasal band", "faintly visible 2 dark bands near its posterior"]
		  color_11=larvae_demoleus[0]
		  nasal_11=larvae_demoleus[1]
		  posterior_11=larvae_demoleus[2]
		  #days=input(" \n How many days past?")
		  qty=0
		  scientific_name=[
		(0,"None"),
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
        (19,"none"),
]
		  for x in items:
		      percent=random.randint(0,100)
		      
		      itm=random.randint(1,8)
		      put_markdown('### Upload Image')
		      put_image("# Choose file")
		      img=file_upload("Select an image",  accept="image/*")
		      qty=int(input(" How many items?:  "))
		      today=dt.datetime.today()
		      hour_in_a_day=24*int(itm)
		      print(" Last  "+str(hour_in_a_day)," hours ago.")
		      print(" Date:", today,"\n")
		      put_text(" Last  "+str(hour_in_a_day)," hours ago.")
		      put_text(" Date:", today,"\n")
		      if itm>=0 and itm<=20:
		          print(" Classification of Butterfly   : ", items[itm], " \nScientific Name   : ", scientific_name[itm])
		          print( " Predicted Adult Butterfly  :",items[itm], " 		Predicted Percentage :" , percent,"%")
		          #scientific_name=input(" Scientific Name   : ")
		          put_text(" Classification Image :   #")
		          put_text(" \n Scientific Name   : ", scientific_name[itm])
		          put_text(" Predicted Adult Butterfly  :",items[itm])
		          put_text(" Predicted Percentage :" , percent,"%")
		          put_text(" **********************************")
		          print("The description of a adult butterfly. " + species10,name10,subspecies10,yr_discovered10,place10)
		          put_text(" Butterfly Information         : ",species10,name10,subspecies10,yr_discovered10,place10)
		          put_text(" Descriptions of adult         : ",size,disposition, color)
		          put_text(" Descriptions of larvae       : ",color_11,nasal_11, posterior_11)
		          print(" --------------------------------------------------")
		          
		          print(" Reference #    : ", random.randint(0,1000000000000000))
		          print(" **********************************")
		          put_text(" Reference #    : ", random.randint(0,1000000000000000))
		          put_text(" **********************************")
		      else:
		          print(" Wrong PIN..")
		butterflyId()		          
		w.writerow([hour_in_a_day,today,items,itm,qty,adultDefects,itm])
	ans=(" Do you want to enter more?")
	img.show()
	# (x, y) position
	xy = (50, 100)
	# Get pixel value
	pixel_value = img.getpixel(xy)
	print(pixel_value)
	pixel_value = list(img.getdata())
#	pixel_value_flat = [x for sets in pixel_value for x in sets]
F=open("butterflyDefects.csv","r")
reader=csv.reader(F)
for row in reader:
	print (row)
	F.closed()

"""
coices from field

"""

