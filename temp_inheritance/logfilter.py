import logging
from random import choice

class ContextFilter(logging.Filter):
  
    USERS = ['giri', 'john', 'ranji']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']

    def filter(self, record):

        record.ip = choice(ContextFilter.IPS)
        record.user = choice(ContextFilter.USERS)
        return True

if __name__ == '__main__':
    levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)s %(levelname)s IP: %(ip)s User: %(user)s %(message)s')
    a1 = logging.getLogger('logger1')
    a2 = logging.getLogger('logger2')

    h1=logging.FileHandler('filter1.log',mode='a')
    a1.addHandler(h1)
    h2=logging.FileHandler('filter2.log',mode='a')
    a2.addHandler(h2)
    
                      
    f1=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    h1.setFormatter(f1)
    h2.setFormatter(f1)


    f = ContextFilter()
    a1.addFilter(f)
    a2.addFilter(f)
    a1.debug('A debug message')
    a1.info('An info message with %s', 'some parameters')
    for x in range(5):
        lvl = choice(levels)
        lvlname = logging.getLevelName(lvl)
        a2.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')
    
   
