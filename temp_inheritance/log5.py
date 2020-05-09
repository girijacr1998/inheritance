import logging
import sys

logger=logging.getLogger('logger1')
logger2=logging.getLogger('logger2')
logger.setLevel(logging.DEBUG)

handler1=logging.FileHandler('log5.log',mode='a')
handler1.setLevel(logging.INFO)

handler2=logging.FileHandler('log5-1.log',mode='a')
handler2.setLevel(logging.ERROR)

logger.addHandler(handler1)
logger2.addHandler(handler2)

logger.info("this is the info message")

handler3=logging.StreamHandler(sys.stdout) 
handler3.setLevel(logging.INFO)
logger.addHandler(handler3)

logger.info('to check ')
logger2.critical('A critical message')

formatter=logging.Formatter('%(name)s %(levelname)s %(message)s')
formatter2=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

handler1.setFormatter(formatter)
handler2.setFormatter(formatter2)

logger.info('this entry should be logged in log5.log')
logger.critical('error message')
logger2.error('this entry should be logged in log5-1.log')