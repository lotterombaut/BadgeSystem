import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pir = 26
led = 21
GPIO.setup(pir, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
    time.sleep(2)
    while 1:
        if GPIO.input(pir):
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led, GPIO.LOW)
            print("beweging")
        time.sleep(0.1)
except:
    GPIO.cleanup()

#import time
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)

#led = 21
#pir = 26

#GPIO.setup(led, GPIO.OUT)
#GPIO.setup(pir, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#def licht(a):
#    print("beweging")
#    print("licht aan")
#    GPIO.output(led, GPIO.HIGH)

#    time.sleep(2)

#    print("licht uit")
 #   GPIO.output(led, GPIO.LOW)

#print("ready")

#try:
#    GPIO.add_event_detect(pir, GPIO.FALLING, callback=licht)
 #   while 1:
 #       print(GPIO.input(pir))
 #       time.sleep(1)
#except KeyboardInterrupt:
  #  print("Quit")
 #   GPIO.cleanup()