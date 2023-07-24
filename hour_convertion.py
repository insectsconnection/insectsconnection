#hours=[]
days=0
hours=0
days=input("Please input days :")
hours=24*int(days)
def week(hour):
    if hours<=167 :
    	print(" zero week ago/", hours,"hours." )
    elif hours==168 :
    	print(" one week ago/", hours,"hours." )
    	if days=="1":
    		print(" and one day")
    	elif days=="2":
    		print(" and two days")
    	elif days =="3":
    		print("and three days")
    	elif days=="4":
    		print(" and four days")
    	elif days=="5":
    		print(" and five days")
    	elif days=="6":
    		print(" and six days")
    	else:
    		print("")
    elif hours==336 and hours>=336:
    	print(" two weeks ago/", hours,"hours." )
    	if days=="8":
    		print(" and one day")
    	elif days=="9":
    		print(" and two days")
    	elif days =="10":
    		print("and three days")
    	elif days=="11":
    		print(" and four days")
    	elif days=="12":
    		print(" and five days")
    	elif days=="13":
    		print(" and six days")
    	else:
    		print(exit())
    elif hours==504 and hours>=504:
    	print(" three weeks ago/", hours,"hours." )
    elif hours==672 and hours>=672:
    	print(" four weeks ago/", hours,"hours." )
    elif hours==1008 and hours>=1008:
    	print(" five weeks ago/", hours,"hours")
    elif hours==1176 and hours>=1176:
    	print(" six weeks ago/", hours ,"hours")
    elif hours==1334 and hours>=1344:
    	print(" seven weeks ago/", hours,"hours" )
    elif hours==1512 and hours>=1512:
    	print(" eight weeks ago/", hours,"hours" )
    else:
    	print(" nine weeks ago", hours, "hours" )
week=week(hours)

