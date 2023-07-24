import csv 

# data rows as dictionary objects 
mydict =[{'Name': 'Ash Ketchum', 'SNo': '1', 'Subject': 'English'}, 
         {'Name': 'Gary Oak', 'SNo': '2', 'Subject': 'Mathematics'}, 
         {'Name': 'Brock Lesner', 'SNo': '3', 'Subject': 'Physics'}]

# field names 
fields = ['SNo', 'Name', 'Subject'] 

with open('students.csv', 'w', newline='') as file: 
    writer = csv.DictWriter(file, fieldnames = fields)

    writer.writeheader() 
    writer.writerows(mydict)
    

    