import random
import datetime as dt

schedule=[" Monday"," Tuesday"," Wednesday"," Thursday"," Friday"," Satuday"," Sunday"]
items={1:" BATWING",2: " ATLAS MOTH",3:" RED LACEWING", 4:" COMMON MIME",5:" PLAIN TIGER",6:" TAILED JAY",7:" COMMON JAY",8:" GREAT EGGFLY",9:" PAPER KITE",10:" PINK ROSE",11:" COMMON LIME",12:" EMERALD SWALLOWTAIL",13:" GREAT YELLOW MORMON",14:" COMMON MORMON",15:" SCARLET MORMON",16:" GIANT SILK MOTH",17:" CLIPPER",18:" GOLDEN BIRDWING"}
Items=0
#perform supervisor task
#def supervisorTask():
    #...
#record to my database that the supervisor is running
#def supervisorCheckIn():
    #...

#this function will execute our tasks in a separate thread
def threadTask(job_function, arguments):
	#schedule my supervisor to run and check itself in every 10 minutes
	schedule.every(10).minutes
	do(threadTask(superviorTask))
	schedule.every(10).minutes
	do(threadTask(supervisorCheckIn))
	while 1:
		schedule.run_pending()
		time.sleep(1)
		
def mgttask():
	print("                      MANAGEMENT AND TASKS \n")
	today=dt.datetime.today()
	print("                      Date : ", today)
	task={}
	task["gl"]="get leaves"
	task["ih"]="interaction by heating the puparium" 
	task["gf"]="get flowers"
	task["wc"]="wash the cagenet"
	task["cb"]="clean bottles"
	task["pf"]="clean the ponds or fall"
	print(" \n TO DO TASK ")
	print(task)#task.append="Separate instars"
	tasks=input(" \n ENTER YOUR TASK KEYWORD..")
	def tsk():
		if tasks=="ih":
			print(" Please do this task. "+task["ih"])
		elif tasks=="gf":
			print(" Please do this task. "+task["gf"])
		elif tasks=="wc":
			print("Please do this task. "+task["wc"])
		elif tasks=="gt":
			print(" Please do this task. "+task["gt"])
		elif tasks=="cb":
			print(" Please do this task. "+task["cb"])
		elif tasks=="pf":
			print(" Please do this task. "+task["pf"])
		elif tasks=="gl":
			print(" Please do this task. "+task["gl"])
		else:
			exit()
			print("No TASK")
	tsk()
mgttask()
print(" Select from the schdule : \n  ", schedule)


stages={1:"  EGGS stage", 2:"  LARVAL stage",3:"  PUPAL stage",4:"  ADULT stage"}
def Stages():
	
	for x in stages:
		#stgs=int(input("Enter stages :"))
		stgs=random.randint(0,3)
		
		if stgs>=1 and stgs<=4:
			print(stages[stgs])
			print(items[stgs], "Butterfly",schedule[stgs])
			
Stages()