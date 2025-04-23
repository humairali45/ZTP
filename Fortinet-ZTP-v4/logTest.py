
import time
import logging
import os

timestr = time.strftime("%Y%m%d_%H%M%S")
print("current directory ...")
print(">>>>",os.path.dirname(__file__))

logFilename = "process_Log_{}.log".format(timestr)
logfilepath= os.path.join(os.path.dirname(__file__), "process_logs\\", logFilename)
print(logfilepath)
            
logging.basicConfig(filename=logfilepath, level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

print("done!") 