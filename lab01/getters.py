import sys
from datetime import datetime

def get_host(line):
    try:
        return line.split()[0]
    except(IndexError):
        return ""
    
def get_date(line):
    try:
        return line.split()[3][1:]
    except(IndexError):
        return ""
    
def get_path(line):
    try:
        return line.split()[6]
    except(IndexError):
        return ""
    
def get_status_code(line):
    try:
        return line.split()[-2]
    except(IndexError):
        return ""
    
def get_request(line):
    try:
        return line.split()[5][1:]
    except(IndexError):
        return ""
    
def get_bytes(line):
    try:
        return line.split()[-1]
    except(IndexError):
        return ""