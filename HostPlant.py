import random
import datetime as dt

items={1:" BATWING",2: " ATLAS MOTH",3:" RED LACEWING", 4:" COMMON MIME",5:" PLAIN TIGER",6:" TAILED JAY",7:" COMMON JAY",8:" GREAT EGGFLY",9:" PAPER KITE",10:" PINK ROSE",11:" COMMON LIME",12:" EMERALD SWALLOWTAIL",13:" GREAT YELLOW MORMON",14:" COMMON MORMON",15:" SCARLET MORMON",16:" GIANT SILK MOTH",17:" CLIPPER",18:" GOLDEN BIRDWING"}

Hostplant_name=[
"Winged Prickly Ash",
"Sweet Potato Vine, Camote Tops",
"Dregea Volubilis",
"Limeberry, Sweet Lime",
"Parsonsia",
"Tetradium",
"Dutchman's Pipe, Indian Tree",
"Soursop",
"Calamondin, Orange Calamondin",
"Heart Veins",
"Crown Flower, Giant Milkweed",
"Blood Flower, Tropical Milkweed, Scarlet Milkweed",
"Curry Leaf, Curry Tree",
"Common Skillpod",
"Pomelo",
"Sweet Orange"]



print("       \n  HOSTPLANT/ IMAGE FRUIT ")
print(" ----------------------------------")
print(" DESCRIPTION ", "        HOSTPLANT CLASS")
print(" ----------------------------------")




def Hostplant_Name():
    Items=0
    for x in items:
        #itm=int(input(" Classification Code :   #"))
        itm=random.randint(1,4)
       
        #Items=int(input(" How many items?:  "))
        today=dt.datetime.today()
        print(" Date:", today,"\n")
        Items=random.randint(1,10)
   
        if itm>=0 and itm<=20:
            print(" Classification of Butterfly   : ", items[itm])
            print( " Predicted Host  :",items[itm], " Percent :" , random.randint(0,100),"%")
            print(" Classification Host Code   : ", itm)
            print(" PREDICTED HOSTPLANT : ",Hostplant_name[itm])
            
            print(" ----------------------------------")
            print(" Reference #    : ", random.randint(0,1000000000000000))
            print(" **********************************")
           
        else:
            print(" Wrong PIN..")
           
Hostplant_Name()