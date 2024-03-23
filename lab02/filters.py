def get_entries_by_addr(logs: list[tuple], address: str) -> list[tuple]:
    return list(filter(lambda log: log[0] == address, logs))

def get_entries_by_code(logs: list[tuple], code: int) -> list[tuple]:
    return list(filter(lambda log: log[3] == code, logs))

def get_failed_reads(logs: list[tuple], param: int) -> list[tuple]:
    # param = 1 -> 4xx codes 
    # param = 2 -> 5xx codes
    # param = 3 -> combined
    if param == 1:
        return list(filter(lambda log: 400 <= log[3] < 500, logs))
    elif param == 2:
        return list(filter(lambda log: 500 <= log[3] < 600, logs))
    elif param == 3:
        return list(filter(lambda log: 400 <= log[3] < 600, logs))

def get_entries_by_extension(logs: list[tuple], extension: str) -> list[tuple]:
    return list(filter(lambda log: log[2].endswith("." + extension), logs))

def print_entries(logs: list[tuple]):
    for log in logs:
        print(log)
