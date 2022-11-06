from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
lcd = LCD()
def safe_exit (signum,frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("Midoriya Izuku:", 1)
    lcd.text("Dreams can become Reality!", 2)
    time.sleep(1)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()