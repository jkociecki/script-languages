

def sort_log(logs, index):
    if  4 < index < 0:
        raise ValueError()

    return sorted(
         logs,
         key=lambda x: x[index]
        )