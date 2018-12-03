import logging
import os
import urllib.parse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('event: %s, context: %s' % (event, context))

    rawUrl = event["pathParameters"]["toUrl"]
    parsedUrl = urllib.parse.unquote(rawUrl)

    logger.info('rawUrl: %s, parsedUrl: %s' % (rawUrl, parsedUrl))

    try:
        return {
            "statusCode": 302,
            "headers": {
                "Location": parsedUrl
            }
        }
    except Exception as e:
        logger.error(e)
        # 適切なエラーページにリダイレクトする
        return {
            "statusCode": 302,
            "headers": {
                "Location": "https://www.google.co.jp" # 仮URL
            }
        }
