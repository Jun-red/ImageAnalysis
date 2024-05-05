import sys


def format_time(hours, minutes, seconds):
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
def seconds_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return format_time(hours, minutes, seconds)

