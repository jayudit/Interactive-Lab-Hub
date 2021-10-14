import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import board
import busio
import adafruit_apds9960.apds9960
import time
import qwiic_button
import sys
import digitalio
import qwiic_joystick
import os
from vosk import Model, KaldiRecognizer
import wave
import json
import shlex
from subprocess import Popen, call


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

# Display the image
disp.image(image, rotation)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Initialize the buttons on the screen
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


# proximity sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True

# joystick
joystick = qwiic_joystick.QwiicJoystick()
joystick.begin()

def handle_speak(val):
    subprocess.run(["sh","GoogleTTS_demo.sh",val])
    
def check_userinput():
    os.system('arecord -D hw:3,0 -f cd -c1 -r 48000 -d 10 -t wav recorded_mono.wav')
    wf = wave.open("recorded_mono.wav", "rb")

    model = Model("model")
    rec = KaldiRecognizer(model, wf.getframerate(), "brown red green yellow usa canada russia mercury mars earth venus zero oh one two three four five six seven eight nine [unk]")
    
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    d = json.loads(rec.FinalResult())
    print("player answered", d["text"])
    return d


question1 = 0
question2 = 0
question3 = 0
d = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    prox = sensor.proximity
    if d == 0:
        welcome_image = Image.open("welcome.png")
        welcome_image = welcome_image.convert('RGB')
        welcome_image = welcome_image.resize((width, height), Image.BICUBIC)
        disp.image(welcome_image, rotation)
        handle_speak("Welcome to Millionaire! To become a millionaire, answer the three questions correctly. Use the joystick to go through the questions. Good luck!")

    if joystick.get_horizontal() > 510:
        if question1 == 0:
            question_image = Image.open("question1.PNG")
            question_image = question_image.convert('RGB')
            question_image = question_image.resize((width, height), Image.BICUBIC)
            disp.image(question_image, rotation)
            handle_speak("Question 1. What is the rarest M and M candy color? You have ten seconds to answer!")
            
            d = check_userinput()
            if("brown" in d["text"]):
                question1 = 1
                num = 3 - (question1+question2+question3)
                handle_speak("Correct Answer! Move the joystick around to go to the next question!")
                question_image = Image.open("question1correct.PNG")
                question_image = question_image.convert('RGB')
                question_image = question_image.resize((width, height), Image.BICUBIC)
                disp.image(question_image, rotation)
            else:
                handle_speak("Wrong Answer! You get one more try! Push the joystick up to try again")
        else:
            question_image = Image.open("question1correct.PNG")
            question_image = question_image.convert('RGB')
            question_image = question_image.resize((width, height), Image.BICUBIC)
            disp.image(question_image, rotation)
            handle_speak("You just won ten thousand dollars!")  
        
    if joystick.get_vertical() < 450:
        if question2 == 0:
            question_image = Image.open("question2.PNG")
            question_image = question_image.convert('RGB')
            question_image = question_image.resize((width, height), Image.BICUBIC)
            disp.image(question_image, rotation)
            handle_speak("Question 2. What country has the most natural lakes? You have ten seconds to answer!")

            d = check_userinput()
            if("canada" in d["text"]):
                question2 = 1
                num = 3 - (question1+question2+question3)
                handle_speak("Correct Answer! Move the joystick around to go to the next question!")
                question_image = Image.open("question2correct.PNG")
                question_image = question_image.convert('RGB')
                question_image = question_image.resize((width, height), Image.BICUBIC)
                disp.image(question_image, rotation)
            else:
                handle_speak("Wrong Answer! You get one more try! Push the joystick left to try again")
        else:
            question_image = Image.open("question2correct.PNG")
            question_image = question_image.convert('RGB')
            question_image = question_image.resize((width, height), Image.BICUBIC)
            disp.image(question_image, rotation)
            handle_speak("You just won hundred thousand dollars!")
            

    if joystick.get_horizontal() < 100:
        if question3 == 0:
            question_image = Image.open("question3.PNG")
            question_image = question_image.convert('RGB')
            question_image = question_image.resize((width, height), Image.BICUBIC)
            disp.image(question_image, rotation)
            handle_speak("Question 3. What is the nearest planet to the sun? You have ten seconds to answer!")

            d = check_userinput()
            if("mercury" in d["text"]):
                question3 = 1
                num = 4 - (question1+question2+question3)
                handle_speak("Correct Answer!")
                question_image = Image.open("question3correct.PNG")
                question_image = question_image.convert('RGB')
                question_image = question_image.resize((width, height), Image.BICUBIC)
                disp.image(question_image, rotation)
            else:
                handle_speak("Wrong Answer! You get one more try! Push the joystick down to try again")
        else:
            question_image = Image.open("question3correct.PNG")
            question_image = question_image.convert('RGB')
            question_image = question_image.resize((width, height), Image.BICUBIC)
            disp.image(question_image, rotation)
            handle_speak("You just won a million dollars!")
            
    if question1 and question2 and question3:
        welcome_image = Image.open("congrats.PNG")
        welcome_image = welcome_image.convert('RGB')
        welcome_image = welcome_image.resize((width, height), Image.BICUBIC)
        disp.image(welcome_image, rotation)
        handle_speak("Congratulations! You are now a millionaire.")
        break

    time.sleep(0.5)    

while True:
    welcome_image = Image.open("congrats.PNG")
    welcome_image = welcome_image.convert('RGB')
    welcome_image = welcome_image.resize((width, height), Image.BICUBIC)
    disp.image(welcome_image, rotation)

