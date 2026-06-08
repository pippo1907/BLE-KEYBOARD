# ESP32 Custom Macro Keyboard (Wired & WiFi)

This repository contains the Python receiver scripts used with a custom-built ESP32 Macro Keyboard developed during a PCB Design Workshop at Delhi Technological University (DTU).

The project allows an ESP32-based macro pad to trigger desktop automation tasks on a computer through either a USB Serial connection (wired mode) or WiFi communication (wireless mode).

---

## Project Overview

The macro keyboard consists of:

* ESP32 Microcontroller
* Custom Designed PCB
* Tactile Push Buttons
* Python Receiver Scripts

When a button is pressed on the macro pad, the ESP32 sends a command to the computer. The corresponding Python script receives the command and executes a predefined desktop action.

---

## Repository Structure

```text
.
├── wire.py          # USB Serial receiver
├── wifi.py          # WiFi UDP receiver
├── README.md        # Project documentation
```

### wire.py

Wired communication implementation.

This script communicates with the ESP32 through a USB Serial connection.

Workflow:

ESP32 → USB Cable → COM Port → Python Script → Desktop Action

Features:

* Reads commands from the configured serial port
* Executes desktop automation tasks
* Requires a physical USB connection

Default Configuration:

* COM Port: COM6
* Baud Rate: 115200

---

### wifi.py

Wireless communication implementation.

This script listens for UDP packets sent by the ESP32 over a WiFi network.

Workflow:

ESP32 → WiFi Network → UDP Packet → Python Script → Desktop Action

Features:

* Wireless operation
* No USB cable required after deployment
* Uses UDP communication on Port 1234

Default Configuration:

* UDP Port: 1234
* Host Address: 0.0.0.0

---

## Available Macros

The following actions are currently mapped to the macro keyboard buttons:

| Button | Function       | Description                                                      |
| ------ | -------------- | ---------------------------------------------------------------- |
| 1      | Screenshot     | Captures and saves a screenshot with timestamp                   |
| 2      | Split Screen   | Snaps current window to the left side and selects another window |
| 3      | Quick Checkout | Opens Blinkit checkout page in the default browser               |
| 4      | Show Desktop   | Executes Windows + D to minimize all windows                     |

---

## Prerequisites

Install Python 3.x and the required dependencies:

```bash
pip install keyboard pyautogui plyer pyserial
```

---

## Usage

### Wired Mode (USB Serial)

1. Connect the ESP32 to the computer using a USB cable.
2. Verify the correct COM port from Device Manager.
3. Update the COM port in `wire.py` if required.
4. Run:

```bash
python wire.py
```

5. Press any button on the macro keyboard to trigger the assigned macro.

---

### Wireless Mode (WiFi)

1. Connect the ESP32 and computer to the same WiFi network.
2. Configure the ESP32 to send UDP packets to the computer's IP address.
3. Ensure the packets are sent to Port 1234.
4. Run:

```bash
python wifi.py
```

5. Press any button on the macro keyboard to trigger the assigned macro.

---

## Hardware Used

* ESP32 Development Board
* Custom PCB
* Tactile Push Buttons
* USB Connection (for wired mode)

---

## Skills & Technologies

* PCB Design
* PCB Fabrication
* Soldering
* Embedded Systems
* ESP32 Programming
* Python Automation
* Serial Communication
* UDP Networking
* Desktop Automation

---

## Future Improvements

* Custom key remapping
* GUI configuration utility
* Additional macro profiles
* Media control shortcuts
* Application-specific shortcuts
* Cross-platform support

---

## Acknowledgments

This project was developed during the PCB Design Workshop conducted at Delhi Technological University (DTU). The workshop provided hands-on experience in PCB design, fabrication, soldering, embedded programming, and hardware-software integration.
