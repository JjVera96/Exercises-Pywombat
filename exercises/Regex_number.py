""" String challenge about checking if a string is a valid number 
Valid numbers are defined as string with every threes digits separated with commaa
and point before the decimal digits.

Valid numbers example
100
0
100.00
13,133,133.00

No valid
13,133,13.00

"""

import re

def StringChallenge(strArr):
  m = re.match(r'^([\d]{1,3},([\d]{3},)*[\d]{3}(\.[\d]+)?)$|^([\d]{1,3}\.[\d]+)$|^([\d]{1,3}')
  return True if m else False

print(StringChallenge(input()))