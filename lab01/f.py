import sys
from datetime import datetime
from utils import get_date, to_datetime_object, is_beetween

def hours_22_6():
    for line in sys.stdin:
        date = to_datetime_object(get_date(line))
        if is_beetween(date, 22, 6):
            sys.stdout.write(line)

if __name__ == "__main__":
    hours_22_6()