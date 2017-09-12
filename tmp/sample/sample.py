import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('got event{}'.format(event))
    logger.error('something went wrong!')
    return 'Hello, first lambda func!'
