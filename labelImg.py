"""
Get Identification
Local name: kotsebuya
English name :PINK ROSE
Scientific subspecies name : Pachliopta kotzebuea 
subspecies name : deseileus 
Discovered by : Fruhstorfer 
Year Discovered : 1911
Family : Papilionidae; Papilioninae; Troidini
Date of flight : 29 Aug 2021; 
Location : Bago, Neg. Occ.
"""

name=""
imgLabel = ['local_name:','english_name:', 'scientific_subspecies_name:', 'discovered_by:', 'Year:', 'family:', 'Date of flight:', 'location:']
cName = ['kotsebuya', 'PINK ROSE', 'Pachliopta kotzebuea deseileus', 'Fruhstorfer', '1911','Papilionidae; Papilioninae; Troidini', ]
for imLabel, cName in zip(name, imgLabel):
    print(imLabel,cName)

#StdTemperature = 37 
#butterfly_temp = 38
butterfly_temp = int(input(" Enter butterfly temp: "))
if butterfly_temp >= 37:
	print(" Bad Weather")
else:
	print(" Good Weather")

"""

Output:
Local name: kotsebuya
English name: PINK ROSE
Scientific subspecies name: Pachliopta kotzebuea deseileus 
Discovered by: Fruhstorfer
Year:1911
Family: Papilionidae; Papilioninae; Troidini
"""