from flask import Blueprint, jsonify, session

from service.location_service import LocationService
from service.message_service import MessageService
from service.reclamation_service import ReclamationService
from tools.user_tools import UserTools


class MessageViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.message_service = MessageService()
        self.reclamation_service = ReclamationService()
        self.location_service = LocationService()
        self.message_bp = Blueprint('message', __name__, template_folder='templates')
        self.message_routes()
        self.notification_alerte()

    def message_routes(self):
        @self.message_bp.route('/get-messages', methods=['GET'])
        def get_messages():
            if self.user_tools.check_user_in_session('admin'):
                status, messages = self.message_service.find_all_message()
                print(messages)
                return jsonify({'status': 'success', 'messages': messages})
            return {'status': 'failed'}

        @self.message_bp.route('/delete-message/<int:id_message>', methods=['DELETE'])
        def delete_message(id_message):
            if self.user_tools.check_user_in_session('admin'):
                status = self.message_service.delete_message(id_message)
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})

        @self.message_bp.route('/messages-notifications', methods=['GET'])
        def messages_notifications():
            if self.user_tools.check_user_in_session('admin'):
                id_admin = session['admin']['id_admin']
                status, messages = self.message_service.find_message_by_something(
                    ' `Vu` NOT LIKE "%' + str(id_admin) + ';%" ORDER BY `Date` DESC')
                print(messages)
                return jsonify({'status': 'success', 'messages': messages})
            return {'status': 'failed'}

    def notification_alerte(self):
        @self.message_bp.route('/alertes-notifications', methods=['GET'])
        def alertes_notifications():
            if self.user_tools.check_user_in_session('admin'):
                id_admin = session['admin']['id_admin']
                status, reclamations = self.reclamation_service.find_reclamation_by_something(
                    f" `Vu` NOT LIKE '%{id_admin};%' ORDER BY `DateReclamation` DESC LIMIT 0, 6 ")
                status, locations = self.location_service.find_location_by_something(
                    ' Confirmation = 0 ORDER BY `DateAjout` DESC LIMIT 0, 6')
                print("22", reclamations, locations)
                reclamations.sort(key=lambda x: x['date_reclamation'], reverse=True)
                locations.sort(key=lambda x: x['date_ajout_location'], reverse=True)
                alertes = []
                for reclamation in reclamations:
                    alertes.append(
                        {'type': 'reclamation', 'date': reclamation['date_reclamation'], 'reclamation': reclamation})
                for location in locations:
                    alertes.append(
                        {'type': 'location', 'date': location['date_ajout_location'], 'location': location})
                alertes.sort(key=lambda x: x['date'], reverse=True)
                if len(alertes) > 6:
                    alertes = alertes[:6]
                print(alertes)
                return jsonify({'status': 'success', 'alertes': alertes})
            return {'status': 'failed'}
