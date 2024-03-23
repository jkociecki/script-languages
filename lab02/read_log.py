import re
import sys
from datetime import datetime

from sort_log import *
from dicts import *
from filters import *


def read_log() -> list[tuple]:
    pattern = r'^(\S+) - - \[([\w:/]+ [+\-]\d{4})\] "(.*?)" (\d{3}) (\d+|-)$'
    date_pattern = "%d/%b/%Y:%H:%M:%S %z"
    lines = []
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            ip, date, req, code, bytes = match.groups()
            date_obj = datetime.strptime(date, date_pattern)
            bytes = int(bytes) if bytes != "-" else None
            lines.append( (ip, date_obj, req, int(code), bytes) )
    return lines


if __name__ == "__main__":
    logs = read_log()
    
    a = log_to_dict(logs)

    print_dict_entry_dates(a)