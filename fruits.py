from pywebio.output import *
from pywebio.input import * 
import time, datetime as dt
from datetime import date,timedelta

res = textarea('Text area', code={
    'mode': "python",
    'theme': 'darcula'
})
def set_now_ts(set_value):
    set_value(int(time.time()))

ts = input('Timestamp', type=NUMBER, action=('Now', set_now_ts))

def select_date(set_value):
    with popup('Select Date'):
        put_buttons(['Today'], onclick=[lambda: set_value(date.today(), 'Today')])
        put_buttons(['Yesterday'], onclick=[lambda: set_value(date.today() - timedelta(days=1), 'Yesterday')])
d=input('Date', action=('Select', select_date), readonly=True)
put_text(type(d), d)


def check_age(age):
    if age>30:
        return 'Too old'
    elif age<10:
        return 'Too young'
input('Input your age', type=NUMBER, validate=check_age)

# 'Name' cell across 2 rows, 'Address' cell across 2 columns
put_table([
    [span('Name',row=2), span('Address', col=2)],
    ['City', 'Country'],
    ['Wang', 'Beijing', 'China'],
    ['Liu', 'New York', 'America'],
])

put_table([
    ['Type', 'Content'],
    ['html', put_html('X<sup>2</sup>')],
    ['text', '<hr/>'],
    ['buttons', put_buttons(['A', 'B'], onclick=...)],  
    ['markdown', put_markdown('`Awesome PyWebIO!`')],
    ['file', put_file('hello.text', b'hello world')],
    ['table', put_table([['A', 'B'], ['C', 'D']])]
])


with popup("Subscribe to the page"):
	put_text("I hope you are having a great day!")
	put_markdown('## Welcome to our fruit store')
	put_table([['Fruit', 'Price'],
	['Blueberry', 20],
	['Mango', 25], 
	['Kiwi', 15]
	])
	fruit = select("Choose your favorite Fruit", ['Blueberry', 'Mango', 'Kiwi'])
	put_text(f"You chose {fruit}. Please wait until it is served!")
	put_processbar('bar')
	for i in range(1, 11):
	    	set_processbar('bar', i / 10)
	    	time.sleep(0.05)
	    	put_markdown(f"Here is your {fruit}! Enjoy!")
	    	if fruit == 'Mango':
	    		put_image(open('/storage/emulated/0/documents/butterfly/mango.jpg', 'rb').read())
	    	elif fruit == 'Blueberry':
	    		put_image(open('/storage/emulated/0/documents/butterfly/mango.jpg', 'rb').read())
	    	else:
	    		put_image(open('/storage/emulated/0/documents/butterfly/kiwi.jpg', 'rb').read())
	    		
# Upload a file and save to server                      
f = input.file_upload("Upload a file")                  
open('asset/'+f['filename'], 'wb').write(f['content'])  

imgs = file_upload("Select some pictures:", accept="image/*", multiple=True)
for img in imgs:
    put_image(img['content'])