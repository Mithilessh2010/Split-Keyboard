# Split Keyboard

**Split Keyboard** is a 60-key split mechanical keyboard with wireless support. It runs on a XIAO nRF52840 and is powered by a battery, allowing it to connect to a computer using Bluetooth.

I made this project to learn more about CAD, PCB design, and firmware. I also wanted to build something useful that I can use every day since I currently just use a laptop keyboard.

---

## Overview

This keyboard is split into two halves for better ergonomics. Each half has its own PCB, and all available GPIO pins on the microcontroller are used for the key matrix.

The firmware is written using CircuitPython and the KMK library. Right now, only the right half is programmed, and wireless communication between both halves is still in progress.

---

## CAD Design

All parts were designed in Fusion 360. This project helped me learn how to use curves and improve my overall CAD skills.

After designing the parts, I exported them into Blender to create realistic renders of the keyboard. I also used PCB STEP files, which made it much easier to design the case accurately around the electronics.
<img width="1118" height="713" alt="image" src="https://github.com/user-attachments/assets/20b85372-ee6b-45f1-9ac0-d3f9425c265d" />

---

## PCB Design

The PCBs were designed using KiCad. The keyboard uses a standard switch matrix along with diodes for each key.

There are also test points on the PCB that connect to battery power and ground, which can be useful for debugging and testing.
<img width="1792" height="1261" alt="image" src="https://github.com/user-attachments/assets/5837fe0b-9a37-4edb-8b2f-65ecce4038ad" />

---

## Firmware

The firmware is built using CircuitPython with the KMK library.

At the moment:
- Only the right side of the keyboard is working
- Wireless support has not been fully implemented yet
- More testing will be done once the PCBs arrive

The firmware will be updated as I test and improve the keyboard in real life.

---

## Keymap

The current keymap is designed for the right half of the keyboard. It will likely change as I continue testing and improving usability.

---

## Bill of Materials (BOM)

| Name                                   | Purpose                                      | Quantity | Total Cost (USD) |
|----------------------------------------|----------------------------------------------|----------|------------------|
| LiPo Battery                           | To power the system                          | 1        | 10.66            |
| MINI NRF52840 Development Board        | Main microcontroller (brain)                 | 2        | 8.72             |
| Keycap Set                             | Keycaps for the switches                     | 1        | 21.07            |
| GATERON G Pro Milk Yellow Switches     | Mechanical switches for keys                 | 1        | 20.20            |
| 1N4148 Diodes                          | Used in the keyboard matrix                  | 1        | 2.46             |
| M3 Heat-Set Inserts (4mm, 4.2mm OD)    | Used to secure the case with screws          | 1        | 12.65            |
| PCB                                    | Custom printed circuit board                 | 1        | 30.84            |
| Tax                                    | Sales tax                                   | —        | 8.65             |
| Shipping                               | Shipping costs                              | —        | 8.72             |
|                                        |                                              |          | **Total: $123.97** |
