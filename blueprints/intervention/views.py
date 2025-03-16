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
                status, i = self.intervention_service.find_intervention_by_used_hardware(id_hardware)
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

        @self.intervention_bp.route('/get-interventions-user-code/<string:code>', methods=['GET'])
        def get_interventions_uc(code):
            if self.user_tools.check_user_in_session('admin'):
                status, user = self.utilisateur_service.find_utilisateur_by_code(code)

                status, interventions = self.intervention_service.find_intervention_by_user(user[0]['id_utilisateur'])
                print(interventions)
                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-hard-code/<string:code>', methods=['GET'])
        def get_interventions_hc(code):
            if self.user_tools.check_user_in_session('admin'):
                status, hard = self.hardware_service.find_hardware_by_code(code)
                status, interventions = self.intervention_service.find_intervention_by_hardware(hard[0]['id_hardware'])
                print(interventions)
                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-hard-num/<string:code>', methods=['GET'])
        def get_interventions_hn(code):
            if self.user_tools.check_user_in_session('admin'):
                status, hard = self.hardware_service.find_hardware_by_numero_inventaire(code)
                status, interventions = self.intervention_service.find_intervention_by_hardware(hard[0]['id_hardware'])
                print(interventions)
                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-closed/<int:page>', methods=['GET'])
        def get_interventions_closed(page):
            if self.user_tools.check_user_in_session('admin'):
                number = 10
                begin = (page - 1) * number
                status, pages = self.intervention_service.find_number_closed_interventions()
                status, interventions = self.intervention_service.find_closed_intervention_with_limit(begin, number)
                if status == 'success':
                    if pages % number != 0:
                        page_number = pages // number + 1
                    else:
                        page_number = pages // number
                    print(interventions)
                    return jsonify(
                        {'status': 'success', 'interventions': interventions, 'pages': page_number,
                         'current_page': page,
                         'nombre_totale': pages})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-current/<int:page>', methods=['GET'])
        def get_interventions_current(page):
            if self.user_tools.check_user_in_session('admin'):
                number = 10
                begin = (page - 1) * number
                status, pages = self.intervention_service.find_number_current_interventions()
                status, interventions = self.intervention_service.find_current_intervention_with_limit(begin, number)
                if status == 'success':
                    if pages % number != 0:
                        page_number = pages // number + 1
                    else:
                        page_number = pages // number
                    print(interventions)
                    return jsonify(
                        {'status': 'success', 'interventions': interventions, 'pages': page_number,
                         'current_page': page,
                         'nombre_totale': pages})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-limit/<int:page>', methods=['GET'])
        def get_interventions_limit(page):
            if self.user_tools.check_user_in_session('admin'):
                number = 10
                begin = (page - 1) * number
                print("err1")
                status, pages = self.intervention_service.find_number_interventions()
                print("err2")
                status, interventions = self.intervention_service.find_all_intervention_with_limit(begin, number)
                print("err3", status, interventions)
                if status == 'success':
                    if pages % number != 0:
                        page_number = pages // number + 1
                    else:
                        page_number = pages // number
                    print(interventions)
                    return jsonify(
                        {'status': 'success', 'interventions': interventions, 'pages': page_number,
                         'current_page': page,
                         'nombre_totale': pages})
            return {'status': 'failed'}

        @self.intervention_bp.route('/close-intervention/<int:id_intervention>', methods=['PUT'])
        def close_intervention(id_intervention):
            if self.user_tools.check_user_in_session('admin'):
                status, i = self.intervention_service.find_intervention_by_id(id_intervention)
                print('Intervention à fermer : ', i)
                if len(i) == 0:
                    return {'status': 'failed', 'message': 'Intervetion introuvable'}
                if i[0]['date_fin_intervention'] is not None:
                    return {'status': 'failed', 'message': 'Intervention déjà fermée'}
                admin = session['admin']['id_admin']
                status = self.intervention_service.close_intervention(id_intervention, admin)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'Erreur de session'}
