# assumes that circuit python is installed on the board, the link for which is given in the readme

import board 
import digitalio
import busio
import time

BUTTON_PIN = board.GP12
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

EN = digitalio.DigitalInOut(board.GP3)
EN.direction = digitalio.Direction.OUTPUT
EN.value = True

uart = busio.UART(tx=board.GP4, rx=board.GP5, baudrate=9600)

WROOM_CONNECTED = False

time.sleep(0.25)

print("connecting")
uart.reset_input_buffer()
while not WROOM_CONNECTED:
    if uart.in_waiting:
        data = uart.readline().decode('utf-8').strip()
        print(data)
        if data == "WROOM READY":
            WROOM_CONNECTED = True
            uart.reset_input_buffer()
    time.sleep(0.1)

print("CONNECTED")

for x in range(0,3):
    uart.write("BREADBOARD READY\n")


debounce = False
while True:

    if uart.in_waiting:
        data = uart.readline().decode('utf-8').strip()
        if data.startswith("ERROR:"):
            print(f"{data}")

    if button.value and not debounce:
        debounce = True
        uart.write("GET_QUOTE\n")
        while not uart.in_waiting:
            pass
        data = uart.readline().decode('utf-8').strip()
        if data.startswith("QUOTE:"):
            quote = data.split("QUOTE:")[1]
            print(f"{quote}\n")
        elif data.startswith("ERROR:"):
            print(f"{data}\n")
            
    elif not button.value:
        debounce = False

    time.sleep(0.01)


