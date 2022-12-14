from flask_restx import fields
from api import api

tag = api.model('tag', {
    '_id': fields.String(required=False, description='Id da noticia'),
    'nome': fields.String(required=True, description='Descrição da tag')
}, strict=True)
