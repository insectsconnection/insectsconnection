import datetime as dt
import random

#PROPER CARE MANAGEMENT SYSTEM
title=" Butterfly Production\n"
new_title=title.center(59)
print(new_title.title())
print("        WELCOME TO BUTTERFLY PRODUCTION TRAINING\n")

today=dt.datetime.today()
print("                          Date:", today,"\n")

fname=""
lname=""
username=""
email=""
age=0
day_of_the_week="Friday"
def signup():
	print(" REGISTRATION")
	fname = input(" First Name: ")
	lname=input(" Last Name: ")
	username=input(" Username: ")
	pass1="*****"
	print(" Password: ",pass1)
	print(" Confirm Password: ", pass1)
	email=input(" Email: ")
	print("    \n REGISTRATION SUCCESSFUL\n")
	print(" Welcome ",fname, lname)
	greeting=f" Good morning {fname.upper()}. Today is {today}.".format("day",day_of_the_week)
	print(greeting)
	print(' It is good to meet you ' + fname.upper()+ " " +lname.upper(), " \n the length of your n name is :", int(len(fname))+ int(len(lname)))
	age = input(" How old are you "+fname.upper()+"?")
	print(' You will be ' + str(int(age)+ 1) + ' in a year! \n\n ')
	print("         PROFILE")
signup()
email=email
username=username

def login():
	#user=input(" Username:")
	if username==username or email==email:
		print(username)
	elif pass1==pass1:
		print(pass1)
	else:
		exit()
login()
print("   PROFILE")
breeder=""
def Q(a):
	breeder=input(" Are you already a breeder ?Y/N: ")
	if breeder=="Y" or breeder=="y":
		print(" You are certified breeder.")
	elif breeder=="N" or breeder=="n":
		print(" You are newbie.")
	else:
		print(" Please enter the correct answer." )
		exit()
		login()
	#return Q(breeder)
Q(breeder)

type=[" breeder"," purchaser"," enthusiast"," entomologist"]
print("   class ",type)

types=input(" You are..select from the top 1_2_3_4 :  " )
def reg():
	if types=="1":
		print(type[0])
	elif types=="2":
		print(type[1])
	elif types=="3":
		print(type[2])
	elif types=="4":
		print(type[3])
	else:
		exit()
reg()


print(" \n WE HAVE CLASSIFICATION OF BUTTERFLIES CULTURE IN MARINDUQUE ")
pupae_choices=(
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
        (16,"Samia luzonica"),
        (17,"Parthenos sylvia"),
        (18,"Troides rhadamantus")
)
#print(" \n THE PUPAE AVAILABLE ARE : ",pupae_choices)

#print("\nTHE SPECIES ARE: ", category_species)


diseases=["Tachinid flies","Ophryocystis","Nuclear polyhedrosis","Trichogramma wasps","Baculoviruses"]
print("  \n         TREATMENTS \n")
Diseases=['bacteria', 'fungi' , 'parasitoids','aphids']

predators = {"ant" : "Ants","bir" : "Birds","gna" : "Gnats","liz" : "Lizards","spi" : "Spiders","was" : "Wasps",
}

#predators["bir"])
"""os.listdir(storage/emulated/0/documents/liveweather.py)"]"""
problem=""
print(" \n History of Exposure in DISEASES.")
print(Diseases)
problem=int(input(" Please enter number only 1-4: "))
def diseases(d):
	if problem==1:
		print(" Diseases:",diseases[0])
	elif problem==2:
		print(" Diseases:",Diseases[1])
	elif problem==3:
		print(" Diseases:",Diseases[2])
	elif problem==4:
		print(" Diseases:",Diseases[3])
	else:
		print(" No Problems!")
Diseases=diseases(problem)
print(diseases)
cagenet={"1": " Cagenet1","2":" Cagenet2","3":" Cagenet3","4":" Cagenet4","5":" Cagenet5"}
cage=int(input("\n Place of Exposure in Cagenet number 1-5: "))
#print(cagenet)
if cage==1:
	print(cagenet["1"])
