import logging
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WAY_JSON = os.path.join(ROOT_DIR, 'user_settings.json')
WAY_EXCEL = os.path.join(ROOT_DIR, 'data', 'operations.xlsx')
WAY_LOG = os.path.join(ROOT_DIR, "logs")
WAY_REPORTS = os.path.join(ROOT_DIR, "reports")


def set_reports(name):
    if not os.path.exists(WAY_REPORTS):
        os.makedirs(WAY_REPORTS)
    return os.path.join(WAY_REPORTS, name)

def modul_log(name):
    if not os.path.exists(WAY_LOG):
        os.makedirs(WAY_LOG)
    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(os.path.join(WAY_LOG, name + ".log"), encoding="utf-8")
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger