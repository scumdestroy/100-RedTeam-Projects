import stem
import stem.connection
import requests
import sys

def tor_it_up():
    with stem.connection.Controller.from_port() as controller:
        controller.authenticate()
        controller.signal(stem.Signal.NEWNYM)

    session = requests.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

session = tor_it_up()
print(session.get(sys.argv[1]).text)