elif cage==2:
	print(cagenet["2"])
elif cage==3:
	print(cagenet["3"])
elif cage==4:
	print(cagenet["4"])
elif cage==5:
	print(cagenet["5"])
else:
	print("None:")

source=[" camera1"," camera2"," camera3"]
sources=int(input("\n Sources of Exposure 1,2, 3: "))
if sources==1:
	print(source[0].capitalize())
elif sources==2:
	print(source[1].capitalize())
elif sources==3:
	print(source[2].capitalize())
else:
	print("None")
#print(source)

category=[" foul smell", " wet fluids", " colouring enzymes"]
categories=int(input("\n Category EXPOSURE are foul \n 1.smell, 2.wet fluids, and 3.colouring enzymes: "))
if categories==1:
	print(category[0].capitalize())
elif categories==2:
	print(category[1].capitalize())
elif categories==3:
	print(category[2].capitalize())
else:
	print("None:")
	
print(" \n History of Exposure in PREDATORS.")
print(predators)
pred=int(input(" Enter number from 1-6: "))
def predator(p):
	if pred==1:
		print(" Predator", predators["ant"])
	elif pred==2:
		print(" Predator", predators["bir"])
	elif pred==3:
		print(" Predator", predators["gna"])
	elif pred==4:
		print(" Predator", predators["liz"])
	elif pred==5:
		print(" Predator", predators["spi"])
	elif pred==6:
		print(" Predator", predators["was"])
	else:
		print("No Predators")
predator=predator(pred)

print('THE PREDATORS VISITED IS ', predators["bir"])
print(predators)
for x in predators:
	pred=input("Enter the predators: ")
	if pred=="ant":
		print("Predators visited today. "+predators["ant"])
	elif pred=="bir":
		print("PREDATORS VISITED TODAY. "+predators["bir"])
	elif pred=="gna":print("PREDATORS VISITED TODAY. "+predators["gna"])
	elif pred=="liz":
		print("PREDATORS VISITED TODAY. "+predators["liz"])
	elif pred=="spi":
		print("PREDATORS VISITED TODAY. "+predators["spi"])
	elif pred=="was":
		print("PREDATORS VISITED TODAY. "+predators["was"])
	else:
		print("NO ONE PREDATORS VISITED TODAY. "+predators["none"])
print("    QUALITY AND ASSURANCE \n")
defect=["overbend abdomen","ants bite","strechmark abdomen","improportion body"]
defects=input("  PUPAE DEFECTS\n  ")
def deft():
	if defects=="1":
		print(" predicted : ", defect[0])
	elif defects=="2":
		print(" predicted : ", defect[1])
	elif defects=="3":
		print(" predicted : ",defect[2])
	elif defects=="4":
		print("  predicted :", defects[3])
	else:
		exit()
deft()
today=dt.datetime.today()
print(" Date:", today,"\n")

Temperature=["relative_humidity","dewpoint"]
temp = float(input(" \n Enter today temperature:"))
rh=float(input(" \n Enter relative humidity: "))
#temperature
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
dp=float(temp-(100-float(rh))/5.0)
rh=float(dp)

print(" The dewpoint is " ,"{:.2f}".format(dp), " °Celsius")
def liveweather():
	print(" TODAY TEMPERATURE is ", "{:.2f}".format(cel), " °Celsius")
	if cel <20 or cel >32:
		print(" The weather is bad temperature", "{:.2f}".format(cel), " °Celsius")
	else:
		print(" The weather is good temperature", "{:.2f}".format(cel), " °Celsius")

liveweather()

print(" \n THE GOOD TEMPERATURE VARIES FROM 28 degree Celsius \n to 32 degree Celsius for the butterflies in order to live")
temp = float(input(" \n Enter today temperature exposure in too hot,too wet/too cold:"))
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0

