import sys
from utils import sum_data

def total_data_sent():
    total_data_gb = sum_data() / (1024 * 1024 * 1024)
    sys.stdout.write(f"Total data sent in GB {total_data_gb:.2f}")

if __name__ == "__main__":
    total_data_sent()