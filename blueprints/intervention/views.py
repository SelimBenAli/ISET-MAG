from flask import Blueprint, request, jsonify, session
from service.intervention_service import InterventionService
from tools.user_tools import UserTools


class InterventionViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.intervention_service = InterventionService()
        self.intervention_bp = Blueprint('intervention', __name__, template_folder='templates')
        self.intervention_routes()

    def intervention_routes(self):
        @self.intervention_bp.route('/add-intervention', methods=['POST'])
        def add_intervention():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_user = data.get('id_user')
                date_debut = data.get('date_debut')
                id_salle = data.get('id_salle')
                if id_salle is None or id_salle == '' or id_salle == 0 or id_salle == '0':
                    id_salle = ' NULL '
                id_hardware = data.get('id_hardware')
                id_admin = session['admin']['IDAdmin']
                status = self.intervention_service.add_intervention(id_user, date_debut, ' NULL ', id_salle,
                                                                    id_hardware, id_admin)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

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