def liveweather2():
	print(" TODAY TEMPERATURE is ","{:.2f}".format(cel), " °Celsius")
	if cel <28 or cel >32:
		print(" The weather is bad temperature", "{:.2f}".format(cel), " ° Celsius")
	else:
		print(" The weather is good temperature"," {:.2f}".format(cel), " ° Celsius\n")

print(" EXPOSURE in TOO COLD,TOO WET, TOO HOT")
def exposure():
	if cel>=10 and cel<=27:
		print(" TOO COLD"  ,"{:.2f}".format(cel), " °Celsius") 
	elif cel>27 and cel<33:
		print(" NORMAL TEMPERATURE"  ,"{:.2f}".format(cel), " °Celsius") 
	
	elif cel<=10:
		print(" TOO WET",  "{:.2f}".format(cel), " °Celsius")
	elif cel>50:
		print(" THAT IS NOT NORMAL TEMPERATURE, YOU GO TO HELL"  ,"{:.2f}".format(cel), " °Celsius") 
	else:
		print(" TOO HOT" ,"{:.2f}".format(cel), " °Celsius") 
exposure()
				

liveweather2()

today=dt.datetime.today()
print(" Date: ", today)
eggs=["Attacus atlas","Cethosia biblis","Hypolimnas bolina","Danaus chrysippus","Papilio demoleus","Pachliopta kotzebuea","Idea Leuconoe","Graphium doson","Graphium agamemnon","Chilasa clytia","Papilio palinurus","Papilio lowi","Papilio polytes","Papilio rumanzovia","Samia luzonica", "Atrophaneura semperi","Partheno sylvia","Troides rhadamantus"]
larvae=["Attacus atlas","Cethosia biblis","Hypolimnas bolina","Danaus chrysippus","Papilio demoleus","Pachliopta kotzebuea","Idea Leuconoe","Graphium doson","Graphium agamemnon","Chilasa clytia","Papilio palinurus","Papilio lowi","Papilio polytes","Papilio rumanzovia","Samia luzonica", "Atrophaneura semperi","Partheno sylvia","Troides rhadamantus"]

pupae={
        "1":"Atrophaneura semperi",
        "2":"Attacus atlas",
        "3":"Cethosia biblis",
        "4":"Chilasa clytia",
        "5":"Danaus chrysippus",
        "6":"Graphium agamemnon",
        "7":"Graphium doson",
        "8":"Hypolimnas bolina",
        "9":"Idea leuconoe", 
        "10":"Pachliopta kotzebuea",
        "11":"Papilio demoleus",
        "13":"Papilio palinurus",
        "12":"Papilio lowi",
        "14":"Papilio polytes",
        "15":"Papilio rumanzovia",
        "16":"Samia luzonica",
        "17":"Parthenos sylvia",
        "18":"Troides rhadamantus"
        }
adult = {1:"Attacus atlas",2:"Cethosia biblis", 3:"Hypolimnas bolina", 4: "Danaus chrysippus",5:"Papilio demoleus", 6:"Pachliopta kotzebuea", 7:"Idea leuconoe", 8:"Graphium doson",9:"Graphium agamemnon", 10:"Chilasa clytia", 11:"Papilio palinurus", 12:"Papilio lowi",13:"Papilio polytes", 14:"Papilio rumanzovia", 15:"Samia luzonica",16:"Atrophaneura semperi", 17:"Parthenos Sylvia",18:"Troides rhadamantus"}

stages=["EGGS stage", "LARVAL stage","PUPAL stage", "ADULT stage"]
stages=int(input(" \n ENTER BUTTERFLY STAGES : 1-4\n"))
def Stages():
	if stages==1:
		print("EGGS stage", eggs.sort())
	elif stages==2:
		print("LARVAL stage ",larvae.sort())
	elif stages==3:
		print("PUPA stage " , pupae.sort())
	elif stages==4:
		print("ADULT stage", adult.sort())
	else:
		print("NONE.")
	return (eggs,larvae,pupae,adult)
Stages()

def stages():
	if stages>=0 and stages<=4:
		print(stages.sort())

