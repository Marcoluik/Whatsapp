import pandas
import pywhatkit
from CSV_grabber import reader
from besked import msg, afskedmsg
import datetime
dt = datetime.datetime.now()
ugenr = int(dt.strftime("%W"))
read = reader(ugenr)
besked = msg()
afsked = afskedmsg()
PC = read[0]
Mikser = read[1]
Host = read[2]
Podiet = read[3]
Message = (f"{besked} \n uge: {ugenr}  \n @{PC} på PC \n @{Mikser} på Mikser \n @{Host} på Host \n @{Podiet} på Podiet\n {afsked}")
print(Message)
#pywhatkit.sendwhatmsg_instantly("+4553628405", Message, 5)
