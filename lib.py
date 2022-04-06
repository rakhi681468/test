import sys
import time

from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


def do_while_loop(keyword):
    count = 0
    max_interval = 300
    interval = 5
    while True:
        other_value = BuiltIn().run_keyword(keyword)
        if other_value == 'Completed':
            break
        else:
            if count * interval > max_interval:
                break
            count += 50

