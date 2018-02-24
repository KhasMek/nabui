import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    BETTERCAP_URL = os.environ.get('BETTERCAP_URL') or 'https://localhost:8083'
    BETTERCAP_USERNAME = os.environ.get('BETTERCAP_USERNAME') or 'bcap'
    BETTERCAP_PASSWORD = os.environ.get('BETTERCAP_PASSWORD') or 'bcap'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bettercap.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
