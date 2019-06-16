from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

inst = {"function_set": 0b00111000, "display_on": 0b00001111, "clear_display_&_cursor_home": 0b00000001, "new_line": 0b11000000}


class Lcd:

    def __init__(self, E = 23, RS = 18, datapins = [5,22,27,17,6,20,16,12]):
        self.E = E
        self.RS = RS
        self.datapins = datapins
        GPIO.setup(self.datapins, GPIO.OUT)
        GPIO.setup([self.E, self.RS], GPIO.OUT)
        GPIO.output(self.E, GPIO.HIGH)
        GPIO.output(self.datapins, GPIO.LOW)
        self.send_instruction(inst["function_set"])
        self.send_instruction(inst["display_on"])
        self.send_instruction(inst["clear_display_&_cursor_home"])

    def send_instruction(self, value):
        GPIO.output(self.RS, GPIO.LOW)
        GPIO.output(self.E, GPIO.HIGH)
        self.set_data_bits(value)
        GPIO.output(self.E, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.E, GPIO.HIGH)

    def send_character(self, value):
        GPIO.output(self.RS, GPIO.HIGH)
        GPIO.output(self.E, GPIO.HIGH)
        self.set_data_bits(value)
        GPIO.output(self.E, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(self.E, GPIO.LOW)

    def set_data_bits(self, byte):
        mask = 128
        for i in range(8):
            x = (byte & mask >> i) >> 8 - (i + 1)
            GPIO.output(self.datapins[i], x)

    def write_message(self, value):
        for i in value:
            self.send_character(ord(i))

    def new_line(self):
        self.send_instruction(inst["new_line"])

    def write_scroll(self, head, boodschap):
        self.send_instruction(0b00000001)
        if len(boodschap) > 16:
            b = boodschap
            lijst = []
            for i in b:
                lijst.append(i)
            for i in range(40 - lijst.__len__()):
                lijst.append(" ")
            for i in range(24):
                self.send_instruction(inst["clear_display_&_cursor_home"])
                self.write_message(head)
                self.new_line()
                for j in range(i, i + 16):
                    self.send_character(ord(lijst[j]))
                time.sleep(0.5)
        else:
            self.write_message(head)
            self.new_line()
            self.write_message(boodschap)