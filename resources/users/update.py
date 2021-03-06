from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.user import UserAdapter
import json


class UpdateUserAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(UpdateUserAPI, self).init()

    def post(self, id):
        try:
            data = request.data.decode()
            json_data = json.loads(data)
            json_data['method'] = "post"
            print(json_data)
            bridge = UserAdapter()
            bridge.update(id, json_data)
            items = True
            return make_response(json.dumps(items, indent=4), 200)
        except Exception as e:
            return self.handle_error(e)