from gpiozero import LED,Button
import random
from time import sleep
import time
led = LED(3)
button = Button(27)
rt = []
for n in range (1, 11):
    sleep (random.randint (1, 5))
    start_time = time.time()
    led.on()
    button.wait_for_press()
    led.off()
    elapsed_time = time.time() - start_time
    rt.append (elapsed_time)

avg = sum (rt) / len (rt)
print (avg)


