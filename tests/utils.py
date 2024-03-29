import json

from flask import Response
from werkzeug.utils import cached_property


class JSONResponse(Response):

    @cached_property
    def json(self):
        return json.loads(self.get_data(as_text=True))

    @cached_property
    def bad_args(self):
        return self.status_code == 400

    @cached_property
    def ok(self):
        return self.status_code in {200, 201}
