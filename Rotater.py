import rotatescreen
import time
screen = rotatescreen.get_primary_display() 
for i in range(49):
    time.sleep(0.25)
    screen.rotate_to(i*90 % 360)
