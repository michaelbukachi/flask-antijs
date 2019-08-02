import pytest
from flask import Flask

from flask_antijs import AntiJs


@pytest.fixture(scope='module')
def flask_app():
    app = Flask(__name__)
    AntiJs(app, ignore_payload=False)

    @app.route('/example', methods=['GET', 'POST'])
    def example():
        return 'Ok'

    yield app


def test_ignore_payload__undefined_present(client):
    res = client.get('/example', data={'test': 'undefined'})
    assert res.bad_args


def test_ignore_payload__undefined_present__json(client):
    res = client.get('/example', json={'test': 'undefined'})
    assert res.bad_args
