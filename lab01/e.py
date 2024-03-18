import sys
from utils import get_status_code

def write_200():
    for line in sys.stdin:
        if get_status_code(line) == "200":
            sys.stdout.write(line)

if __name__ == "__main__":
    write_200()