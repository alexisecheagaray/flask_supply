from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.employee_in_charge import EmployeeInChargeAdapter
import json


class UpdateEmployeeInChargeAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(UpdateEmployeeInChargeAPI, self).init()

    def post(self, id):
        try:
            data = request.data.decode()
            json_data = json.loads(data)
            json_data['method'] = "post"
            print(json_data)
            bridge = EmployeeInChargeAdapter()
            return bridge.update(id, json_data)
        except Exception as e:
            return self.handle_error(e)