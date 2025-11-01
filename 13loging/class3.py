# Logging With A Real World Example

import logging as log

log.basicConfig(
    level=log.DEBUG,
    format="%(asctime)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        log.FileHandler("app1.log"),  # Change "app.log" to any file name you want
        log.StreamHandler()
    ]
)

log.getLogger('ArithmaticApp')
def add(a,b):
    result = a+b
    log.debug(f'adding {a} + {b} = {result}')
    return result
def sub(a,b):
    result = a-b
    log.debug(f'substract {a} - {b} = {result}')
    return result
def mult(a,b):
    result = a*b
    log.debug(f'multpling  {a} * {b} = {result}')
    return a*b

def div(a, b):
    result = a / b
    log.debug(f'Dividing\ {a} / {b} = {result}')
    return result

add(1,2)
sub(2,1)
mult(2,2)
try:
    div(3,5)
except ZeroDivisionError:
    log.error('this is a ZeroDivisionError')
add(12,12)
