import logging

class GenLoger:
    @staticmethod
    def gen_loger():
        logger = logging.getLogger('Test Automation')
        fh = logging.FileHandler('../logs/automation.log')
        fm = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
        fh.setFormatter(fm)
        fh.setLevel(logging.INFO)
        logger.addHandler(fh)
        return logger

if __name__ == '__main__':
    logger = GenLoger.gen_loger()
    logger.error(msg='kkrtotrkhorkohktoprkoty')