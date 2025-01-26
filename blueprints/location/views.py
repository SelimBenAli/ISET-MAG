from flask import Blueprint, jsonify, session

from service.location_service import LocationService
from tools.user_tools import UserTools


class LocationViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.location_service = LocationService()
        self.location_bp = Blueprint('location', __name__, template_folder='templates')
        self.location_routes()

    def location_routes(self):
        @self.location_bp.route('/confirmer-location/<int:id_location>', methods=['PUT'])
        def confirm_location(id_location):
            if self.user_tools.check_user_in_session('admin'):
                admin = session['admin']
                status = self.location_service.confirm_location(1, id_location, admin['id_admin'])
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.location_bp.route('/refuser-location/<int:id_location>', methods=['PUT'])
        def refuse_location(id_location):
            if self.user_tools.check_user_in_session('admin'):
                admin = session['admin']
                status = self.location_service.confirm_location(-1, id_location, admin['id_admin'])
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.location_bp.route('/delete-location/<int:id_location>', methods=['DELETE'])
        def delete_location(id_location):
            if self.user_tools.check_user_in_session('admin'):
                status = self.location_service.delete_location(id_location)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.location_bp.route('/get-locations', methods=['GET'])
        def get_locations():
            if self.user_tools.check_user_in_session('admin'):
                status, locations = self.location_service.find_all_location()
                print(locations)
                return jsonify({'status': 'success', 'locations': locations})
            return {'status': 'failed'}
