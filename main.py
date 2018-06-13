from structures.currency import Currency
import schedule

import time

def job():
    curr = Currency("USD")
    print(curr.average)

schedule.every().day.at("9:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

