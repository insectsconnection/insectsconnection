import datetime as dt
import csv
from pywebio.input import input, FLOAT,TEXT,NUMBER,PASSWORD,checkbox,slider
from pywebio.output import put_text,put_markdown,put_table
#from pywebio. session import local
from pywebio.session import *

#csv.writer(csvfile, dialect=’excel’, **fmtparams)

	#PROPER CARE MANAGEMENT SYSTEM
title=" Butterfly Production\n"
new_title=title.center(59)
print(new_title.title())
print("        WELCOME TO BUTTERFLY PRODUCTION TRAINING\n")
put_markdown("##      WELCOME TO BUTTERFLY PRODUCTION TRAINING\n")

today=dt.datetime.today()
print("                          Date:", today,"\n")
put_text(" Date : ",today)
fname=""
lname=""
username=""
email=""
pass1=""
pass2=""
age=0
day_of_the_week="Friday"

with open('breeders.csv', 'w', newline='') as f:
	   writer = csv.writer(f)
	   field=["First Name", "Last Name", "Username","Password","Confirm Passowrd","Email","Age","Day"]
	   writer.writerow(field)
	   ans="y"
	   while ans=="y":
	   	def signup():
	   		print(" REGISTRATION")
	   		put_markdown("### REGISTRATION")
	   		fname = input(" First Name: ",type=TEXT,required=True,placeholder="Your Firstname")
	   		lname = input(" Last Name: ",type=TEXT,required=True,placeholder="Your Lastname")
	   		username=input(" Username: ", help_text="Please put alphanumeric.", placeholder="Your Name")
	   		#pass1="*****"
	   		password=input(" Password: ", type=PASSWORD,required=True,)
	   		confirm_password=input(" Confirm Password: ", type=PASSWORD,required=True, )
	   		email=input(" Email: ", type=TEXT, required=True,)
	   		print("    \n REGISTRATION SUCCESSFUL\n")
	   		put_text(" Welcome ",fname, lname)
	   		greeting=f" Good morning {fname.upper()}. Today is {today}.".format("day",day_of_the_week)
	   		put_text(greeting)
	   		put_text(' It is good to meet you ' + fname.upper()+ " " +lname.upper(), " \n the length of your n name is :", int(len(fname))+ int(len(lname)))
	   		age = input(" How old are you "+fname.upper()+"?",type=NUMBER)
	   		put_text(' You will be ' + str(int(age)+ 1) + ' in a year! \n\n ')
	   		# CheckBox
	   		agree = checkbox("Agreement", options=['I agree to terms and conditions'])
	   		slider(label="AUGMENTED：",value=5, min_value=1, max_value=100, step=1)
    
	   	signup()
	   writer.writerow([fname,lname,username,pass1,pass2,email,age])
f=open("breeders.csv","r")
reader=csv.reader(f)
for row in reader:
	print (row)
f.closed()
	   


	   

"""
writer.writerow(["First Name", "Last Name", "Username"])
	   writer.writerow([1, "Ash Ketchum", "English"])
	   writer.writerow([2, "Gary Oak", "Mathematics"])
	   writer.writerow([3, "Brock Lesner", "Physics"])
"""