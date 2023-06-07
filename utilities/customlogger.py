import logging


class LogGen:
    @staticmethod  # дає можливість використовувати обєкт класу як простір імен без привязки до екземпляру класу
    def get_logger():
        logger = logging.getLogger('test application')
        fh = logging.FileHandler("./logs/automation.log")
        fh.setLevel(logging.INFO)
        fm = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s", datefmt="%d:%m:%Y %I/%M/%S %p")
        fh.setFormatter(fm)
        logger.addHandler(fh)
        return logger
