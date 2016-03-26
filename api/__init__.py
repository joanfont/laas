from flask import Flask
from api.modules.songs import blueprint as songs_blueprint

app = Flask(__name__)
app.register_blueprint(songs_blueprint)
