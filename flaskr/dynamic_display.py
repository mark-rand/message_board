# Clock example with NTP synchronization
#
# Create a secrets.py with your Wifi details to be able to get the time
# when the Galactic Unicorn isn't connected to Thonny.
#
# secrets.py should contain:
# WIFI_SSID = "Your WiFi SSID"
# WIFI_PASSWORD = "Your WiFi password"
#
# Clock synchronizes time on start, and resynchronizes if you press the A button

import time
import math
import machine
from network_manager import NetworkManager
import ntptime
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
import uasyncio
import urequests
import gc

def text(text, x, y):
    graphics.set_pen(COLOURS[7])
    graphics.text(text, x, y, -1, 1)

# create galactic object and graphics surface for drawing
gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

# create the rtc object
rtc = machine.RTC()

width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT
utc_offset = 1

# set up some pens to use later
COLOURS = [
    graphics.create_pen(0, 0, 0), # 0, BLACK
    graphics.create_pen(0, 0, 255), # 1, BLUE
    graphics.create_pen(255, 0, 0), # 2, RED
    graphics.create_pen(255, 0, 255), # 3, MAGENTA
    graphics.create_pen(0, 255, 0), # 4, GREEN
    graphics.create_pen(0, 255, 255), # 5, CYAN
    graphics.create_pen(255, 255, 0), # 6, YELLOW
    graphics.create_pen(255, 255, 255), # 7, WHITE
    ]

URL="http://192.168.0.2:5050/"

# set the font
graphics.set_font("bitmap8")
gu.set_brightness(0.25)
text("Initialising...", 0, 2)
gu.update(graphics)

def status_handler(mode, status, ip):
    # reports wifi connection status
    print(mode, status, ip)
    print('Connecting to wifi...')
    if status is not None:
        if status:
            print('Wifi connection successful!')
        else:
            print('Wifi connection failed!')
            text("Wifi Failed")
            gu.update(graphics)
            time.sleep(120)

try:
    from secrets import WIFI_SSID, WIFI_PASSWORD, COUNTRY
    wifi_available = True
    network_manager = NetworkManager(COUNTRY, status_handler=status_handler)
    uasyncio.get_event_loop().run_until_complete(network_manager.client(WIFI_SSID, WIFI_PASSWORD))
except ImportError:
    print("Create secrets.py with your WiFi credentials to get time from NTP")
    wifi_available = False
except Exception as e:
    print(f'Wifi connection failed! {e}')
    wifi_available = False


# Connect to wifi and synchronize the RTC time from NTP
def sync_time():
    try:
        ntptime.settime()
        print("Time set")
    except OSError:
        pass

    
def get_data():
    # open the json file
    try:
        print(f'Requesting URL: {URL}')
        r = urequests.get(URL)
        # open the json data
        j = r.json()
        #print('Data obtained!' + r)
        r.close()
        return j
    except Exception as e:
        print(e)


year, month, day, wd, hour, minute, second, _ = rtc.datetime()

last_second = second

# Check whether the RTC time has changed and if so redraw the display


def display_time():
    global year, month, day, wd, hour, minute, second, last_second

    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    if second != last_second:
        hour = (hour + utc_offset) % 24
        time_through_day = (((hour * 60) + minute) * 60) + second
        percent_through_day = time_through_day / 86400
        percent_to_midday = 1.0 - \
            ((math.cos(percent_through_day * math.pi * 2) + 1) / 2)
        print(percent_to_midday)

        clock = "{:02}:{:02}".format(hour, minute)

        # calculate text position so that it is centred
        w = graphics.measure_text(clock, 1)
        x = int(width / 2 - w / 2 + 1)
        y = 2

        text(clock, x, y)

        last_second = second    

data=None

def display(tick):
    offset=tick % len(data['message'])
    for column in range(0, width):
        column_ref = data['message'][(column + offset) % len(data['message'])]
        column_pixels = str(data['cols'][column_ref])
        for pixel in range(0, height):
            graphics.set_pen(COLOURS[int(column_pixels[pixel])])
            graphics.pixel(column, pixel)
    gu.update(graphics)

mode=0
sync_time()
tick=0
while True:
    print(f"Mem free {gc.mem_free()}")
    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
        gu.adjust_brightness(+0.01)

    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
        gu.adjust_brightness(-0.01)

    if gu.is_pressed(GalacticUnicorn.SWITCH_A):
        sync_time()
    
    graphics.set_pen(COLOURS[0])
    graphics.clear()
    if mode==0:
        display_time()
        gu.update(graphics)
        data=get_data()
        mode=1
        print(int(time.time()))
    elif mode==1 and data != None:
        tick=0
        mode=2
        display(tick)
    elif mode==2 and data != None:
        tick += 1
        display(tick)
    else:
        mode=0
    
    time.sleep(0.01)

