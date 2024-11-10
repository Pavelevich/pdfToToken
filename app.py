from flask import Flask
from routes import init_routes
import os

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['TOKEN_FOLDER'] = 'tokens'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['TOKEN_FOLDER'], exist_ok=True)


init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
