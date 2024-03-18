import sys
from utils import get_date, to_datetime_object
import datetime


def friday_requests():
    for line in sys.stdin:
        date = to_datetime_object(get_date(line))
        if date.weekday() == 4:
            sys.stdout.write(line)

if __name__ == "__main__":
    friday_requests()
