from datetime import datetime
from getters import *


def to_datetime_object(date):
    date_format = "%d/%b/%Y:%H:%M:%S"
    try:
        date_ob = datetime.strptime(date, date_format)
        return date_ob
    except(ValueError, AttributeError):
        return None

def get_host_domain(line):
    try:
       path = get_host(line)
       return path.split('.')[-1]
    except(IndexError):
        return None
    

def sum_data():
    total_data = 0
    for line in sys.stdin:
        data = get_bytes(line)
        if get_request(line) == "GET" and data.isdigit():
            total_data += int(get_bytes(line))
    return total_data


def count_codes(code):
    counter = 0
    for line in sys.stdin:
        if get_status_code(line) == code:
            counter += 1
    return counter


def biggest_resource():
    max = 0
    path = ""
    for line in sys.stdin:
        bytes = get_bytes(line)
        if bytes.isdigit() and int(bytes) > max:
            max = int(bytes)
            path = get_path(line)
    return (path, max)


def extensions_ratio():
    extensions = { "gif" : 0, "jpg" : 0, "jpeg" : 0, "xbm" : 0 }
    rest = 0
    for line in sys.stdin:
        extension = get_path(line).split('.')[-1]
        if extension in extensions:
            extensions[extension] += 1
        else:
            rest += 1
    return (extensions, rest)


def is_beetween(date, start, end):
    if date:
        if start <= date.hour or date.hour < end or (date.hour == end and date.minute == 0 and date.second == 0):
            return True
        else:
            return False
