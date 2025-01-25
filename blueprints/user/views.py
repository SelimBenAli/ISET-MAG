from flask import Blueprint, jsonify, request, session

from service.hardware_service import HardwareService
from service.location_service import LocationService
from service.marque_service import MarqueService
from service.modele_service import ModeleService
from service.reclamation_service import ReclamationService
from service.utilisateur_service import UtilisateurService
from tools.user_tools import UserTools


class UserViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.user_service = UtilisateurService()
        self.reclamation_service = ReclamationService()
        self.hardware_service = HardwareService()
        self.modele_service = ModeleService()
        self.marque_service = MarqueService()
        self.location_service = LocationService()
        self.user_bp = Blueprint('user', __name__, template_folder='templates')
        self.user_routes()

    def user_routes(self):
        @self.user_bp.route('/add-reclamation', methods=['POST'])
        def add_reclamation():
            if self.user_tools.check_user_in_session('user'):
                data = request.get_json()
                description = data.get('description')
                user = session['user']
                hardware = session['hardware_reclamation']
                description = description.replace('"', "'")
                status = self.reclamation_service.add_reclamation(hardware['id_hardware'],
                                                                  user['id_utilisateur'], 'NULL',
                                                                  description)
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/hardware-model-list', methods=['GET'])
        def hardware_model_list():
            if self.user_tools.check_user_in_session('user'):
                status, modele_list = self.modele_service.find_all_modele()
                status, marque_list = self.marque_service.find_all_marque()
                print(modele_list, marque_list)
                return jsonify({'status': 'success', 'types': modele_list, 'marques': marque_list})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/add-location', methods=['POST'])
        def add_location():
            if self.user_tools.check_user_in_session('user'):
                data = request.get_json()
                date_debut = data.get('date_debut')
                date_fin = data.get('date_fin')
                id_modele = data.get('id_modele')
                # id_marque = data.get('id_marque')
                quantite = data.get('quantite')

                status = self.location_service.add_location(date_debut, date_fin, session['user']['id_utilisateur'],
                                                            id_modele, quantite)

                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})
