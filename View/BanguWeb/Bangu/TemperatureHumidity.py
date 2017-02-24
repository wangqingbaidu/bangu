import sys
sys.path.append("/home/pi/eHouse/")

import serial
import time
import lcd1602
from FileOperation.execSQL import exeSQL

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.open()
lcd = lcd1602.HD44780()
try:
	totalRunTime = 0
	while 1:
		res = ser.readline()
		res = res.strip("\r\n")
		res = res.split(",")
#		print '***********************'
#		print res
#		print '-----------------------'
		lcd.clear()
		if res[0] == "OK":
			msg = "Temperature:%s \nHumidity:%s%%"% (res[2], res[1])
#			print msg
			lcd.message(msg)
			
			if totalRunTime % 60 == 0:
				sql = 'update TempHum set temperature=%f,humidity=%f where id = 1;' %(float(res[2]), float(res[1]) / 100.0)
				#print sql
				exeSQL(sql)
		totalRunTime += 1
		time.sleep(1)
except KeyboardInterrupt:
     ser.close()
