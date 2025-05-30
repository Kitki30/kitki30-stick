from machine import I2C, Pin
import time

i2c = None
did_init = False

CARDKB_ADDR = 0x5F

def init():
    global i2c
    try:
        i2c = I2C(1, scl=Pin(33), sda=Pin(32), freq=100000)
        did_init = True
        return did_init
    except:
        did_init = False
        return did_init

def read():
    data = i2c.readfrom(CARDKB_ADDR, 1)
    return data

def decode(data):
    try:
        return data.decode('utf-8')
    except:
        return None