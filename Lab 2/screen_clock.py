import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Initialize the buttons on the screen
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


yScroll = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    #draw hour bar
    draw.text((0, 0 + yScroll), 'HH:', font=font, fill = (0, 0, 255))
    draw.rectangle((36, 0 + yScroll, 36 + 9*hour, 20 + yScroll), outline=1, fill=(0, 0, 255))
    draw.text((40, 0 + yScroll), str(hour), font=font, fill = (0,0,0))
    
    #draw minute bar
    draw.text((0, (21 + yScroll)%135), 'MM:', font=font, fill = (0, 255, 0))
    draw.rectangle((36, (21 + yScroll)%135, 36 + int(3.4*minute), 40 + yScroll), outline=1, fill=(0, 255, 0))
    draw.text((40, (21 + yScroll)%135), str(minute), font=font, fill = (0,0,0))
    
    #draw second bar
    draw.text((0, (41 + yScroll)%135), 'SS:', font=font, fill = (255, 0, 0))
    draw.rectangle((36, (41 + yScroll)%135, 36 + int(3.4*second), 60 + yScroll), outline=1, fill=(255, 0, 0))
    draw.text((40, (41 + yScroll)%135), str(second), font=font, fill = (0,0,0))

    #Message
    draw.text((0, (65 + yScroll)%135), 'Use your time wisely!', font=font, fill = (255, 255, 255))
    draw.text((0, (85 + yScroll)%135), 'It never stops', font=font, fill = (255, 255, 255))
    
     #interaction
    if buttonB.value and not buttonA.value: # just button A pressed - backgrounds
        if int(time.strftime("%H")) < 6 or int(time.strftime("%H")) >= 18:
            image = Image.open("nighttime.jpg")
        else:
            image = Image.open("daytime.jpg")
        
    if buttonA.value and not buttonB.value: # just button B pressed - quotes
        b = 0
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        if b % 3 == 0:
            text = draw.text((33, (0 + yScroll)%135), 'Quote of the day', font=font, fill = (255, 255, 255))
            text = draw.text((0, (40 + yScroll)%135), 'Lost time is never found', font=font, fill = (255, 255, 255))
            text = draw.text((0, (60 + yScroll)%135), 'again.', font=font, fill = (255, 255, 255))
            text = draw.text((0, (80 + yScroll)%135), ' - Benjamin Franklin', font=font, fill = (255, 255,255))
        elif b % 3 == 1:
            text = draw.text((0, (50 + yScroll)%135), 'Quote 2', font=font, fill = (255, 255, 255))
        else:
            text = draw.text((0, (50 + yScroll)%135), 'Quote 3', font=font, fill = (255, 255, 255))
        b += 1
    
    # Display image.
    disp.image(image, rotation)
    time.sleep(0.05)
