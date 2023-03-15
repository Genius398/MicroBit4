from microbit import *
import radio
radio.config(group=7)
radio.on()
variation=0
while True:

    if button_a.is_pressed():
        radio.send('low')

    if button_b.is_pressed():
        radio.send('high')
    
