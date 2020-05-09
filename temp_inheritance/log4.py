import logging
import mylib

def first():
    logging.basicConfig(filename='log4.log',level=logging.INFO)
    logging.info('starting')
    mylib.do_add()
    logging.info('finished')

if __name__ == "__main__":
    first()