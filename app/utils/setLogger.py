import logging, os
from logging.handlers import SMTPHandler
from concurrent_log import ConcurrentTimedRotatingFileHandler


logger = logging.getLogger()        # 获取到ROOT


def init_logger(LOG_basename, Log_level=logging.INFO, LOG_path='log/', env='unknown'):


    logger.setLevel(Log_level)  # 设置logger日志等级

    # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:

        # 完整的日志存储文件路径和名称
        if not os.path.exists(LOG_path):
            os.makedirs(LOG_path)

        LOG_FILENAME = os.path.join(LOG_path, LOG_basename)

        # 添加processID到日志文件名
        pid = os.getpid()
        LOG_FILENAME = LOG_FILENAME + '_' + str(pid)

        # 创建两个handler
        fh = logging.handlers.TimedRotatingFileHandler(
        # fh = ConcurrentTimedRotatingFileHandler(
            # LOG_FILENAME, when="D", interval=1, backupCount=90, encoding="utf-8", delay=False, utc=True)
            LOG_FILENAME, when="midnight", interval=1, backupCount=90, encoding="utf-8", delay=False)
        ch = logging.StreamHandler()

        # 设置输出日志格式
        formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                      '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        # 为两个handler指定输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 添加到logger
        logger.addHandler(fh)
        logger.addHandler(ch)

    '''
    # 额外增加一个 Email Handler， ERROR级log直接发邮件出来
    mail_handler = SMTPHandler(
        mailhost=('mail.enovatemotors.com', 587),
        fromaddr='holodata@enovatemotors.com',
        toaddrs=['5452594@qq.com'],
        subject=LOG_basename + ': Error',
        secure=("", ""),
        credentials=('holodata', '@123qwe')
    )
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s"
    ))
    logger.addHandler(mail_handler)
    '''