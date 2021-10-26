import time
import board
import busio
import adafruit_mpr121
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
import random
import sys
import digitalio

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
disp = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

draw.text((0.5, 10), " <--- START GAME", font=font_small, fill="#FFFFFF")
draw.text((0.5, 105), "<--- QUIT GAME", font=font_small, fill="#FFFFFF")
disp.image(image, rotation)


# lets define the game logic

def game():
    countdown = 3
    while countdown > 0:
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        draw.text((5, 1), "Ready, set, go!", font=font, fill="#FFFF00")
        draw.text((110, 60), str(countdown), font=font, fill="#FFFF00")
        disp.image(image, rotation)
        countdown -= 1
        time.sleep(1)


    i2c = busio.I2C(board.SCL, board.SDA)

    mpr121 = adafruit_mpr121.MPR121(i2c)

    player1_range = range(0, 3)
    player2_range = range(8, 11)

    number_match = {
        3: ("#FFFFFF", "PAD 1"),
        2: ("#1E90FF", "PAD 2"),
        1: ("#228B22", "PAD 3"),
        0: ("#DC143C", "PAD 4"),
        8: ("#FFFFFF", "PAD 1"),
        9: ("#1E90FF", "PAD 2"),
        10: ("#228B22", "PAD 3"),
        11: ("#DC143C", "PAD 4"),
    }

    player1_error = player2_error = 0
    max_error = 16

    interval = 1.5
    count = 0

    while player1_error < max_error and player2_error < max_error:
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        curr_key = random.randint(0, 3)
        draw.rectangle((60, 30, 80, 80), outline=0, fill=number_match[curr_key][0])
        draw.text((110, 30), number_match[curr_key][1], font=font, fill="#FFFFFF")

        draw.text((0.5, 90), "P1 Strikes", font=font_small, fill="#FFFFFF")
        draw.text((0.5, 110), "X"*int(player1_error/5), font=font_small, fill="#FFFFFF")
        draw.text((140, 90), "P2 Strikes", font=font_small, fill="#FFFFFF")
        draw.text((200, 110), "X"*int(player2_error/5), font=font_small, fill="#FFFFFF")

        disp.image(image, rotation)

        curr_time = time.time()

        player1_firstkey = player2_firstkey = None

        while time.time() - curr_time < interval:
            for i in range(12):
                if mpr121[i].value:
                    if i < 4 and player1_firstkey is None:
                        player1_firstkey = i
                    if i > 7 and player2_firstkey is None:
                        player2_firstkey = i

        if player1_firstkey is None or player1_firstkey != curr_key:
            player1_error += 1
        if player2_firstkey is None or player2_firstkey != 11-curr_key:
            player2_error += 1

        if count > 25:
            interval = 0.5
        elif count > 20:
            interval = 0.75
        elif count > 15:
            interval = 1
        elif count > 10:
            interval = 1.25

        count += 1

    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    if player1_error < player2_error:
        draw.text((10, 45), "Player 1 WINS!", font=font, fill="#FFFFFF")
    elif player2_error < player1_error:
        draw.text((10, 45), "Player 2 WINS!", font=font, fill="#FFFFFF")
    else:
        draw.text((60, 50), "GAME TIED", font=font_small, fill="#FFFFFF")

    draw.text((1, 1), "<--- RESTART GAME", font=font_small, fill="#FFFFFF")
    draw.text((1, 105), "<--- QUIT GAME", font=font_small, fill="#FFFFFF")
    disp.image(image, rotation)
    
while True:
    if buttonB.value and not buttonA.value:
        game()
    if buttonA.value and not buttonB.value:
        sys.exit()