from flask import Blueprint, request, jsonify, url_for
from service.hardware_service import HardwareService
from service.relation_service import RelationService
from tools.user_tools import UserTools


class HardwareViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.hardware_service = HardwareService()
        self.relation_service = RelationService()
        self.hardware_bp = Blueprint('hardware', __name__, template_folder='templates')
        self.hardware_routes()

    def hardware_routes(self):
        @self.hardware_bp.route('/add-hardware', methods=['POST'])
        def add_hardware():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_modele = data.get('modele_hardware')
                id_fournisseur = data.get('fournisseur_hardware')
                id_magasin = data.get('magasin_hardware')
                id_salle = data.get('salle_hardware')
                num_inventaire = data.get('numero_inventaire_hardware')
                date_achat = data.get('date_achat_hardware')
                date_mise_en_service = data.get('date_mise_en_service_hardware')
                code_hardware = data.get('code_hardware')
                id_etat = data.get('etat_hardware')
                if id_modele is None:
                    return jsonify({'status': 'failed', 'message': 'modele is required'})
                if id_fournisseur is None:
                    return jsonify({'status': 'failed', 'message': 'fournisseur is required'})
                if id_magasin is None and id_salle is None:
                    return jsonify({'status': 'failed', 'message': 'magasin or salle is required'})
                if num_inventaire is None:
                    return jsonify({'status': 'failed', 'message': 'numero inventaire is required'})
                if id_etat is None:
                    return jsonify({'status': 'failed', 'message': 'etat is required'})
                if date_achat is None or date_achat == '':
                    date_achat = ' NULL '
                if date_mise_en_service is None or date_mise_en_service == '':
                    date_mise_en_service = ' NULL '
                if id_salle == 0 or id_salle == '0':
                    id_salle = ' NULL '
                if id_magasin == 0 or id_magasin == '0':
                    id_magasin = ' NULL '
                status = self.hardware_service.add_hardware(id_modele, id_fournisseur, id_magasin, id_salle,
                                                            num_inventaire,
                                                            date_achat, date_mise_en_service, code_hardware, id_etat,
                                                            None
                                                            )

                if status != 'failed' and status[0] != 'failed' and status != 'error' and status[0] != 'error':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'error'}

        @self.hardware_bp.route('/update-hardware/<int:id_hardware>', methods=['PUT'])
        def update_hardware(id_hardware):
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_modele = data.get('modele_hardware')
                id_fournisseur = data.get('fournisseur_hardware')
                id_magasin = data.get('magasin_hardware')
                id_salle = data.get('salle_hardware')
                num_inventaire = data.get('numero_inventaire_hardware')
                date_achat = data.get('date_achat_hardware')
                date_mise_en_service = data.get('date_mise_en_service_hardware')
                code_hardware = data.get('code_hardware')
                id_etat = data.get('etat_hardware')

                if id_modele is None:
                    return jsonify({'status': 'failed', 'message': 'modele is required'})
                if id_fournisseur is None:
                    return jsonify({'status': 'failed', 'message': 'fournisseur is required'})
                if id_magasin is None and id_salle is None:
                    return jsonify({'status': 'failed', 'message': 'magasin or salle is required'})
                if num_inventaire is None:
                    return jsonify({'status': 'failed', 'message': 'numero inventaire is required'})
                if id_etat is None:
                    return jsonify({'status': 'failed', 'message': 'etat is required'})
                if date_achat is None or date_achat == '':
                    date_achat = ' NULL '
                if date_mise_en_service is None or date_mise_en_service == '':
                    date_mise_en_service = ' NULL '
                if id_salle == 0 or id_salle == '0':
                    id_salle = ' NULL '
                if id_magasin == 0 or id_magasin == '0':
                    id_magasin = ' NULL '
                status = self.hardware_service.update_hardware(id_hardware, id_modele, id_fournisseur, id_magasin,
                                                               id_salle,
                                                               num_inventaire,
                                                               date_achat, date_mise_en_service, code_hardware, id_etat,
                                                               None
                                                               )
                if status != 'failed' and status[0] != 'failed' and status != 'error' and status[0] != 'error':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'error'}

        @self.hardware_bp.route('/delete-hardware/<int:id_hardware>', methods=['DELETE'])
        def delete_hardware(id_hardware):
            if self.user_tools.check_user_in_session('admin'):
                status = self.hardware_service.delete_hardware(id_hardware)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.hardware_bp.route('/get-hardwares', methods=['GET'])
        def get_hardwares():
            if self.user_tools.check_user_in_session('admin'):
                status, hardwares = self.hardware_service.find_all_hardware()
                return jsonify({'status': 'success', 'hardwares': hardwares})
            return {'status': 'failed'}

        @self.hardware_bp.route('/add-hardware-link/<int:id_hardware>', methods=['PUT'])
        def add_hardware_link(id_hardware):
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_hardware2 = data.get('id_hardware2')
                status, hw2 = self.hardware_service.find_hardware_by_code(id_hardware2)
                if status != 'success':
                    return {'status': 'failed', 'message': 'hardware non trouvé'}
                status, hw1 = self.hardware_service.find_hardware_by_id(id_hardware)
                if status != 'success':
                    return {'status': 'failed', 'message': 'hardware non trouvé'}
                id_hardware2 = hw2[0]['id_hardware']
                if id_hardware2 in hw1[0]['historique_relation_hardware']:
                    return {'status': 'failed', 'message': 'hardware déjà lié'}
                status = self.relation_service.add_relation(id_hardware, id_hardware2)
                if status != 'failed':
                    status, hardwares = self.hardware_service.find_all_hardware()
                    return jsonify({'status': 'success', 'hardwares': hardwares})
            return {'status': 'failed'}

        @self.hardware_bp.route('/delete-hardware-link/<int:id_hardware>', methods=['PUT'])
        def delete_hardware_link(id_hardware):
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_hardware2 = data.get('id_hardware2')
                status, hw2 = self.hardware_service.find_hardware_by_code(id_hardware2)
                if status != 'success':
                    return {'status': 'failed', 'message': 'hardware non trouvé'}
                status, hw1 = self.hardware_service.find_hardware_by_id(id_hardware)
                if status != 'success':
                    return {'status': 'failed', 'message': 'hardware non trouvé'}
                id_hardware2 = hw2[0]['id_hardware']
                if id_hardware2 not in hw1[0]['historique_relation_hardware']:
                    return {'status': 'failed', 'message': 'hardware non lié'}
                status = self.relation_service.delete_relation(id_hardware, id_hardware2)
                if status != 'failed':
                    status, hardwares = self.hardware_service.find_all_hardware()
                    return jsonify({'status': 'success', 'hardwares': hardwares})
            return {'status': 'failed'}
