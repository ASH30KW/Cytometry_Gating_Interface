from flask_restx import Api

from .cytometrygating import api as cytometrygating_namespace

api = Api(
    title='Plugin cytometrygating API',
    version='1.0',
    description='A simple TodoMVC API',
)

api.add_namespace(cytometrygating_namespace)