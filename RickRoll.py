"""Ensure you have hid libraries and micropython 
firmware installed on your peco2"""

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Initialize the keyboard
kbd = Keyboard(usb_hid.devices)

# Wait for the OS to recognize the Pico as a keyboard
time.sleep(2)

# Open a new browser tab (universal keystrokes)
kbd.press(Keycode.CONTROL, Keycode.T)  # Windows/Linux
kbd.release_all()
time.sleep(0.5)

# Type the Rickroll URL
rickroll_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
for char in rickroll_url:
    kbd.send(getattr(Keycode, f"KEY_{char.upper()}" if char.isalpha() else f"KEYPAD_{char}"))
    time.sleep(0.1)

# Press Enter
kbd.send(Keycode.ENTER)
kbd.release_all()
