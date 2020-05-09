from django.shortcuts import render
import logging
import time
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'test_log.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})
logger = logging.getLogger('Test-logging')



def my_logger(func1):
    def wrapper(*args,**kwargs):
         logging.info('started running the file')
         return func1(*args,**kwargs)
    return wrapper

def my_timer(func1):
    def wrapper(*args,**kwargs):
              t1=time.time()
              result=func1(*args,**kwargs)
              t2=time.time()-t1
              logging.info("Done running:{}".format(func1.__name__))    
              logging.info('{} ran in{} sec'.format(func1.__name__,t2))
              return result
           


    return wrapper

@my_logger
@my_timer
def index(request):
 return render(request,'temp_inheritance/index.html')

    
@my_logger
@my_timer
def others(request):
    try:
     return render(request,'temp_inheritance/others.html')
    except Exception as eyea:
        logging.exception ("no such templates are found")
@my_logger
@my_timer
def base(request):
    return render(request,'temp_inheritance/base.html')
    