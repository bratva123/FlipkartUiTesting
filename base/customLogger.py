import inspect
import logging


def customLogger(loglevel=logging.DEBUG):
    #get the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    #By default , log all message
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("reports_and_log/automation.log", mode='a')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m/%d/%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
