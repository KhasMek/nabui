import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    BETTERCAP_URL = os.environ.get('BETTERCAP_URL') or 'https://localhost:8083'
    BETTERCAP_USERNAME = os.environ.get('BETTERCAP_USERNAME') or 'bcap'
    BETTERCAP_PASSWORD = os.environ.get('BETTERCAP_PASSWORD') or 'bcap'
    BETTERCAP_SESSION = os.environ.get('BETTERCAP_SESSION') or None
    NABUI_POLL_RATE = os.environ.get('NABUI_POLL_RATE') or 20
    SQLALCHEMY_DATABASE_URI = os.environ.get('NABUI_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bettercap.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
