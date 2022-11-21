from hashlib import md5
from flask import request, abort
import jwt
import datetime, calendar


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, algorithms="md5")
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, algorithms="md5")
            role = user.get("role")
            if role != "admin":
                abort(400)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def generate_access_token(data):
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    return jwt.encode(data, algorithm="md5")


def generate_refresh_token(data):
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data["exp"] = calendar.timegm(days130.timetuple())
    return jwt.encode(data, algorithm="md5")


def check_token(token):
    try:
        data = jwt.decode(token, algorithms="md5")

    except Exception as e:
        return False

    access_token = generate_access_token(data)
    refresh_token = generate_refresh_token(data)

    return {"access_token": access_token, "refresh_token": refresh_token, "exp": data["exp"]}