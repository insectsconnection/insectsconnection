#pip install plyer,notify-py
from pywebio.output import *
from pywebio.input import * 
import time, datetime as dt
from plyer import notification
import time

while True:
    time.sleep(30)
    notification.notify(
        title = 'testing',
        message = 'message',
        app_icon = "image.ico",
        timeout = 10,
    )

notification.notify(
    title = 'testing',
    message = 'message',
    app_icon = None,
    timeout = 10,
)

from notifypy import Notify

notification = Notify(
  default_notification_title="Function Message",
  default_application_name="Great Application",
  default_notification_icon="path/to/icon.png",
  default_notification_audio="path/to/sound.wav"
)

def your_function():
  # stuff happening here.
  notification.message = "Function Result"
  notification.send()