import csv
import random
import time
from pywebio.input import input, FLOAT,file_upload
from pywebio.output import put_text,put_markdown,put_table,put_image,put_file
from pywebio. session import local
from PIL import Image
from colorama import Fore
import datetime as dt


with open('diseaseTreatmentPos.csv',"a",newline="") as f:
	w=csv.writer(f)
	today = dt.datetime.today().strftime('%A %B %d, %Y')
	items={1:" BATWING",2: " ATLAS MOTH",3:" RED LACEWING", 4:" COMMON MIME",5:" PLAIN TIGER",6:" TAILED JAY",7:" COMMON JAY",8:" GREAT EGGFLY",9:" PAPER KITE",10:" PINK ROSE",11:" COMMON LIME",12:" EMERALD SWALLOWTAIL",13:" GREAT YELLOW MORMON",14:" COMMON MORMON",15:" SCARLET MORMON",16:" GIANT SILK MOTH",17:" CLIPPER",18:" GOLDEN BIRDWING"}
	treatments={1:"Larvae that have Tachinid flies diseases require immediate attention before the disease takes over. Usually, a single larva develops inside an individual host insect. Many tachinid larvae almost totally consume the host insect before they bore out of the host to pupate and complete the. Reducing the use of insecticides and providing sources of food like dills, parsley, clover and other herbs are the most efficient ways to conserve Trachinid flies in agricultural ecosystems (Ellis; Bradley, 1996: pp. 328-329).",2:"Larvae that have Ophryocystis diseases require immediate attention before the disease takes over. butterfly scale.The only currently known way of treating the Ophryocystis parasite is by soaking the host's eggs in a light bleach solution, which kills the spores that are present on the eggs' surface",3:"Larvae that have Nuclear polyhedrosis diseases require immediate attention before the disease takes over. Larvae were treated with nuclear polyhedrosis virus (NPV) in the laboratory to assess whether the presence of virus could potentially explain reduced fecundity observed in declining field populations of the host.",4:"The propensity of T. bourarachae to cold storage with and without diapause induction was studied. The effect of this technique on its emergence rate and parasitic activity was investigated. The study showed that wasps of T. bourarachae treated at the induction temperature of 15 °C for 5 days can be stored at 4 ± 1 °C for more than 30 days without significant loss of their performances. By using this prestorage temperature, T. bourarachae could keep its emergence capacity (77.5%) up to 60 days of cold storage at 4 ± 1 °C. However, its parasitic activity decreased significantly (37.16%) after 45 days of cold storage. " ,5:"Larvae that have Ophryocystis diseases require immediate attention before the disease takes over. Thoroughly dissect all species to prevent viral infections. Separate healthy larvae from the sick larvae. Clean the larval cabinet regularly. Transfer away to the safest cabinet like a new place for propagation and improve baculovirus-based pesticides is concentrated in the area of the virus genome controlling its host range.",6:"Larvae is Healthy, No Need  Treatment"}
	diseases={1:"No problem, healthy",2:"Tachinid flies",3:"Ophryocystis elektroscirrha",4:"Nuclear polyhedrosis",5:"Trichogramma wasps",6:"Baculoviruses", 7:"Unknown disease."}
	stages=["eggs","larvae","pupae","adult"]
	put_text("       \n  DISEASE TREATMENT FOR LARVAE")
	put_text(" ----------------------------------")
	print(" DESCRIPTION ", "        BUTTERFLY CLASS")
	print(" ----------------------------------")
	put_markdown('### Upload Image')
	put_image("# Choose file")
	img=file_upload("Select an image",  accept="image/*")
	def DiseaseTreatment():
	   seconds=""
	   time=""
	   #days=input(" \n How many days past?")
	   qty=0
	   for x in items:
	       #itm=int(input(" Classification Code :   #"))
	       itm=random.randint(1,6)
	       #qty=int(input(" How many items?:  "))
	       today=dt.date.today()
	       seconds=60*60*int(itm)
	       put_text(" Last  "+str(seconds)," seconds ago.")
	       put_text(" Date:", today,"\n")
	       if itm>=0 and itm<=20:
	           put_text(" Classification of Butterfly   : ", items[itm])
	           put_text( " Predicted larvae  :",items[itm], "  Percent :" , random.randint(0,100),"%")
	           put_text(" Classification Disease Code   : #", itm)
	           put_text(" PREDICTED DISEASE : ",treatments[itm])
	           #print(" \n TREATMENT         : ", treatments[itm])
	           put_text(" ----------------------------------")
	           put_text(" Reference #    : ", random.randint(0,1000000000000000))
	           print(" **********************************")
	       else:
	          put_text(" Wrong PIN..")
           
DiseaseTreatment()
# Get pixel value
pixel_value = img.getpixel(xy)
print(pixel_value)
pixel_value = list(img.getdata())
pixel_value_flat = [x for sets in pixel_value for x in sets]

F=open("diseaseTreatmentPos.csv","r")
reader=csv.reader(F)
for row in reader:
	print (row.append())
	F.closed()
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
"""