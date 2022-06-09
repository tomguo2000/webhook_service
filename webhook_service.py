from app import create_app
from app.utils.setLogger import logger
from flask import request

application = create_app()

errorLogfileHandle = open('log/errorLogfile.txt', 'a')
infoLogfileHandle = open('log/infoLogfile.txt', 'a')

@application.route('/webhook',  methods=['POST'])
def webhook():
    try:
        infoLogfileHandle.write(f"MESSAGE: {request.data.decode()}")
    except:
        errorLogfileHandle.write(f"MESSAGE: something wrong with write log: {request.data.decode()} \n")
        errorLogfileHandle.flush()

    finally:
        return {'code': 200}


@application.route('/webhook/get', methods=['GET'])
def webhook_get():
    try:
        infoLogfileHandle.write(f"MESSAGE: {request.url}")
    except:
        errorLogfileHandle.write(f"MESSAGE: something wrong with write log: {request.url} \n")
        errorLogfileHandle.flush()

    return {'code': 200}


@application.route('/response_put', methods=['PUT'])
def response_put():
    try:
        logger.info(f"MESSAGE_URL: {request.url}")
        logger.info(f"MESSAGE_FORM_DATA: {request.form}")
        logger.info(f"MESSAGE_BODY: {request.data}")
    except:
        errorLogfileHandle.write("MESSAGE: something wrong with write log \n")
        errorLogfileHandle.flush()

    return {'code': 200}


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5666, use_reloader=False)
