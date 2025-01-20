from flask_cors import CORS
from flask import Flask

from blueprints.admin import admin_bp
from blueprints.auth import auth_bp
from blueprints.client import client_bp
from blueprints.dashboard import dashboard_bp
from blueprints.fournisseur import fournisseur_bp
from blueprints.hardware import hardware_bp
from blueprints.intervention import intervention_bp
from blueprints.magasin import magasin_bp
from blueprints.marque import marque_bp
from blueprints.modele import modele_bp
from blueprints.salle_bloc import salle_bloc_bp

app = Flask(__name__)
CORS(app)
app.secret_key = 'secret_key'

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(fournisseur_bp, url_prefix='/fournisseur')
app.register_blueprint(salle_bloc_bp, url_prefix='/salle-bloc')
app.register_blueprint(marque_bp, url_prefix='/marque')
app.register_blueprint(modele_bp, url_prefix='/modele')
app.register_blueprint(magasin_bp, url_prefix='/magasin')
app.register_blueprint(hardware_bp, url_prefix='/hardware')
app.register_blueprint(intervention_bp, url_prefix='/intervention')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(client_bp, url_prefix='/client')

if __name__ == '__main__':
    app.run()
