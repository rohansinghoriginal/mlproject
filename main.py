from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging

#test function for exception
def test_exception():
    try:
        logging.info("Here is an error!!!")
        a=1/0
    except Exception as e:
        raise SensorException(e, sys)

# testing exception 
if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)