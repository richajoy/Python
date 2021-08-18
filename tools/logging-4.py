import logging.config

logging.config.fileConfig("logging.ini", disable_existing_loggers=False)

log = logging.getLogger(__name__)

log.debug('DEBUG message')
log.info('INFO message')
log.warning('WARNING message')
log.error('ERROR message')
log.critical('CRITICAL message')