import random
import datetime as dt
from registration import fname

print(" MANAGE FARM")
print(" MY Farm")
print(" CREATE HOME ")

print(" Name :  ",fname)
print(" Location : ")
y=""
home=[" Cabinet"," Puparium"," Butterfly House"]
puparium=["A","B","C","D"]
cabinet=["A","B","C","D","E","F","G"]
house=["A","B","C","D"]
for i in home:
	print("      Select :  ", i)
if y==True:
	print(" Done",btnsubmit)
	
print(" JOIN HOME ")
print(" Please ask for invitation code from the owner of this farm. ")
itm=random.randint(1,1000)
#itm=input(itm)
print("   CODE: " , itm)
if y==True:
	print(" Done",btnsubmit)
o=0
if o>=0 and o<=6:
	print(" \n Cabinet  : ", cabinet)
if o>=0 and o<=4:
	print(" \n Puparium : ", puparium)
if o>=0 and o<=4:
	print(" \n House    : ", house)
today=dt.datetime.today()
print("                      Date : ", today)
import pupaDefects
import butterflyDefects
import exposure