import pytest
import data
import requests

@pytest.fixture
def server():
    serv = data.serv_start()
    serv.engine.start()
    serv.engine.wait(serv.engine.states.STARTED)

    yield
    serv.engine.exit()
    serv.engine.block()

def test_r(server):
    print('before request')
    r = requests.get('http://127.0.0.1:8080/api/users')
    assert r.text == 1

def test_ok(server):
    assert "data: [{'username': 'van', 'email': 'vanbyvan@fmail.ru', 'department': 'production', 'date_joined': '2011-11-11T11:10:09'}]" == requests.get('http://127.0.0.1:8080/api/users')