import sys
from utils import extensions_ratio

def extension_comp():
    extensions, rest = extensions_ratio()

    output = ""
    graph_files = 0
    for key, value in extensions.items():
        output += f"extension: {key}, requests: {value} \n"
        graph_files += value
    output += f"graph/rest ratio = {graph_files / rest}"
    sys.stdout.write(output)
    
if __name__ == "__main__":
    extension_comp()