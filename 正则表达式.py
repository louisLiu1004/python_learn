__author__ = '財'

import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')

final = p.search('2018-05-10').groups()

print(final)

