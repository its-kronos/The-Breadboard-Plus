# Assumes that micropython is installed on the WROOM module, which should be for the ESP32-C3
# To flash after micropython is installed, please use the USB UART bridge given in the firmware folder and use any tool to flash, running at 115200 baud

WIFI_NAME = ""
WIFI_PASSWORD = ""


import network
from machine import UART as UART_maker
import time
import requests

UART = UART_maker(1)
UART.init(baudrate=9600, bits=8, tx=9, rx=8)

wifi = network.WLAN()
wifi.active(True)


error = False
err_m = ""

wifi.connect(WIFI_NAME, WIFI_PASSWORD)
while not wifi.isconnected():
    if wifi.status() == network.STAT_WRONG_PASSWORD:
        err_m = "Wrong WiFi password"
        error = True
        break
    elif wifi.status() == network.STAT_NO_AP_FOUND:
        err_m = "No WiFi access point found"
        error = True
        break
    time.sleep(0.5)


BREADBOARD_READY = False

while not BREADBOARD_READY:
    UART.write("WROOM READY\n")
    if UART.any():
        data = UART.readline().decode('utf-8').strip()
        if data == "BREADBOARD READY":
            BREADBOARD_READY = True
    time.sleep(0.1)

time.sleep(0.1)

UART.read()

while True:
    if error:
        UART.write(f"ERROR:{err_m}\n")
        break

    if UART.any():
        data = UART.readline().decode('utf-8').strip()
        if data=="GET_QUOTE":
            res = requests.get("https://zenquotes.io/api/random")
            if res.status_code == 200:
                quote = res.json()[0]['q'] + " - " + res.json()[0]['a']
                UART.write(f"QUOTE:{quote}\n")
            else:
                error = True
                err_m = "Failed to fetch quote"

    time.sleep(0.1)
