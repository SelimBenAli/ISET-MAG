from flask import Blueprint, request, jsonify
from service.fournisseur_service import FournisseurService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class FournisseurViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.fournisseur_service = FournisseurService()
        self.sql_injection_tools = SQLInjectionTools()
        self.fournisseur_bp = Blueprint('fournisseur', __name__, template_folder='templates')
        self.fournisseur_routes()

    def fournisseur_routes(self):
        @self.fournisseur_bp.route('/add-fournisseur', methods=['POST'])
        def add_fournisseur():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom')
                tel = data.get('telephone')
                if self.sql_injection_tools.detect_sql_injection([nom, tel]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.fournisseur_service.add_fournisseur(nom, tel)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'Erreur Serveur'}

        @self.fournisseur_bp.route('/update-fournisseur', methods=['PUT'])
        def update_fournisseur():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_fournisseur = data.get('id_fournisseur')
                nom = data.get('nom_fournisseur')
                tel = data.get('telephone_fournisseur')
                if self.sql_injection_tools.detect_sql_injection([id_fournisseur, nom, tel]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                print(id_fournisseur, nom, tel)
                status = self.fournisseur_service.update_fournisseur(id_fournisseur, nom, tel)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.fournisseur_bp.route('/delete-fournisseur', methods=['DELETE'])
        def delete_fournisseur():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_fournisseur = data.get('id_fournisseur')
                if self.sql_injection_tools.detect_sql_injection([id_fournisseur]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.fournisseur_service.delete_fournisseur(id_fournisseur)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.fournisseur_bp.route('/get-fournisseurs', methods=['GET'])
        def get_fournisseurs():
            if self.user_tools.check_user_in_session('admin'):
                status, fournisseurs = self.fournisseur_service.find_all_fournisseur()
                print(fournisseurs)
                return jsonify({'status': 'success', 'fournisseurs': fournisseurs})
            return {'status': 'failed'}

        @self.fournisseur_bp.route('/get-fournisseur', methods=['GET'])
        def get_fournisseur():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_fournisseur = data.get('id_fournisseur')
                if self.sql_injection_tools.detect_sql_injection([id_fournisseur]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status, fournisseur = self.fournisseur_service.find_fournisseur_by_id(id_fournisseur)
                return {'status': 'success', 'fournisseur': fournisseur}
            return {'status': 'failed'}

        @self.fournisseur_bp.route('/get-fournisseur-by-name', methods=['GET'])
        def get_fournisseur_by_name():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom')
                if self.sql_injection_tools.detect_sql_injection([nom]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status, fournisseur = self.fournisseur_service.find_fournisseur_by_nom(nom)
                return {'status': 'success', 'fournisseur': fournisseur}
            return {'status': 'error', 'message': 'Erreur Serveur'}

        @self.fournisseur_bp.route('/get-fournisseur-by-tel', methods=['GET'])
        def get_fournisseur_by_tel():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                tel = data.get('tel')
                if self.sql_injection_tools.detect_sql_injection([tel]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status, fournisseur = self.fournisseur_service.find_fournisseur_by_tel(tel)
                return {'status': 'success', 'fournisseur': fournisseur}
            return {'status': 'error', 'message': 'Erreur Serveur'}
