from flask import Blueprint, jsonify, session
from service.message_service import MessageService
from tools.user_tools import UserTools


class MessageViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.message_service = MessageService()
        self.message_bp = Blueprint('message', __name__, template_folder='templates')
        self.message_routes()

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
