import LCD
import time
from subprocess import check_output
from RPi import GPIO
GPIO.setmode(GPIO.BCM)

try:
    lcd = LCD.Lcd()
    ip = check_output(['hostname', '--all-ip-addresses'])
    ips = ip.split()
    while True:
        for i in range(len(ips)):
            lcd.write_scroll("ip-adressen:", str(ips[i])[2:-1])
            time.sleep(5)
except Exception as e:
    print(e)
finally:
    print("gestopt")
    GPIO.cleanup()