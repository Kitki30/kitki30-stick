import time
import machine

ir_pin = None

def set_ir(pin):
    global ir_pin
    ir_pin = pin

def mark(dur):
    ir_pin.freq(40000)
    ir_pin.duty(512)
    time.sleep_us(dur)

def space(dur):
    ir_pin.duty(0)
    time.sleep_us(dur)

def send_sony(data, bits=12):
    mark(2400)
    space(600)
    
    for i in range(bits):
        if (data >> i) & 1:
            mark(1200)
        else:
            mark(600)
        space(600)
    
    ir_pin.duty(0)
    
def send_array(codes):
    for data, bits in codes:
        print("Sending Sony (Code: " + str(data) + " Bits: " + str(bits) +")")
        send_sony(data, bits)
        time.sleep(0.05)
