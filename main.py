#!/usr/bin/env python
"""
Je laat een LED aangaan, na 5 seconden schakelt deze LED terug uit.
Na 2 seconden gaat deze terug aan, na 2 seconden ook weer uit.
Dit herhaal je 5 keer waarna de led in een blink toestand blijft (1 sec aan, 1 sec uit).
"""


import time
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


remote_factory = PiGPIOFactory(host='192.168.1.31')
led1 = LED(pin=17, pin_factory=remote_factory)


def main():
    for i in range(5):
        led1.on()
        time.sleep(5)
        led1.off()
        time.sleep(2)
        led1.on()
        time.sleep(2)
        led1.off()
        time.sleep(2)
    while True:
        led1.on()
        time.sleep(1)
        led1.off()
        time.sleep(1)


if __name__ == '__main__':  # code to execute if called from command-line
    main()