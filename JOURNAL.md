# Journal

# Information
- Title: "The Breadboard"
- Author: An. D. (its_kronos)
- Description: Breadboard, but microcontroller (AKA custom devboard) *probably change later*
- Creation Date: 6/24/2025
- Total Time (before building): 13h 

# 6/24/2025

- Did a lot of unfocused researched, and also hopped in a huddle (voicechat) with @Cyao and asked a lot of questions about incorperating RF into a design
- Confirmed what exactly I wanted to build, which would be a devboard with the 2350B MCU for maximum GPIO and a routing challenge. I would also want to include WIFI connectivity like the PI Pico W, which would make it useful in projects that require things like API calls based on peripherals.

**Time: Untimed, especially since this research was unfocused**

# 6/25/2025

* did some research about the PI235x chips with the hardware guide
* downloaded footprint for RP2350B
* created schematic part for the VREG

![image](https://github.com/user-attachments/assets/2da23498-85c1-4c00-875b-4e9df5356662)


* made custom footprint for the inductor, which recommended a specific part to ensure correct coiling for minimal interferance

![image](https://github.com/user-attachments/assets/ef40a38a-5f6b-4a9a-96e1-944912b26bc9)


* sourced components needed for the VREG
* Made schematic for and sourced all parts needed for the USB connection, including parts like an LDO, which was pretty easy since this is the second time doing it for me

![image](https://github.com/user-attachments/assets/d1e8e4bb-9f0f-4053-9510-2f34f432481e)


* made the schematic for and sourced parts required for decoupling capacitors for the power pins

![image](https://github.com/user-attachments/assets/61debbe0-ebfb-4067-b006-c1bbf4b9f808)


* in the hardware guide for the rp235x series chips, it includes a resistor with value 0 ohms for the QSPI_SS pin, so I researched why there wasn't a direct connection and learned that it can be used as a "jumper wire" on a pcb

![image](https://github.com/user-attachments/assets/1b900ae6-95dd-4f24-a72c-8a1fba96c165)

* finished schematic for the flash memory for the chip

![image](https://github.com/user-attachments/assets/d81e52d5-0797-4207-80ed-3a545993abe8)


* finished schematic for the crystal

![image](https://github.com/user-attachments/assets/c8072dcb-63ff-4bae-b3fc-23d0c1280476)


- And here is the running component list (most of which are either basic or extended preferred parts, which took a bit of time to find, but nothing too serious)!

![image](https://github.com/user-attachments/assets/902b7856-4243-45de-bd03-334c5ceb2df2)


- overall this part of the schematic was pretty easy and didn't require too much challenge, and I believe that the main part of the challenge will come when actually routing the board

**TIME: 2h30m**

* I was done with the RP chip wiring from last session, so now the next logical step would be for me to wire the pin headers, but I was unable to decide which nets/GPIOs should go to which pin on the headers, but I did add a boot button to RUN and some more headers for debugging

![image](https://github.com/user-attachments/assets/944420b2-67c0-4f00-bf80-fd934d120c2c)

* I instead decided to try and add the RF/WIFI IC for the wifi support that I wanted to add, and I looked at the documentation for the CC2500 transceiver by TI, but this only led to me being increasingly confused and spending a lot of time pretty much getting nowhere
* My main question would be how the RP2350 chip would communicate with the CC2500 to control what packets of data or being sent out, or what mode the chip is in.


**time: 1h**

# 6/26/2025

* Using another MCU (the wroom c3) as a way to add wifi connectivity at the cost of 1 UART interface when being used
* decided to start routing the board so that I can know which pins are ideal to use for what purpose, so i assigned all the footprints

![image](https://github.com/user-attachments/assets/9298c907-adc1-4508-9a1d-cd949ea0405e)


* I had trouble routing because the pins were too close together, so I changed the main MCU to the RP2040 and double checked that everything was according to the different hardware guide

![image](https://github.com/user-attachments/assets/3628c8ea-95b3-43e8-b645-53cbb77f72dc)


* i had to replace a few of the parts of the schematics to fit with the RP2040, and then I reselected all the footprints and started routing

![image](https://github.com/user-attachments/assets/22a9316c-8716-49b5-8ddf-000d00cae4c3)


* here is the routing I have so far, and I tried my best to make sure that sensitive components would be out of the way from traces that would disrupt them, but what I did realize is that I need to find a new ESD protection IC since the current one would pretty much make it impossible to route
* It was pretty time consuming due to the numerous decoupling capacitors needed in many locations, and I might have to compromise on a few of them 


**Time: 2h**

* found a new, better ESD protection that would be easier to route and even cheaper too
* restarted routing because I didn't plan for the ESD protection to be this big

![image](https://github.com/user-attachments/assets/51310495-d62c-4185-be19-6e7bbe835603)


* placed everything except the connectors, which could go almost anywhere on the board (this took a while to get everything seemingly spaced out well enough but I feel that it's pretty good)

![image](https://github.com/user-attachments/assets/765502e2-df04-4da1-9bb2-a3c24e8a107c)


* finished routing everything for the main part of the board (meaning excluding WIFI and GPIO), which took around an hour due to slight repositioning and trying to space out signals when possible, which was mostly a new-ish concept for me, which I only slight skimmed over for a keyboard I made prior.

![image](https://github.com/user-attachments/assets/230ba348-8aa4-40d8-9ee5-b88bd68caf82)

**TIME:2h**

# 6/27/2025

* rerouted the differential pair so that it actually has a 90 ohm differential impedance which is called for by USB protocol, and this took a long while because I didn't really know how to get the DRC to stop screaming at me for having too small clearances, but this was fixed by just assigning different netclasses.

![image](https://github.com/user-attachments/assets/e25c85dc-2b6b-48a4-ae40-6c867b012729)


* routed the secondary MCU completely, although i am worried a bit about the TX and RX traces for it interfering, so if I have space in the future after routing GPIO, I'll try to separate them.

![image](https://github.com/user-attachments/assets/34b2d76f-e1e5-4499-862b-68d77f65f4e8)


* moved some components in order to have a much slimmer layout, and then proceeded to route the GPIO pins, which for now was pretty easy (except for deciding which GPIO pin should be where), but I have a feeling that the last few GPIOs might be a lot more difficult

![image](https://github.com/user-attachments/assets/546a7992-ba91-4d1e-a8ba-cae6113803da)



TIME: 2h 15m

* I finished up routing everything which was surprisingly easy due to the amount of excess space I had. It was just a bit time consuming to figure out the best way to route everything to minimize crossovers
* I was a bit worried about the crystal being close to GPIO traces, but somebody also part of Hackclub told me that it's most likely fine due to the grounding vias, but I did also move it closer to the XTAL pins on the MCU
* Added some art on the front and back C:

![image](https://github.com/user-attachments/assets/6832c15f-6d53-4862-ba1c-306d291e18b8)

![image](https://github.com/user-attachments/assets/2edf8ba0-e7a7-4991-9acc-0fa04d617e89)

![image](https://github.com/user-attachments/assets/33ca0cb7-a177-42f1-857f-51fd17137526)

![image](https://github.com/user-attachments/assets/70c8e87b-0a2c-42e2-8d56-9ad9d710b602)


* All that's really left for me would be to draft up some code and maybe (?) create a case (probably not since single-color PLA wouldn't really look that great for it)


**time: 1h45m** 

# 6/28/2025

- Just drafted up some code to be able to flash the second MCU for the WIFI connection by forwarding USB signals through UART
- Started creating stuff like the BOM and will finish a description in the README with pictures (This will most likely be untimed)

**TIME: 30m**

# 6/30/25

- Turns out I used the wrong footprint for the pin headers, so I had to restart routing them and make the board bigger, which wasn't much of a challenge since the routing was pretty similar, but still a bit time consuming.
  
![image](https://github.com/user-attachments/assets/52d549d9-311a-4961-9e7a-d7e7e28af3e0)

- Anyways here is the (hopefully) final version
  
![image](https://github.com/user-attachments/assets/c0ce1422-f917-4611-b2c3-08655632f1f8)
![image](https://github.com/user-attachments/assets/b333355a-2da1-4c38-9407-1c0878888d27)

**TIME: 1h**

# 7/25/25

- Started by figuring out how to get circuit python on the RP2040, which required me to use linux to create a custom devboard config
- Since I used windows, I had to research about virtual machines and had to get linux running with everything needed for circuit python, which was quite a challenge due to me not really using terminal before

<img width="494" height="161" alt="image" src="https://github.com/user-attachments/assets/fad45cbf-a702-42ee-af6d-6a5531bf3deb" />

- However, after flashing circuit python, it didn't allow me to use the TX and RX pins I needed, so then I tried micropython, which also didn't work!

<img width="850" height="660" alt="image" src="https://github.com/user-attachments/assets/fb14635e-0a23-43d1-8ea5-4c8a3950f9e3" />

- I decided to then try circuit python again, but this ultimately failed, and I realized that the RP2040 chip doesn't support UART on *every* single pin, only some of them for TX and RX, so I then learned that I needed to use PIO

**Time: 6.25h**

- I implemented PIO and was able to flash and read the MCU

<img width="463" height="243" alt="image" src="https://github.com/user-attachments/assets/5f4fd61a-8de9-40d7-9e95-c324ae35a9cc" />

<img width="809" height="200" alt="image" src="https://github.com/user-attachments/assets/aff48a09-1e91-437d-b894-1c9a1e2fbf50" />


- However, it did take me a while to learn that I had to use a much slower bauderate than default, and trying to use the normal one just resulted in no connection to esptool

  **TIME: 2h**

- Not much here, but found out that my previous code just completely broke, so next session will be implementing somebody elses USB UART bridge in C, but doing some small edits for things like bootloader mode vs normal

[Repo for the other bridge](https://github.com/GrechTech/rp2040-pio-uart-bridge/tree/main)

**TIME: 30m**
