from flask import Blueprint, jsonify, request, session

from service.hardware_service import HardwareService
from service.location_service import LocationService
from service.marque_service import MarqueService
from service.message_service import MessageService
from service.modele_service import ModeleService
from service.reclamation_service import ReclamationService
from service.utilisateur_service import UtilisateurService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools
# from extensions import socketio


class UserViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.user_service = UtilisateurService()
        self.reclamation_service = ReclamationService()
        self.hardware_service = HardwareService()
        self.modele_service = ModeleService()
        self.marque_service = MarqueService()
        self.location_service = LocationService()
        self.message_service = MessageService()
        self.user_bp = Blueprint('user', __name__, template_folder='templates')
        self.user_routes()

    def user_routes(self):
        @self.user_bp.route('/add-reclamation', methods=['POST'])
        def add_reclamation():
            if self.user_tools.check_user_in_session('user'):
                data = request.get_json()
                description = data.get('description')
                description = description.replace('"', "'")
                if self.sql_injection_tools.detect_sql_injection_in_descriptions([description]):
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                user = session['user']
                hardware = session['hardware_reclamation']
                description = description.replace('"', "'")
                status, id_reclamation = self.reclamation_service.add_reclamation(hardware['id_hardware'],
                                                                                  user['id_utilisateur'], 'NULL',
                                                                                  description)
                if status == 'success':
                    status, r = self.reclamation_service.find_reclamation_by_id(id_reclamation)

                    # socketio.emit('update_admin_alert', {'message': 'success'})
                    # socketio.emit('update_client_alerts', {'message': 'success', 'reclamation': r[0]})
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/hardware-model-list', methods=['GET'])
        def hardware_model_list():
            if self.user_tools.check_user_in_session('user'):
                status, modele_list = self.modele_service.find_all_modele()
                status, marque_list = self.marque_service.find_all_marque()

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
                if self.sql_injection_tools.detect_sql_injection([date_debut, date_fin, id_modele, quantite]):
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                status = self.location_service.add_location(date_debut, date_fin, session['user']['id_utilisateur'],
                                                            id_modele, quantite)

                if status == 'success':
                    # socketio.emit('update_admin_alert', {'message': 'success'})
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/send-message', methods=['POST'])
        def send_message():
            if self.user_tools.check_user_in_session('user'):
                data = request.get_json()
                message = data.get('message')
                sujet = data.get('sujet')
                message = message.replace('"', "'")
                sujet = sujet.replace('"', "'")
                if self.sql_injection_tools.detect_sql_injection_in_descriptions([message, sujet]):
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                user = session['user']
                status = self.message_service.add_message(user['id_utilisateur'], sujet, message)
                if status == 'success':
                    # socketio.emit('update_admin_message', {'message': 'success'})
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/get-utilisateurs', methods=['GET'])
        def get_utilisateurs():
            if self.user_tools.check_user_in_session('admin'):
                status, utilisateurs = self.user_service.find_all_utilisateur()
                return jsonify({'status': 'success', 'utilisateurs': utilisateurs})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/add-utilisateur', methods=['POST'])
        def add_utilisateur():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom_utilisateur')
                prenom = data.get('prenom_utilisateur')
                mail = data.get('email_utilisateur')
                tel = data.get('telephone_utilisateur')
                role = data.get('role_utilisateur')
                code = data.get('code_utilisateur')
                if self.sql_injection_tools.detect_sql_injection([nom, prenom, mail, tel, role, code]):
                    print("1")
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                status, user = self.user_service.find_utilisateur_by_mail(mail)
                if status == 'success' and user != []:
                    print("2")
                    return jsonify({'status': 'failed', 'message': 'email already used'})
                status, user = self.user_service.find_utilisateur_by_code(code)
                if status == 'success' and user != []:
                    print("3")
                    return jsonify({'status': 'failed', 'message': 'code already used'})
                status = self.user_service.add_utilisateur(nom.upper(), prenom.upper(), mail, tel, "", role,
                                                           code.upper())
                if status == 'success':
                    print("4")
                    return jsonify({'status': 'success'})
                print("5")
                return jsonify({'status': 'failed'})
            print("6")
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/delete-utilisateur/<int:id_utilisateur>', methods=['DELETE'])
        def delete_utilisateur(id_utilisateur):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_utilisateur]):
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                status = self.user_service.delete_utilisateur(id_utilisateur)
                if status == 'success':
                    # socketio.emit('desactivate_client_account_by_id',
                    #              {'message': 'success', 'id_utilisateur': id_utilisateur})
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/update-utilisateur/<int:id_utilisateur>', methods=['PUT'])
        def update_utilisateur(id_utilisateur):
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom_utilisateur')
                prenom = data.get('prenom_utilisateur')
                mail = data.get('email_utilisateur')
                tel = data.get('telephone_utilisateur')
                role = data.get('role_utilisateur')
                code = data.get('code_utilisateur')
                if self.sql_injection_tools.detect_sql_injection([id_utilisateur, nom, prenom, mail, tel, role, code]):
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                status = self.user_service.update_utilisateur(id_utilisateur, nom.upper(), prenom.upper(), mail, tel,
                                                              role, code.upper())
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/desactiver-compte/<int:id_utilisateur>', methods=['PUT'])
        def desactiver_compte(id_utilisateur):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_utilisateur]):
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                status = self.user_service.desactiver_compte(id_utilisateur)
                # socketio.emit('desactivate_client_account_by_id',
                #               {'message': 'success', 'id_utilisateur': id_utilisateur})
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/activer-compte/<int:id_utilisateur>', methods=['PUT'])
        def activer_compte(id_utilisateur):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_utilisateur]):
                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                status = self.user_service.activer_compte(id_utilisateur)

                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/activer-tous-compte', methods=['PUT'])
        def activer_tous_compte():
            if self.user_tools.check_user_in_session('admin'):
                status = self.user_service.activer_tous_compte()
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/desactiver-tous-compte', methods=['PUT'])
        def desactiver_tous_compte():
            if self.user_tools.check_user_in_session('admin'):
                status = self.user_service.desactiver_tous_compte()
                # socketio.emit('desactivate_all_client_accounts', {'message': 'success'})
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/fermer-reclamation/<int:idr>', methods=['PUT'])
        def fermer_reclamation(idr):
            if self.user_tools.check_user_in_session('user'):
                data = request.get_json()
                description = data.get('message')
                description = description.replace('"', "'")
                if self.sql_injection_tools.detect_sql_injection_in_descriptions([description]):

                    return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
                technicien = session['user']

                status = self.reclamation_service.finish_reclamation(idr, technicien['id_utilisateur'], description)
                if status == 'success':
                    # socketio.emit('delete_reclamation_alert', {'message': 'success', 'id_reclamation': idr})
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.user_bp.route('/envoyer-email-recuperation', methods=['PUT'])
        def envoyer_email_recuperation():
            data = request.get_json()
            email = data.get('email')
            if self.sql_injection_tools.detect_sql_injection([email]):
                return jsonify({'status': 'failed', 'message': 'Problème de sécurité détecté'})
            status, user = self.user_service.find_utilisateur_by_mail(email)
            if status == 'success' and user != []:
                status = self.user_service.envoyer_email_recuperation(email)
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'error'})
            return jsonify({'status': 'failed', 'message': 'Utilisateur Non Trouvé'})


if __name__ == '__main__':
    pass
