import pytest
from flask import Flask

from flask_antijs import AntiJs


@pytest.fixture(scope='module')
def flask_app():
    app = Flask(__name__)
    AntiJs(app)

    @app.route('/example', methods=['GET', 'POST'])
    def example():
        return 'Ok'

    yield app


def test_ignore_query_params_false__undefined_present(client):
    res = client.get('/example?test=undefined')
    assert res.bad_args
