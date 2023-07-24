from pywebio.input import input, FLOAT,file_upload
from pywebio.output import put_text,put_markdown,put_table,put_image,put_file
from pywebio. session import local
terminal=[" 0 Lawton Terminal", " 1 Kalaw"," 2 UN Ave", " 3 Quirino Ave", " 4 Buendia", " 5 Baclaran", " 6 Bacoor", " 7 Imus", " 8 Dasma", " 9 Silang"," 10 Mendez Terminal"]

terminal2=[ " 0 Lawton Terminal"," 1Kalaw","2 UN Ave", "3 Quirino Ave", "4 Buendia", "5 Baclaran", "6 Bacoor", "7 Imus", "8 Dasma", "9 Silang","10 Mendez Terminal"]
ter=0
ter2=0
def start():
		ter=int(input(" Kilometer start : " ))
		if ter==0:
			print(" FROM: ",terminal2[0])
			put_text(" FROM: ",terminal2[0])
		elif ter>=2 and ter<=4:
			print(" FROM:", terminal2[1])
			put_text(" FROM: ", terminal2[1])
		elif ter>=5 and ter<=9:
			print(" FROM: ", terminal2[2])
			put_text(" FROM: ", terminal2[2])
		elif ter>=10 and ter<=14:
			print(" FROM:", terminal2[3])
			put_text(" FROM: ", terminal2[3])
		elif ter>=15 and ter<=19:
			print(" FROM: ", terminal2[4])
			put_text(" FROM: ", terminal2[4])
		elif ter>=20 and ter<=24:
			print(" FROM: ", terminal2[5])
			put_text(" FROM: ", terminal2[5])
		elif ter>=25 and ter<=29:
			print(" FROM: ", terminal2[6])
			put_text(" FROM: ", terminal2[6])
		elif ter>=30 and ter<=39:
			print(" FROM: ", terminal2[7])
			put_text(" FROM: ", terminal2[7])
		elif ter>=40 and ter<=49:
			print(" FROM:", terminal2[8])
			put_text(" FROM: ", terminal2[8])
		elif ter>=50 or ter<=59:
			print(" FROM:", terminal2[9])
			put_text(" FROM: ", terminal2[9])
		elif ter>=60 or ter<=69:
			print(" FROM: ", terminal2[10])
			put_text(" FROM: ", terminal2[10])
		elif ter>=70 or ter<=80:
			print(" FROM: ", terminal2[11])
			put_text(" FROM: ", terminal2[11])
		else:
			print(" FROM: ", terminal2[12])
			put_text(" FROM: ", terminal2[12])
start()

def end():
		ter2=int(input(" Kilometer start : " ))
		if ter2==0:
			print(" TO      : ",terminal[0])
			put_text(" TO      :  ",terminal[0])
		elif ter2>=2 and ter2<=4:
			print(" TO      : ", terminal[1])
			put_text(" TO      : ", terminal[1])
		elif ter2>=5 and ter2<=9:
			print(" TO      : ", terminal[2])
			put_text(" TO      : ", terminal[2])
		elif ter2>=10 and ter2<=14:
			print(" TO      : ", terminal[3])
			put_text(" TO      : ", terminal[3])
		elif ter2>=15 and ter2<=19:
			print(" TO      : ", terminal[4])
			put_text(" TO      : ", terminal[4])
		elif ter2>=20 and ter2<=24:
			print(" TO      : ", terminal[5])
			put_text(" TO      : ", terminal[5])
		elif ter2>=25 and ter2<=29:
			print(" TO      : ", terminal[6])
			put_text(" TO      : ", terminal[6])
		elif ter2>=30 and ter2<=39:
			print(" TO      : ", terminal[7])
			put_text(" TO      : ", terminal[7])
		elif ter2>=40 and ter2<=49:
			print(" TO      : ", terminal[8])
			put_text(" TO      : ", terminal[8])
		elif ter2>=50 or ter2<=59:
			print(" TO      : ", terminal[9])
			put_text(" TO      : ", terminal[9])
		elif ter2>=60 or ter2<=70:
			print(" TO      : ", terminal[10])
			put_text(" TO      : ", terminal[10])
		else:
			print(" TO      : ", terminal[11])
			put_text(" TO      : ", terminal[11])
end()