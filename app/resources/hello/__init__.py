from flask_restx import Resource
from app import api
# Import resources
from .get import get, get_id

hello = api.namespace('hello')


@hello.route('/')
class Hello(Resource):

    def get(self):
        return get(self)


@hello.route('/<int:id>/')
class Hello(Resource):

    def get(self, id):
        return get_id(self, id)
