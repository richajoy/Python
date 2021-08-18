import logging

# Create a console handler
consoleHandler = logging.StreamHandler()

# Define a formatter
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(name)-10s: %(message)s')
consoleHandler.setFormatter(formatter)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(consoleHandler)

log.debug('DEBUG message')
log.info('INFO message')
log.warning('WARNING message')
log.error('ERROR message')
log.critical('CRITICAL message')