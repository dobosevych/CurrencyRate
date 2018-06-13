from structures.currency import Currency
import time
from datetime import datetime
import logging

logging.basicConfig(filename='info.log',level=logging.INFO)
next_time = "09:00"
curr = Currency("USD")
delay = 60

while True:
    str_time = datetime.now().strftime("%H:%M")
    if str_time == next_time:
        avg = curr.average
        if avg is None:
            logging.ERROR("An error occured")
            if next_time == "09:00":
                next_time = "09:30"
            else:
                next_time = "09:00"
        else:
            logging.INFO("Successfully parsed")
    print(str_time)

    # TODO: This delay could be optimized
    time.sleep(delay)
