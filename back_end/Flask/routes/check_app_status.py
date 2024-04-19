"""Check App Status"""
from shared_function.send_response import create_response
from flask_restful import Resource

class AppStatus(Resource):
    """To get the app status"""

    def get(self):
        """cheking api is up or not"""
        return create_response(message="Application is up", code=200, status=True)
