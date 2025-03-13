from flask import Blueprint, request, jsonify, session

from service.hardware_service import HardwareService
from service.intervention_service import InterventionService
from service.utilisateur_service import UtilisateurService
from tools.user_tools import UserTools


class InterventionViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.intervention_service = InterventionService()
        self.utilisateur_service = UtilisateurService()
        self.hardware_service = HardwareService()
        self.intervention_bp = Blueprint('intervention', __name__, template_folder='templates')
        self.intervention_routes()

    def intervention_routes(self):
        @self.intervention_bp.route('/add-intervention', methods=['POST'])
        def add_intervention():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                code_user = data.get('user')
                code_hardware = data.get('hardware')
                # date_debut = data.get('date_debut')
                # id_salle = data.get('id_salle')
                # if id_salle is None or id_salle == '' or id_salle == 0 or id_salle == '0':
                #     id_salle = ' NULL '
                status, u = self.utilisateur_service.find_utilisateur_by_code_barre(code_user)
                status, h = self.hardware_service.find_hardware_by_code(code_hardware)
                print('User : ', u)
                print('Hardware : ', h)
                if u is not None and h is not None:
                    id_user = u[0]['id_utilisateur']
                    id_hardware = h[0]['id_hardware']
                else:
                    return {'status': 'failed'}
                print('Int ajout : ', id_user, id_hardware)
                status, i = self.intervention_service.find_intervention_by_hardware(id_hardware)
                print('currrrrrr', i)
                if len(i) > 0:
                    return {'status': 'failed', 'message': 'Hardware déjà pris en intervention'}
                id_admin = session['admin']['id_admin']
                status = self.intervention_service.add_intervention(id_user, None, ' NULL ', None,
                                                                    id_hardware, id_admin)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'Erreur de session'}

        @self.intervention_bp.route('/update-intervention/<int:id_intervention>', methods=['PUT'])
        def update_intervention(id_intervention):
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_user = data.get('id_user')
                date_debut = data.get('date_debut')
                id_salle = data.get('id_salle')
                if id_salle is None or id_salle == '' or id_salle == 0 or id_salle == '0':
                    id_salle = ' NULL '
                id_hardware = data.get('id_hardware')
                status = self.intervention_service.update_intervention(id_intervention, id_user, date_debut,
                                                                       id_salle,
                                                                       id_hardware)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.intervention_bp.route('/delete-intervention/<int:id_intervention>', methods=['DELETE'])
        def delete_intervention(id_intervention):
            if self.user_tools.check_user_in_session('admin'):
                status = self.intervention_service.delete_intervention(id_intervention)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions', methods=['GET'])
        def get_interventions():
            if self.user_tools.check_user_in_session('admin'):
                status, interventions = self.intervention_service.find_all_intervention()
                print(interventions)
                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/close-intervention/<int:id_intervention>', methods=['PUT'])
        def close_intervention(id_intervention):
            if self.user_tools.check_user_in_session('admin'):
                status = self.intervention_service.close_intervention(id_intervention)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}
