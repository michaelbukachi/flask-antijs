import pytest
from flask import Flask

from flask_antijs import AntiJs


@pytest.fixture(scope='session')
def flask_app():
    app = Flask(__name__)
    AntiJs(app, path_variables_only=True)

    @app.route('/<test>', methods=['GET', 'POST'])
    def example(test):
        return test

    yield app


def test_path_variables_only__true__undefined_present(client):
    res = client.get('/undefined')
    assert res.bad_args


def test_path_variables_only__true__undefined_absent(client):
    res = client.get('/hello')
    assert res.ok


def test_path_variables_only__true__undefined_present_in_payload(client):
    res = client.get('/hello', data={'test': 'undefined'})
    assert res.ok


def test_path_variables_only__true__undefined_present_in_query_params(client):
    res = client.get('/hello?test=undefined')
    assert res.ok
