import logging

class Loggen:

 @staticmethod
 def log_generator():
    logger= logging.getLogger()
    fhandler=logging.FileHandler("C:\\Users\\karti\\PycharmProjects\\Canvas2.0\\Logs\\Automation.log",mode='a')
    formatter=logging.Formatter("%(asctime)s;%(levelname)s;%(message)s", "%Y-%m-%d %H:%M:%S")
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.INFO)
    return logger
