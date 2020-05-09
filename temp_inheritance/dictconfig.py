import logging.config
import time
logger = logging.getLogger('test')
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'f1': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'f2': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'h1': {
            'class': 'logging.StreamHandler',
            'formatter': 'f1'
        },
        'h2': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'f2',
            'filename': 'dictconfig.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': [ 'h1','h2']
        }
    }
})


logger.info('hi')
logger.debug('this')
logger.warning('is the example')
logger.error('of dict configuration')
logger.critical('succesfully completed')
