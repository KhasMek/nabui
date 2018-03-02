import json
import requests

from app import app

username = app.config['BETTERCAP_USERNAME']
password = app.config['BETTERCAP_PASSWORD']
bettercap_url = app.config['BETTERCAP_URL']


# type can be json or text
def get_session(_type='json'):
    url = str('{}/api/session'.format(bettercap_url))
    r = requests.get(
        url,
        auth=(
            username,
            password
        ),
        verify=False
    )
    if _type is 'text':
        return r.text
    return r.json()


def get_events(num=None):
    url = str('{}/api/events'.format(bettercap_url))
    if num:
        url = str('{}/api/events?n={}'.format(bettercap_url, num))
    r = requests.get(
        url,
        auth=(
            username,
            password
        ),
        verify=False
    )
    return r.json()


def run_command(cmd=None):
    if cmd:
        url = str('{}/api/session'.format(bettercap_url))
        cmd = {"cmd": cmd}
        r = requests.post(
            url,
            data=json.dumps(cmd),
            auth=(
                username,
                password
            ),
            verify=False
        )
        return r.json()
    return {'error': 'no command'}
