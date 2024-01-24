#This project is to test regres useages in python

import re


s = "83.149.9.216 - (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36 \n \
83.149.9.216 - (\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36\"";

print(s)
ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
