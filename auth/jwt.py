import os

from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import timedelta
from dotenv import load_dotenv
from exceptions.error import InvalidUserException

load_dotenv()
HASH_ACCESS = os.environ.get("HASH_ACCESS")
USER_ADMIN = os.environ.get("USER_ADMIN")


def create_token(user_id, hash):
    if HASH_ACCESS != hash or USER_ADMIN != user_id:
        raise InvalidUserException
    return create_access_token(expires_delta=timedelta(minutes=15), identity=user_id)

def verify_user():
    current_user = get_jwt_identity()
    print(current_user)
