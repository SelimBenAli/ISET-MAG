from flask import Blueprint, url_for, redirect, render_template, session

from service.hardware_service import HardwareService
from service.intervention_service import InterventionService
from service.location_service import LocationService
from service.reclamation_service import ReclamationService
from service.utilisateur_service import UtilisateurService
from tools.user_tools import UserTools


class ClientViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.client_service = UtilisateurService()
        self.intervention_service = InterventionService()
        self.hardware_service = HardwareService()
        self.reclamation_service = ReclamationService()
        self.location_service = LocationService()
        self.client_bp = Blueprint('client', __name__, template_folder='templates')
        self.client_routes()

    def client_routes(self):
        @self.client_bp.route('/contact', methods=['GET'])
        def contact_client():
            if self.user_tools.check_user_in_session('user'):
                return render_template('client/contacts.html')
            return redirect(url_for('auth.login'))

        @self.client_bp.route('/location', methods=['GET'])
        def location_client():
            if self.user_tools.check_user_in_session('user'):
                return render_template('client/location.html')
            return redirect(url_for('auth.login'))

        @self.client_bp.route('/reclamation/<string:numero_inventaire_hardware>', methods=['GET'])
        def reclamation_client(numero_inventaire_hardware):
            if self.user_tools.check_user_in_session('user'):
                new = False
                if numero_inventaire_hardware is not None and numero_inventaire_hardware != "":
                    if numero_inventaire_hardware == 'new':
                        new = True
                    status, hardware = self.hardware_service.find_hardware_by_numero_inventaire(
                        numero_inventaire_hardware)
                    if status == 'success' and hardware is not None and hardware != []:
                        print(hardware)
                        session['hardware_reclamation'] = hardware[0]
                        return render_template('client/reclamation.html', hardware=hardware[0], new=True)
                return render_template('client/reclamation.html', hardware=None, new=new)
            return redirect(url_for('auth.login'))

        @self.client_bp.route('/historique-materielle', methods=['GET'])
        def historique_materielle_client():
            if self.user_tools.check_user_in_session('user'):
                user = session['user']
                print(user)
                status, interventions = self.intervention_service.find_intervention_by_user(user['id_utilisateur'])
                if status != 'success':
                    return render_template('client/404.html')
                print(interventions)
                return render_template('client/historique-materielle.html', liste_interventions=interventions)
            return redirect(url_for('auth.login'))

        @self.client_bp.route('/historique-reclamation', methods=['GET'])
        def historique_reclamation_client():
            if self.user_tools.check_user_in_session('user'):
                user = session['user']
                status, reclamations = self.reclamation_service.find_reclamation_by_id_utilisateur(
                    user['id_utilisateur'])
                if status != 'success':
                    return render_template('client/404.html')
                print(reclamations)
                return render_template('client/historique-reclamation.html', liste_reclamations=reclamations)
            return redirect(url_for('auth.login'))

        @self.client_bp.route('/historique-location', methods=['GET'])
        def historique_location_client():
            if self.user_tools.check_user_in_session('user'):
                user = session['user']
                status, locations = self.location_service.find_location_by_utilisateur(user['id_utilisateur'])
                if status != 'success':
                    return render_template('client/404.html')
                print(locations)
                return render_template('client/historique-location.html', liste_locations=locations)
            return redirect(url_for('auth.login'))
