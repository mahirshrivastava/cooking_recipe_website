"""Define URLS here"""
from flask_restful import Api
from routes.check_app_status import AppStatus

def add_urls(api: Api):
    """Add routes for the application"""
    api.add_resource(AppStatus, '/', '/home', '/status')

