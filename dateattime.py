list_of_numbers = [1,2,3,4,4,4,5,]
no_duplicate_set = set(list_of_numbers)
print(no_duplicate_set)


no_duplicate_list = list(no_duplicate_set)
list_of_numbers = no_duplicate_list
print(list_of_numbers)

library_1={'Harry Potter','Hunger Games','Lord of the Rings'}

print(library_1)

library_2 = {'Harry Potter','Romeo and Juliet',}
print(library_2)

all_books_in_town = library_1.union(library_2)
print(all_books_in_town)

all_both_libraries = library_1.intersection(library_2)
print(all_both_libraries)


import re
text = 'random string.Myame12@website.com.some more random text. YourName888@company.net'
pattern = re.compile('[a-z A-Z 0-9]+\,[a-zA-Z]+')
result = pattern.search(text)
print(result)

import datetime

today = datetime.date.today()
print("DATE:", today)
birthday = datetime.date(1990, 2, 21)
print('BIRTHDAY', birthday)

days_since_birth = (today - birthday).days
print('DAYS SINCE BIRTH',days_since_birth)

tdelta = datetime.timedelta(days = 10)
print('PLUS TEN DAYS STARTING TODAY',today-tdelta)

print(today.day)
#Monday = 0, Sunday = 6
print(today.weekday())
print(datetime.time(7, 2, 20,15))

#datetime.date (Y, M, D)
#datetime.time (h,m, s, ms)
#datetime.datetime (Y, M , D, h, m, s, ms)

hour_delta = datetime.timedelta(hours =10)
print(datetime.datetime.now() + hour_delta)

l1 = [1,"a", True, "b",2, False]
if l1[0] == 1:
	print(l1)

 
