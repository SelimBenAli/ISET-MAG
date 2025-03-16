from flask import Blueprint, request, jsonify

from service.bloc_service import BlocService
from service.salle_service import SalleService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class SalleBlocViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.bloc_service = BlocService()
        self.salle_service = SalleService()
        self.salle_bloc_bp = Blueprint('salle_bloc', __name__, template_folder='templates')
        self.salle_bloc_routes()

    def salle_bloc_routes(self):
        @self.salle_bloc_bp.route('/add-bloc', methods=['POST'])
        def add_bloc():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                bloc = data.get('nom_bloc')
                if self.sql_injection_tools.detect_sql_injection([bloc]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.bloc_service.add_bloc(bloc)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/update-bloc', methods=['PUT'])
        def update_bloc():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                bloc_id = data.get('id_bloc')
                bloc_nom = data.get('nom_bloc')
                if self.sql_injection_tools.detect_sql_injection([bloc_id, bloc_nom]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.bloc_service.update_bloc(bloc_id, bloc_nom)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/delete-bloc', methods=['DELETE'])
        def delete_bloc():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                bloc_id = data.get('id_bloc')
                if self.sql_injection_tools.detect_sql_injection([bloc_id]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.bloc_service.delete_bloc(bloc_id)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/get-blocs', methods=['GET'])
        def get_blocs():
            if self.user_tools.check_user_in_session('admin'):
                blocs = self.bloc_service.find_all_bloc()
                return {'status': 'success', 'blocs': blocs}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/add-salle', methods=['POST'])
        def add_salle():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                salle = data.get('nom_salle')
                bloc = data.get('id_bloc')
                if self.sql_injection_tools.detect_sql_injection([salle, bloc]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.salle_service.add_salle(salle, bloc)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/update-salle', methods=['PUT'])
        def update_salle():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                salle_id = data.get('id_salle')
                salle_nom = data.get('nom_salle')
                bloc = data.get('id_bloc')
                if self.sql_injection_tools.detect_sql_injection([salle_id, salle_nom, bloc]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.salle_service.update_salle(salle_id, salle_nom, bloc)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/delete-salle', methods=['DELETE'])
        def delete_salle():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                salle_id = data.get('id_salle')
                if self.sql_injection_tools.detect_sql_injection([salle_id]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.salle_service.delete_salle(salle_id)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/get-salles', methods=['GET'])
        def get_salles():
            if self.user_tools.check_user_in_session('admin'):
                salles = self.salle_service.find_all_salle()
                return {'status': 'success', 'salles': salles}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/get-salles-by-bloc', methods=['GET'])
        def get_salles_by_bloc():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                bloc = data.get('id_bloc')
                if self.sql_injection_tools.detect_sql_injection([bloc]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                salles = self.salle_service.find_salle_by_bloc(bloc)
                return {'status': 'success', 'salles': salles}
            return {'status': 'failed'}

        @self.salle_bloc_bp.route('/get-salle-and-bloc', methods=['GET'])
        def get_salle_and_bloc():
            if self.user_tools.check_user_in_session('admin'):
                status_salles, salles = self.salle_service.find_all_salle()
                status_blocs, blocs = self.bloc_service.find_all_bloc()
                print(salles, blocs)
                return jsonify({'status': 'success', 'salles': salles, 'blocs': blocs})
            return {'status': 'failed'}
