import time as t
from win10toast import ToastNotifier

title = str(input("Title of timer: "))
note = str(input("Note of timer: "))

hours = int(input("How many hours to wait: "))
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))

seconds += (hours*3600) + (minutes*60)

for i in range(seconds):
    t.sleep(1)

toast = ToastNotifier()
toast.show_toast(f"{title}", f"{note}", duration=20)