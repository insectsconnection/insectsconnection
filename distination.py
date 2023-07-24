from pywebio.input import input, FLOAT,file_upload
from pywebio.output import put_text,put_markdown,put_table,put_image,put_file
from pywebio. session import local
terminal=[" 0 Lawton Terminal", " 1 Kalaw"," 2 UN Ave", " 3 Quirino Ave", " 4 Buendia", " 5 Baclaran", " 6 Bacoor", " 7 Imus", " 8 Dasma", " 9 Silang"," 10 Mendez Terminal"]

distination=[ " 0 Lawton Terminal"," 1Kalaw","2 UN Ave", "3 Quirino Ave", "4 Buendia", "5 Baclaran", "6 Bacoor", "7 Imus", "8 Dasma", "9 Silang","10 Mendez Terminal"]

def start():
		ter=int(input(" Kilometer start : " ))
		if ter==0:
			print(" FROM: ",terminal[0])
			put_text(" FROM: ",terminal[0])
		elif ter>=2 and ter<=4:
			print(" FROM:", terminal[1])
			put_text(" FROM:", terminal[1])
		elif ter>=5 and ter<=9:
			print(" FROM:", terminal[2])
			put_text(" FROM:", terminal[2])
		elif ter>=10 and ter<=14:
			print(" FROM:", terminal[3])
			put_text(" FROM:", terminal[3])
		elif ter>=15 and ter<=19:
			print(" FROM:", terminal[4])
			put_text(" FROM:", terminal[4])
		elif ter>=20 and ter<=24:
			print(" FROM:", terminal[5])
			put_text(" FROM:", terminal[5])
		elif ter>=25 and ter<=29:
			print(" FROM:", terminal[6])
			put_text(" FROM:", terminal[6])
		elif ter>=30 and ter<=39:
			print(" FROM:", terminal[7])
			put_text(" FROM:", terminal[7])
		elif ter>=40 and ter<=49:
			print(" FROM:", terminal[8])
			put_text(" FROM:", terminal[8])
		elif ter>=50 or ter<=59:
			print(" FROM:", terminal[9])
			put_text(" FROM:", terminal[9])
		elif ter>=60 or ter<=70:
			print(" FROM:", terminal[10])
			put_text(" FROM:", terminal[10])
		else:
			print(" FROM:", terminal[11])
			put_text(" FROM:", terminal[11])
start()

def unload():
		dist=int(input(" Kilometer end   : " ))
		if dist==0:
			print(" TO  : ",distination[0])
			put_text(" TO  : ",distination[0])
		elif dist>=2 or dist<=4:
			print(" TO  : ",distination[1])
			put_text(" TO  : ",distination[1])
		elif dist>=5 or dist<=9:
			print(" TO  : ", distination[2])
			put_text(" TO  : ", distination[2])
		elif dist>=10 or dist<=14:
			print(" TO  : ", distination[3])
			put_text(" TO  : ", distination[3])
		elif dist>=15 or dist<=19:
			print(" TO  : ", distination[4])
			put_text(" TO  : ", distination[4])
		elif dist>=20 or dist<=24:
			print(" TO  : ", distination[5])
			put_text(" TO  : ", distination[5])
		elif dist>=25 or dist<=29:
			print(" TO  : ", distination[6])
			put_text(" TO  : ", distination[6])
		elif dist>=30 or dist<=39:
			print(" TO  : ", distination[7])
			put_text(" TO  : ", distination[7])
		elif dist>=40 or dist<=49:
			print(" TO  : ", distination[8])
			put_text(" TO  : ", distination[8])
		elif dist>=50 or dist<=59:
			print(" TO  : ", distination[9])
			put_text(" TO  : ", distination[9])
		elif dist>=60 or dist<=70:
			print(" TO  : ", distination[10])
			put_text(" TO  : ", distination[10])
		else:
			exit()
			#print(" TO  : ", distination[11])
			#put_text(" TO  : ", distination[11])
unload()