import requests
import threading
import time

from app import app
from app.bettercap import get_session


@app.before_first_request
def activate_job():
    def session_polling():
        while True:
            time.sleep(app.config['NABUI_POLL_RATE'])
            app.config['BETTERCAP_SESSION'] = get_session()

    thread = threading.Thread(target=session_polling)
    thread.start()


def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            try:
                r = requests.get('http://127.0.0.1:5000/')
                if r.status_code == 200:
                    print('Server started')
                    print('Polling session information from Bettercap...')
                    app.config['BETTERCAP_SESSION'] = get_session()
                    not_started = False
                print(r.status_code)
            except requests.exceptions.ConnectionError:
                print('Server not started, sleeping...')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()


if __name__ == '__main__':
    start_runner()
    app.run()