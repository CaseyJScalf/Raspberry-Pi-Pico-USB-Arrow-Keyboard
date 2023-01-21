import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP2
btn2_pin = board.GP5
btn3_pin = board.GP10
btn4_pin = board.GP14

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP

while True:
    if not btn1.value:
        print("button 1 pressed")
        keyboard.press(Keycode.LEFT_ARROW)
        led.value = True
        time.sleep(0.08)
        keyboard.release(Keycode.LEFT_ARROW)
        led.value = False
    if not btn2.value:
        print("button 2 pressed")
        keyboard.press(Keycode.UP_ARROW)
        led.value = True
        time.sleep(0.08)
        keyboard.release(Keycode.UP_ARROW)
        led.value = False
    if not btn3.value:
        print("button 3 pressed")
        keyboard.press(Keycode.RIGHT_ARROW)
        led.value = True
        time.sleep(0.08)
        keyboard.release(Keycode.RIGHT_ARROW)
        led.value = False
    if not btn4.value:
        print("button 4 pressed")
        keyboard.press(Keycode.DOWN_ARROW)
        led.value = True
        time.sleep(0.08)
        keyboard.release(Keycode.DOWN_ARROW)
        led.value = False
    time.sleep(0.07)
