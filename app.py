from flask_cors import CORS
from flask import Flask, url_for, redirect, session

# Import Blueprints
from blueprints.admin import admin_bp
from blueprints.auth import auth_bp
from blueprints.client import client_bp
from blueprints.dashboard import dashboard_bp
from blueprints.fournisseur import fournisseur_bp
from blueprints.hardware import hardware_bp
from blueprints.intervention import intervention_bp
from blueprints.location import location_bp
from blueprints.magasin import magasin_bp
from blueprints.marque import marque_bp
from blueprints.message import message_bp
from blueprints.modele import modele_bp
from blueprints.reclamation import reclamation_bp
from blueprints.salle_bloc import salle_bloc_bp
from blueprints.user import user_bp
from blueprints.parametre import parametre_bp

app = Flask(__name__)
CORS(app)
app.secret_key = 'selim_ben_ali'


# Define your session-related functions
def current_scan_ending():
    if 'scan_ending' not in session or session['scan_ending'] is None:
        session['scan_ending'] = 'Enter'
        return 'Enter'
    return session['scan_ending']


def current_scan_mode():
    # mode 1: open, mode 2: close
    if 'scan_mode' not in session or session['scan_mode'] is None:
        session['scan_mode'] = 1
        return 1
    return session['scan_mode']


# Register functions as Jinja globals
app.jinja_env.globals['current_scan_ending'] = current_scan_ending
app.jinja_env.globals['current_scan_mode'] = current_scan_mode

# Register Blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(fournisseur_bp, url_prefix='/fournisseur')
app.register_blueprint(salle_bloc_bp, url_prefix='/salle-bloc')
app.register_blueprint(marque_bp, url_prefix='/marque')
app.register_blueprint(modele_bp, url_prefix='/modele')
app.register_blueprint(magasin_bp, url_prefix='/magasin')
app.register_blueprint(hardware_bp, url_prefix='/hardware')
app.register_blueprint(intervention_bp, url_prefix='/intervention')
app.register_blueprint(reclamation_bp, url_prefix='/reclamation')
app.register_blueprint(location_bp, url_prefix='/location')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(client_bp, url_prefix='/client')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(message_bp, url_prefix='/message')
app.register_blueprint(parametre_bp, url_prefix='/parameter')


# Define routes
@app.route('/')
def index_client():
    return redirect(url_for('auth.login'))


@app.route('/admin')
def index_admin():
    return redirect(url_for('dashboard.reclamation_template'))


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
