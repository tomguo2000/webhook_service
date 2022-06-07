from flask import Flask
import logging

def create_app() -> Flask:

    app = Flask(__name__)

    app.config['LOGFILE_NAME'] = 'webhook_service'
    app.config['LOG_LEVEL'] = logging.DEBUG

    # init logger
    from app.utils.setLogger import init_logger
    init_logger(LOG_basename=app.config.get('LOGFILE_NAME')+'.log', Log_level=app.config.get('LOG_LEVEL'))

    return app
