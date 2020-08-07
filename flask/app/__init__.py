from flask import Flask
from flasgger import Swagger

app = Flask(__name__)

from app import views