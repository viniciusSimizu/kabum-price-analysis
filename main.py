from src.config.config import config
from flask import Flask
from flask_cors import CORS
from src.server.routes import create_routes

app = Flask(__name__)
CORS(app)
app.app_context()
app.secret_key = config.get('APP_SV_SECRET')
app.config['JSON_SORT_KEYS'] = False

create_routes(app)

if __name__ == '__main__':
    app.run(port=3000, debug=True, load_dotenv=True)
