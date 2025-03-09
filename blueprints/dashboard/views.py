from flask import Blueprint, render_template, redirect, url_for, session

from service.bloc_service import BlocService
from service.etat_service import EtatService
from service.fournisseur_service import FournisseurService
from service.hardware_service import HardwareService
from service.intervention_service import InterventionService
from service.location_service import LocationService
from service.magasin_service import MagasinService
from service.marque_service import MarqueService
from service.message_service import MessageService
from service.modele_service import ModeleService
from service.parametre_email_service import ParametreEmailService
from service.reclamation_service import ReclamationService
from service.role_service import RoleService
from service.salle_service import SalleService
from service.utilisateur_service import UtilisateurService
from tools.user_tools import UserTools


class DashboardViews:
    def __init__(self):
        self.user_tools = UserTools('dashboard')
        self.fournisseur_service = FournisseurService()
        self.bloc_service = BlocService()
        self.salle_service = SalleService()
        self.marque_service = MarqueService()
        self.modele_service = ModeleService()
        self.magasin_service = MagasinService()
        self.hardware_service = HardwareService()
        self.etat_service = EtatService()
        self.intervention_service = InterventionService()
        self.location_service = LocationService()
        self.message_service = MessageService()
        self.utilisateur_service = UtilisateurService()
        self.role_service = RoleService()
        self.reclamation_service = ReclamationService()
        self.parametre_email_service = ParametreEmailService()
        self.dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates')
        self.dashboard_fournisseur_routes()
        self.dashboard_salle_bloc_routes()
        self.dashboard_marque_routes()
        self.dashboard_modele_routes()
        self.dashboard_magasin_routes()
        self.dashboard_hardware_routes()
        self.dashboard_intervention_routes()
        self.dashboard_location_routes()
        self.dashboard_message_routes()
        self.dashboard_utilisateur_routes()
        self.dashboard_reclamation_routes()
        self.dashboard_profile_routes()

    def dashboard_salle_bloc_routes(self):
        @self.dashboard_bp.route('/salle-bloc', methods=['GET'])
        def salle_bloc_template():
            if self.user_tools.check_user_in_session('admin'):
                status, liste_bloc = self.bloc_service.find_all_bloc()
                return render_template('salle-bloc.html', liste_bloc=liste_bloc, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-salle-bloc', methods=['GET'])
        def ajout_salle_bloc_template():
            if self.user_tools.check_user_in_session('admin'):
                liste_bloc = self.bloc_service.find_all_bloc()[1]
                return render_template('ajout-salle-bloc.html', liste_bloc=liste_bloc, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-bloc/<int:idb>', methods=['GET'])
        def modifier_bloc_template(idb):
            if self.user_tools.check_user_in_session('admin'):
                status, bloc = self.bloc_service.find_bloc_by_id(idb)
                return render_template('modifier-bloc.html', bloc=bloc[0], user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-salle/<int:ids>', methods=['GET'])
        def modifier_salle_template(ids):
            if self.user_tools.check_user_in_session('admin'):
                status, salle = self.salle_service.find_salle_by_id(ids)
                liste_bloc = self.bloc_service.find_all_bloc()[1]
                return render_template('modifier-salle.html', salle=salle[0], liste_bloc=liste_bloc,
                                       user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_fournisseur_routes(self):
        @self.dashboard_bp.route('/fournisseur', methods=['GET'])
        def fournisseur_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('fournisseur.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-fournisseur', methods=['GET'])
        def ajout_fournisseur_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('ajout-fournisseur.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-fournisseur/<int:idf>', methods=['GET'])
        def modifier_fournisseur_template(idf):
            if self.user_tools.check_user_in_session('admin'):
                status, fournisseur = self.fournisseur_service.find_fournisseur_by_id(idf)
                return render_template('modifier-fournisseur.html', fournisseur=fournisseur[0], user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_marque_routes(self):
        @self.dashboard_bp.route('/marque', methods=['GET'])
        def marque_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('marque.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-marque', methods=['GET'])
        def ajout_marque_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('ajout-marque.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-marque/<int:idm>', methods=['GET'])
        def modifier_marque_template(idm):
            if self.user_tools.check_user_in_session('admin'):
                status, marque = self.marque_service.find_marque_by_id(idm)
                return render_template('modifier-marque.html', marque=marque[0], user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_modele_routes(self):
        @self.dashboard_bp.route('/modele', methods=['GET'])
        def modele_template():
            if self.user_tools.check_user_in_session('admin'):
                liste_marque = self.marque_service.find_all_marque()[1]
                return render_template('modele.html', liste_marque=liste_marque, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-modele', methods=['GET'])
        def ajout_modele_template():
            if self.user_tools.check_user_in_session('admin'):
                liste_marque = self.marque_service.find_all_marque()[1]
                return render_template('ajout-modele.html', liste_marque=liste_marque, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-modele/<int:idm>', methods=['GET'])
        def modifier_modele_template(idm):
            if self.user_tools.check_user_in_session('admin'):
                status, modele = self.modele_service.find_modele_by_id(idm)
                liste_marque = self.marque_service.find_all_marque()[1]
                return render_template('modifier-modele.html', modele=modele[0], liste_marque=liste_marque,
                                       user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_magasin_routes(self):
        @self.dashboard_bp.route('/magasin', methods=['GET'])
        def magasin_template():
            if self.user_tools.check_user_in_session('admin'):
                liste_bloc = self.bloc_service.find_all_bloc()[1]
                return render_template('magasin.html', liste_bloc=liste_bloc, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-magasin', methods=['GET'])
        def ajout_magasin_template():
            if self.user_tools.check_user_in_session('admin'):
                liste_salle = self.salle_service.find_all_salle()[1]
                return render_template('ajout-magasin.html', liste_salle=liste_salle, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-magasin/<int:idm>', methods=['GET'])
        def modifier_magasin_template(idm):
            if self.user_tools.check_user_in_session('admin'):
                status, magasin = self.magasin_service.find_magasin_by_id(idm)
                liste_salle = self.salle_service.find_all_salle()[1]
                return render_template('modifier-magasin.html', magasin=magasin[0], liste_salle=liste_salle,
                                       user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_hardware_routes(self):
        @self.dashboard_bp.route('/hardware', methods=['GET'])
        def hardware_template():
            if self.user_tools.check_user_in_session('admin'):
                liste_modele = self.modele_service.find_all_modele()[1]
                liste_fournisseur = self.fournisseur_service.find_all_fournisseur()[1]
                liste_magasin = self.magasin_service.find_all_magasin()[1]
                liste_salle = self.salle_service.find_all_salle()[1]
                liste_etat = self.etat_service.find_all_etat()[1]
                liste_marque = self.marque_service.find_all_marque()[1]
                return render_template('hardware.html', liste_modele=liste_modele, liste_marque=liste_marque,
                                       liste_fournisseur=liste_fournisseur,
                                       liste_magasin=liste_magasin, liste_salle=liste_salle, liste_etat=liste_etat,
                                       user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-hardware', methods=['GET'])
        def ajout_hardware_template():
            if self.user_tools.check_user_in_session('admin'):
                liste_modele = self.modele_service.find_all_modele()[1]
                liste_fournisseur = self.fournisseur_service.find_all_fournisseur()[1]
                liste_magasin = self.magasin_service.find_all_magasin()[1]
                liste_salle = self.salle_service.find_all_salle()[1]
                liste_etat = self.etat_service.find_all_etat()[1]
                return render_template('ajout-hardware.html', liste_modele=liste_modele,
                                       liste_fournisseur=liste_fournisseur,
                                       liste_magasin=liste_magasin, liste_salle=liste_salle, liste_etat=liste_etat,
                                       user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-hardware/<int:idh>', methods=['GET'])
        def modifier_hardware_template(idh):
            if self.user_tools.check_user_in_session('admin'):
                status, hardware = self.hardware_service.find_hardware_by_id(idh)
                liste_modele = self.modele_service.find_all_modele()[1]
                liste_fournisseur = self.fournisseur_service.find_all_fournisseur()[1]
                liste_magasin = self.magasin_service.find_all_magasin()[1]
                liste_salle = self.salle_service.find_all_salle()[1]
                liste_etat = self.etat_service.find_all_etat()[1]
                return render_template('modifier-hardware.html', hardware=hardware[0], liste_modele=liste_modele,
                                       liste_fournisseur=liste_fournisseur, liste_magasin=liste_magasin,
                                       liste_salle=liste_salle, liste_etat=liste_etat, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_intervention_routes(self):
        @self.dashboard_bp.route('/intervention', methods=['GET'])
        def intervention_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('intervention.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        # TO COMPLETE

    def dashboard_location_routes(self):
        @self.dashboard_bp.route('/location', methods=['GET'])
        def location_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('location.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_message_routes(self):
        @self.dashboard_bp.route('/message', methods=['GET'])
        def message_template():
            if self.user_tools.check_user_in_session('admin'):
                user_id = session['admin']['id_admin']
                self.message_service.add_seen_all_message(user_id)
                return render_template('message.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_utilisateur_routes(self):
        @self.dashboard_bp.route('/utilisateur', methods=['GET'])
        def utilisateur_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('utilisateur.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-utilisateur', methods=['GET'])
        def ajout_utilisateur_template():
            if self.user_tools.check_user_in_session('admin'):
                status, role = self.role_service.find_all_role()
                return render_template('ajout-utilisateur.html', liste_role=role, user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/update-utilisateur/<int:idu>', methods=['GET'])
        def modifier_utilisateur_template(idu):
            if self.user_tools.check_user_in_session('admin'):
                status, utilisateur = self.utilisateur_service.find_utilisateur_by_id(idu)
                status, role = self.role_service.find_all_role()
                return render_template('modifier-utilisateur.html', utilisateur=utilisateur[0], liste_role=role,
                                       user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_reclamation_routes(self):
        @self.dashboard_bp.route('/reclamation', methods=['GET'])
        def reclamation_template():
            if self.user_tools.check_user_in_session('admin'):
                self.reclamation_service.add_seen_all_reclamation(session['admin']['id_admin'])
                return render_template('reclamation.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

    def dashboard_profile_routes(self):
        @self.dashboard_bp.route('/profile', methods=['GET'])
        def profile_template():
            if self.user_tools.check_user_in_session('admin'):
                user = session['admin']
                print("99", user)
                return render_template('profile.html', user=user)
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/settings', methods=['GET'])
        def settings_template():
            if self.user_tools.check_user_in_session('admin'):
                user = session['admin']
                parametre_email_add_admin = None  # self.parametre_email_service.find_marametre_add_admin_email()[1][0]
                parametre_email_add_user = None
                parametre_email_forgot_password_user = None
                return render_template('parametre.html', user=user, parametre_email_add_admin=parametre_email_add_admin,
                                       parametre_email_add_user=parametre_email_add_user,
                                       parametre_email_forgot_password_user=parametre_email_forgot_password_user)
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/admin-utilisateur', methods=['GET'])
        def admin_utilisateur_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('admin-utilisateur.html', user=session['admin'])
            else:
                return redirect(url_for('admin.login'))

        @self.dashboard_bp.route('/add-admin', methods=['GET'])
        def ajout_admin_template():
            if self.user_tools.check_user_in_session('admin'):
                return render_template('ajout-admin.html')
            else:
                return redirect(url_for('admin.login'))
