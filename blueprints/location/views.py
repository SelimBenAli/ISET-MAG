from flask import Blueprint, jsonify, session

from service.location_service import LocationService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class LocationViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.location_service = LocationService()
        self.location_bp = Blueprint('location', __name__, template_folder='templates')
        self.location_routes()

    def location_routes(self):
        @self.location_bp.route('/confirmer-location/<int:id_location>', methods=['PUT'])
        def confirm_location(id_location):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_location]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                admin = session['admin']
                status, reservation = self.location_service.find_location_by_id(id_location)
                if status == 'failed' or reservation is None or len(reservation) == 0:
                    return {'status': 'failed', 'message': 'Réservartion non trouvée'}
                if reservation[0]['confirmation_location'] != 0 and reservation[0]['confirmation_location'] != '0':
                    return {'status': 'failed', 'message': 'Réservation déjà répondu'}
                status = self.location_service.confirm_location(1, id_location, admin['id_admin'])
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'Erreur'}

        @self.location_bp.route('/refuser-location/<int:id_location>', methods=['PUT'])
        def refuse_location(id_location):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_location]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                admin = session['admin']
                status, reservation = self.location_service.find_location_by_id(id_location)
                if status == 'failed' or reservation is None or len(reservation) == 0:
                    return {'status': 'failed', 'message': 'Location not found'}
                if reservation[0]['confirmation_location'] != 0 and reservation[0]['confirmation_location'] != '0':
                    return {'status': 'failed', 'message': 'Réserver déjà répondu'}
                status = self.location_service.confirm_location(-1, id_location, admin['id_admin'])
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.location_bp.route('/delete-location/<int:id_location>', methods=['DELETE'])
        def delete_location(id_location):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_location]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.location_service.delete_location(id_location)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.location_bp.route('/get-locations', methods=['GET'])
        def get_locations():
            if self.user_tools.check_user_in_session('admin'):
                status, locations = self.location_service.find_all_location()

                return jsonify({'status': 'success', 'locations': locations})
            return {'status': 'failed'}


if __name__ == '__main__':
    pass
