from flask_restx import Api
from flask import Blueprint

from .todos.endpoints import ns as ns_todos

# Create Api blueprint object with API prefix
api_bp = Blueprint("api", __name__, url_prefix="/api/")

# Init API object in api_bp
api = Api(
    api_bp,
    title="API title", 
    version="v1.0", 
    description="A simple API example",
)

# Add namespace todos in API
api.add_namespace(ns_todos)