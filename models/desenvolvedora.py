from flask_restx import fields
from api import api

desenvolvedora = api.model('desenvolvedora', {
    '_id': fields.String(required=False, description='Id da desenvolvedora'),
    'nome': fields.String(required=True, description='Nome da desenvolvedora'),
    'fundacao': fields.Date(required=True, description='Data de fundação da desenvolvedora'),
    'localizacao': fields.String(required=True, description='Localização da desenvolvedora')
}, strict=True)