print("         \n SCHEDULES\n ")
print("     TOTAL HOURS OF SCHEDULE IN A WEEK")
total_hour=0
day=[" Monday"," Tuesday"," Wednesday"," Thursday"," Friday"," Saturday"," Sunday"]
for x in day:
	hour =int(input(" Enter hours: "))
	if hour>0 and hour<24:
		print(" Hour for "+x+" is "+str(hour))
		total_hour+=int(hour)
	elif hour >24:
		print(" Invalid, try numbers not over 24 hours")
		
print(" TOTAL HOUR IS "+str(total_hour))

print("\n What was happened in "+str(total_hour)+"?")
print(" \n Date:",today)
days=input(" \n How many days past?")
seconds_in_a_day = 24 * 60 * 60*int(days)
print(" \n Last "+str(seconds_in_a_day*31)+ " seconds ago. ")
if days>="2":
	print(" You have to check it regularly..")
elif days<"2":
	print(" Thank you for the update daily.")
hour_in_a_day=24*int(days)
print(" Last  "+str(hour_in_a_day)+" hours ago.")
minutes_in_a_day=24*60*int(days)
print(" Last  "+str(minutes_in_a_day)+" minutes ago.")
days_in_week=24*7*int(days)
print(" Last", days_in_week," hours ago.")
weeks_in_year=24*60*7*54*int(days)
print(" Last", weeks_in_year, " hours ago.")
weekly=int(weeks_in_year)/int(days_in_week)
print(" Week in a Year:", weekly)
seconds_in_a_day/=2
print(" One half of it  "+str(seconds_in_a_day)+" seconds ago.")
seconds_in_a_day/=2
print(" One fourth of it  "+str(seconds_in_a_day)+" seconds ago.")
	
	
print("What butterfly species? ")

#filename=df['filename']
#class_names=df["class_names"]
#np.unique(class_names)

for key in pupae:
	print(key, pupae[key])
#   print(pupae.get("4"))
#LEP=lep()
#print(LEP)



pupa=input("\n Enter code numbers from 1-18: ")

if pupa == 1:
	print(pupae[1])
elif pupa== 2:
	print(pupae[2])
if pupa == 3:
	print(pupae[3])
elif pupa== 4:
	print(pupae[4])
if pupa == 5:
	print(pupae[5])
elif pupa== 6:
	print(pupae[6])
if pupa == 7:
	print(pupae[7])
elif pupa== 8:
	print(pupae[8])
if pupa == 9:
	print(pupae[9])
elif pupa== 10:
	print(pupae[10])
if pupa == 11:
	print(pupae[11])
elif pupa== 12:
	print(pupae[12])
if pupa == 13:
	print(pupae[13])
elif pupa== 14:
	print(pupae[15])
if pupa == 16:
	print(pupae[16])
elif pupa== 17:
	print(pupae[17])
elif pupa == 18:
	print(pupae[18])

	
print("\n Enter the hours for the day of exposure you monitored in a week.")
print("Pupae of ", pupae)

exposure=[ 'bacteria', 'fungi' , 'parasitoids']
exposures=input("\nTYPE OF EXPOSURE in 1.bacteria,2.fungi, and 3.parasitoids: ")
if exposures=="1":
	print("EXPOSURE in"+exposure[0].capitalize())
elif exposures=="2":
	print("EXPOSURE in  "+exposure[1].capitalize())
elif exposures=="3":
	print("EXPOSURE in "+exposure[2].capitalize())
#print(exposure[1])
predators = {
"ant" : "Ants",
"bir" : "Birds",
"gna" : "Gnats",
"liz" : "Lizards",
"spi" : "Spiders",
"was" : "Wasps",
}


dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print(dict)


case=input("Case: ")
print(case)
size=input("Size: ")
print(size)

acitivities=['feeding','basking','puddling','patroling','mating','egg laying','hybernating','migrating','camouflage','nectaring','munching','oviposting','crawling','hatchling']
print("Butterfly Activities", activities)
print(activities)
print("Done!! THANK YOU")
import POS