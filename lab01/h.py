import sys
from utils import get_host_domain


def get_polish_requests():
    for line in sys.stdin:
        if get_host_domain(line) == "pl":
            sys.stdout.write(line)


if __name__ == "__main__":
    get_polish_requests()