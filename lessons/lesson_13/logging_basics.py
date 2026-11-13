import logging # sys.path = []
from logging import DEBUG, INFO

# # Налаштування конфігурації логування - ROOT
logging.basicConfig(level=DEBUG, format='LOGGER:%(name)s: [%(filename)s] - [%(funcName)s] - [line:%(lineno)d] -%(asctime)s - %(levelname)s - %(message)s')

def log_this():
    # Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logging.debug('Це повідомлення рівня DEBUG')
    logging.info('Це повідомлення рівня INFO') #
    logging.warning('Це повідомлення рівня WARNING')
    logging.error('Це повідомлення рівня ERROR')
    logging.critical('Це повідомлення рівня CRITICAL')

log_this()
