# The Breadboard+

![PCB_FRONT](https://github.com/user-attachments/assets/3adad736-2129-4c30-b9ae-679a96ccceec)

![PCB_BACK](https://github.com/user-attachments/assets/6c6d4610-c3ea-4d7f-a9e6-3198758aaf28)

<img width="3000" height="4000" alt="Adobe Express - file (1)" src="https://github.com/user-attachments/assets/c257884d-8349-4daf-8d14-e619e1e1ce54" />

<img width="433" height="577" alt="20250730_171424-removebg-preview" src="https://github.com/user-attachments/assets/de9f793a-691e-497e-8d1b-aa8430076bc8" />


# What is it?
- The Breadboard+ is a custom RP2040 devboard in the ***shape of bread*** and fun decorations on both the front and back, making it slightly bigger than others in return for a much nicer look.
- This board should have nearly everything that would be needed for any IOT project, including a ***USBC connection, 24 GPIO pins (4 analog), and even WIFI connectivity*** through a secondary microcontroller on the board (the ESP-32 WROOM C3)
- Unfortunately, the WIFI connection must sacrifice 1 out of 2 UART connections when in use, but other than that, the sky's the limit!
# Why did I design it?
- Many designs for devboards like the PI Pico and other competitors have been designed to be as compact as possible, but this naturally limits space for creativity and art on the PCB itself. Rather than make something with the constraint of size, I decided to add as many features that I saw reasonable without removing too much.
- After previously designing a keyboard PCB with a bare RP2040 chip, I decided that creating a custom devboard would be a good way for me to practice reading documentation and extend upon the skills developed during that previous project.

![image](https://github.com/user-attachments/assets/1a4461b9-ab84-4c5d-8580-057af9d8251b)

# Demo

[demo](https://youtube.com/shorts/6yIjaiG749g?feature=share)

# Instructions & Credits

- To be able to flash the ESP32-C3 on the board, you must use the code given in the firmware production folder. Raw code is given in this folder as well, and in order to build it, you would have to clone [this repo for a PIO USB UART bridge](https://github.com/GrechTech/rp2040-pio-uart-bridge) by GrechTech and replace the uart-bridge.c file with the code version you want, bootloader for installing something like micropython, and the normal version for using thonny with micropython.

- If you are planning to implement UART with the WROOM, please use pins 8 and 9, as those are what work the best

- To use circuitpython on the RP2040 chip, please use the custom board build inside the firmware folder. You can build it yourself from [my circuitpython fork](https://github.com/its-kronos/circuitpython), and eventually (once it gets approved), from [Adafruit](https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/) and maybe even the offical circuitpython website one day


### Pin naming conventions: 
  - WIFI/WROOM/GP3 (turn value to high to use WIFI)
  - WROOM_TX (goes to WROOM's GPIO 8/RX)
  - WROOM_RX (goes to WROOM's GPIO 9/TX)
  - All other GPIO pins on the board work as normal/labelled

# Surprises
- When I first started routing the PCB, I didn't realize how thick the traces would need to be to insure a 90 ohm impedence on the USB data lines, which is called for by USB standards. This posed quite a difficulty because the design rules checker (DRC) kept on warning that the clearence between traces was too small, and it took me a good amount of time to learn how to assign different rules for different netlists (AKA connected parts).

![image](https://github.com/user-attachments/assets/a21a8e85-5be8-416c-a298-47e3b4b37227)

- Something that was pretty surprising, but not much of a challenge for me to work around was the cost of PCBA for custom devboards
- Naturally, custom devboards would require many parts that are considered "extended" requiring 3 dollars per type of component for assembly.
- I had already tried choosing the best parts for their task (most of which were either basic parts or extended preferred)

![image](https://github.com/user-attachments/assets/4c23ecc2-318d-4fd9-ac7d-5ead1e68d810)

- With this amount of extended parts (the 27 ohm resistor being extended preferred), the price for PCBA ended up being quite high
![image](https://github.com/user-attachments/assets/fc779ca7-f714-4f4b-bec4-3427f23bfb41)

# PCB
- There were some moments of learning, but since I already created a PCB for a bare-chip custom keyboard, this process was pretty fast comparatively.
![image](https://github.com/user-attachments/assets/7673d5b7-8ca9-4117-a122-7dee78e772a3)

![image](https://github.com/user-attachments/assets/8636b02e-7edc-40ab-a2ba-13ff5da1ca1c)
![image](https://github.com/user-attachments/assets/fa821974-743b-48d4-8863-e21d9f0e82e5)
![image](https://github.com/user-attachments/assets/c8feffc1-2c8f-4bc7-a94c-e4c0a7d5b139)
![image](https://github.com/user-attachments/assets/a44f97c6-7b3c-4edb-8427-2f9e2576d3ef)



# CAD
- I unfortunately feel that anything in a single-color print wouldn't really look good and instead completely hide the purpose that I designed this PCB for.
- The PCB was designed to look creative, but printing a case would would hide these qualities, and the best case that I see coming out of it would be copying the breadshape from an SVG and effortlessly extruding it as well as adding holes for screws

# BOM

| VENDOR     | ITEM    | PRICE(USD)                                        | SHIPPING | PCS                         | CNT | REMARKS 1                         | REMARKS 2                             |
|------------|---------|---------------------------------------------------|----------|-----------------------------|-----|-----------------------------------|---------------------------------------|
|            |         |                                                   |          |                             |     |                                   |                                       |
| JLCPCB     |         |                                                   |          |                             |     |                                   |                                       |
|            | PCB     | 3.2                                               |          | 5                           | 1   | LEAD-FREE HASL                    |                                       |
|            | PCBA    | 42.43                                             |          | 2                           | 1   | Only for SMD                      |                                       |
|            |         |                                                   | 26.83    |                             |     | UPS DDP to avoid customs headache (cheapest shipping available with DDP) | Detailed by the cost-optimizing guide |
|            |         |                                                   | 25.1    |                             |     | Taxes & Fees                      |                                       |
|            |         |                                                   |          |                             |     |                                   |                                       |
|            | TOTAL   | 97.56                                             |          |                             |     |                                   |                                       |
|            |         |                                                   |          |                             |     |                                   |                                       |
| ALIEXPRESS |         |                                                   |          |                             |     |                                   |                                       |
|            | [HEADERS](https://www.aliexpress.us/item/3256807894655866.html?spm=a2g0o.productlist.main.10.2048TOyvTOyvjB&algo_pvid=78836b1f-3d59-4a97-b9b7-cac95eaa052c&algo_exp_id=78836b1f-3d59-4a97-b9b7-cac95eaa052c-52&pdp_ext_f=%7B%22order%22%3A%2220%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%212.13%212.13%21%21%212.13%212.13%21%4021030ea417511226170433127e741d%2112000043591263791%21sea%21US%216403496327%21X&curPageLogUid=TOsqkBImCibu&utparam-url=scene%3Asearch%7Cquery_from%3A#nav-specification) | 2.13                                              |          | 10 1x40 Female 10 1x40 Male | 1   |                                   |                                       |
|            | [BUTTONS](https://www.aliexpress.us/item/3256804068199319.html?spm=a2g0o.productlist.main.4.e8c1dec5Inxuai&aem_p4p_detail=202506280802286024204940544760001218999&algo_pvid=f3ffc751-558f-49ca-ac5c-7ffbabd14130&algo_exp_id=f3ffc751-558f-49ca-ac5c-7ffbabd14130-3&pdp_ext_f=%7B%22order%22%3A%22680%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%212.77%212.77%21%21%2119.73%2119.73%21%402103146c17511229483267527eb3c8%2112000028534796958%21sea%21US%216403496327%21X&curPageLogUid=fRMaRWsfiR0Y&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202506280802286024204940544760001218999_1) | 2.77                                              |          | 20                          | 1   | 6x6x4.3mm                         | EXCLUDED                              |
|            |         |                                                   | 1.99     |                             |     |                                   |                                       |
|            |         |                                                   |          |                             |     |                                   |                                       |
|            | TOTAL   | 4.12                                              |          |                             |     |                                   |                                       |
|            |         |                                                   |          |                             |     |                                   |                                       |
|            |         |                                                   |          |                             |     |                                   |                                       |
| TAXES      |         | (Have way more than enough needed for ALIEXPRESS) |          |                             |     |                                   |                                       |
|            |         |                                                   |          |                             |     |                                   |                                       |
| TOTAL      | 101.68   |                                                   |          |                             |     |                                   |                                       |


