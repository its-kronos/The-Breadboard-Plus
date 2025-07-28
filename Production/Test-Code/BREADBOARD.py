# assumes that circuit python is installed on the board, the link for which is given in the readme
# also assumes that the module for PIO uart is installed, which is given in the readme

import board 
import digitalio
import adafruit_pio_uart as pio_uart
import time

BUTTON_PIN = board.GP12
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

uart = pio_uart.UART(tx=board.GP2, rx=board.GP1, baudrate=9600)

WROOM_CONNECTED = False

while not WROOM_CONNECTED:
    uart.write("BREADBOARD READY")

    if uart.in_waiting:
        data = uart.read().decode('utf-8').strip()
        if data == "READY FOR COMMANDS":
            WROOM_CONNECTED = True


while True:

    if uart.in_waiting:
        data = uart.read().decode('utf-8').strip()
        if data.startswith("ERROR:"):
            print(f"{data}\n")


    if button.value:
        uart.write("GET_QUOTE")
        while not uart.in_waiting:
            pass
        data = uart.read().decode('utf-8').strip()
        if data.startswith("QUOTE:"):
            quote = data.split("QUOTE:")[1]
            print(f"{quote}\n")
        elif data.startswith("ERROR:"):
            print(f"{data}\n")

    time.sleep(0.1)


