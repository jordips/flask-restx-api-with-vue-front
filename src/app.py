from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import json

from api import api_bp
from vueui import vue_bp

app = Flask(__name__)

# Register API blueprint
app.register_blueprint(api_bp)

# Register VUE-UI blueprint
app.register_blueprint(vue_bp)
