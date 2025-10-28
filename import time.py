import time
from RPLCD.i2c import CharLCD



def timeToString(specificTime):
    currentTime = time.localtime(specificTime)
    return f"{currentTime[2]}/{currentTime[1]}/{currentTime[0]}:{currentTime[3]}:{currentTime[4]}"
#print(time.time())
#print(time.localtime(time.time()))
mytime = str(timeToString(time.time()))
print(mytime)
file = open("camReadTime.txt", "w")
file.write(mytime)



lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

lcd.write_string('You owe: ')
lcd.write_string('$100')

lcd.crlf()

lcd.write_string(mytime)

