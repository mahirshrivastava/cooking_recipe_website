"""Create response"""

from flask import jsonify
import datetime

def create_response(
    data: dict = {},
    message: str = "Internal Error",
    code: int = "500",
    status: bool = False,
):
    """create response according to industry standards"""
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    meta_data = len(data)
    response_dict = {
        "data": data,
        "message": message,
        "code": code,
        "status": status,
        "meta": meta_data,
        "time_stamp": time_stamp
    }
    response_data = jsonify(response_dict)
    return response_data

