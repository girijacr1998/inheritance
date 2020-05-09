import logging

logging.basicConfig(filename='log3.log',filemode='a',level=logging.DEBUG,format= ' %(asctime)s-%(process)s-%(levelname)s-%(message)s',datefmt='%m:%d:%y %I:%M:%S %p')

                                                                                                                                                 
logging.debug("log3-1:This is the debug message")
logging.info("log3-1:This is info")
logging.warning("log3-1:This is for warning")
logging.error("log3-1:This is for error")
logging.critical("log3-1:This is to be called when the critical situation come")


