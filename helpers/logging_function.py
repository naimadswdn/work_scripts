import datetime
import logging
import sys
import os


def create_log_directory(current_directory):
    """
    Function responsible for creating log directory if not exist yet.
    :return:
    """
    # current_directory = os.path.dirname(os.path.abspath(__file__))
    # print(current_directory)
    log_directory = os.path.join(current_directory, r'logs')
    # print(log_directory)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    return log_directory


def logger_function(current_directory):
    """
    Function is creating logger object, which allow to run customized logging -
    it return output both to file and to stdout.
    :param current_directory: directory on which log directory need to be crated.
    :return: logger object
    """
    log_directory = create_log_directory(current_directory)

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # set up logging configuration
    logging.basicConfig(
                        level=logging.INFO,
                        format='%(asctime)s lvl=%(levelname)s : %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[
                            logging.FileHandler(log_directory + r'\log_{}.log'.format(datetime.datetime.today().strftime('%Y-%m-%d'))),
                            logging.StreamHandler(sys.stdout)
                        ])

    logger = logging.getLogger()
    return logger
