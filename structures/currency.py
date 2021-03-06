from datetime import datetime, timedelta
import time
import requests
from pathlib import Path
import json
import logging


class Currency:
    def __init__(self, symbol, filename="data.json"):
        self.symbol = symbol
        self.filename = Path(filename)

    def retrieve(self, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        timestamp = time.time()
        try:
            r = requests.get("https://free.currencyconverterapi.com/api/v5/convert?q=GBP_{}&date={}".format(self.symbol, date))
            data = r.json()
            value = data["results"]["GBP_USD"]["val"][date]
            return date, timestamp, value
        # TODO: Correct exceptions should be listed
        except Exception as e:
            return date, timestamp, None

    def save(self, new_data={}):
        data = {}
        if self.filename.exists():
            data = json.load(open(self.filename))

        data.update(new_data)
        with open(self.filename, "w+") as file:
            file.write(json.dumps(data))

    @property
    def average(self):
        """
        Compute average exchange rate
        :return:
        """
        date = datetime.now()
        delta = timedelta(days=1)

        data = {}
        if self.filename.exists():
            data = json.load(open(self.filename))


        result = 0
        num = 30

        for i in range(num):
            str_date = date.strftime("%Y-%m-%d")

            if str_date not in data:
                this_date, this_timestamp, this_value = self.retrieve(date=str_date)

                # If some error happened
                if this_value is None:
                    return None

                data[this_date] = {"timestamp": this_timestamp, "value": this_value}

            result += data[str_date]["value"]
            date -= delta

        self.save(data)

        return result / num


    def __str__(self):
        return self.symbol

if __name__ == "__main__":
    curr = Currency("USD", "./data.json")
    print(curr.average)