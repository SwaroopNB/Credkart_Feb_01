import logging

class log_generator_Class:
    @staticmethod
    def log_gen_method():

        log_file = logging.FileHandler(".\\logs\\Credkart.log")     # log file
        log_formate = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d- %(message)s') # log formate
        log_file.setFormatter(log_formate)  # log file --> log formatter
        logger = logging.getLogger()        # get logger object or u can write--> logger = logging.getLogger("Credkart")
        logger.addHandler(log_file)     # add new log everytime in same log file
        logger.setLevel(logging.INFO)  # level set
        return logger


'''
debug
info
warning
error
critical
'''