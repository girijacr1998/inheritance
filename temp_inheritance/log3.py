import logging

logging.basicConfig(filename='log3.log',filemode='a',level=logging.DEBUG)
logging.debug("This is the debug message")
logging.info("This is info")
logging.warning("This is for warning")
logging.error("This is for error")
logging.critical("This is to be called when the critical situation come")


