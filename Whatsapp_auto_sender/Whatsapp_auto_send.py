import pandas
import pywhatkit
from CSV_grabber import reader
from besked import msg, afskedmsg
import datetime
import pyautogui
dt = datetime.datetime.now()
ugenr = int(dt.strftime("%W"))
year = datetime.date.today().year
read = reader(ugenr,year)
besked = msg()
afsked = afskedmsg()
PC = read[0]
Mikser = read[1]
Host = read[2]
Podiet = read[3]
Message = (f"{besked} \nuge: {ugenr}  \n @{PC} på PC \n @{Mikser} på Mikser \n @{Host} på Host \n @{Podiet} på Podiet\n {afsked}")
print(Message)
#pywhatkit.sendwhatmsg_instantly("+4553628405", Message, 20)
pywhatkit.sendwhatmsg_to_group("FieoIDakdn77PHasvu1Eo9","",13,6,0)
pyautogui.sleep(10)
print("auto vågen")
pyautogui.typewrite(Message+"@ivan")
pyautogui.press("enter")

