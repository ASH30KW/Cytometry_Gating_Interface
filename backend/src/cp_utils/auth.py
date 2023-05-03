from flask_restx import Namespace, Resource, fields, reqparse, abort
import functools
from cp_utils import coreAPI

authorizations = {
    'token' : {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Copy & Paste in your API access token. You can get it from the /login endpoint or the top right user menu in CellPhaser."
    }
}

tokenparser = reqparse.RequestParser()
tokenparser = tokenparser.add_argument('Authorization', location='headers')
def withTokenOnly(api, role=None):
    def decorator(func):
        # apply flask decorators
        for dec in [api.doc(security='token'), api.header("Authorization", description="API access token")]:
            func = dec(func)
        # wrapper to check validity of the token
        @functools.wraps(func)
        def wrapper_check_token(*args, **kwargs):
            token = tokenparser.parse_args()["Authorization"]
            coreAS = coreAPI.APIService(token)
            user = coreAS.getSelf()
            if (not token is None) and isinstance(user, dict) and user.get("token",object())==token and (role is None or user.get("role")==role):
                api.current_user = user
                r = func(*args, **kwargs)
                api.current_user = None
                return r
            else:
                return abort(401)
        return wrapper_check_token
    return decorator