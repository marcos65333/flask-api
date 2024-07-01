from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



from src.routes.index import *
from src.routes.estudiante import *
