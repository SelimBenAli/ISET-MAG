var types = [];
var marques = [];

function trouver_hardware_reclamation() {
    var numero_inventaire = document.getElementById("numero_inventaire").value;
    window.location.href = "/client/reclamation/" + numero_inventaire;
}

function envoyer_reclamation() {
    var description = document.getElementById("description").value;
    var reclamation_btn = document.getElementById("reclamation-btn");
    reclamation_btn.disabled = true;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/user/add-reclamation', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                //reclamation_btn.disabled = false;
                openPageHistoriqueReclamationClient();
            } else {
                reclamation_btn.disabled = false;
                alert('Erreur lors de l\'envoi de la réclamation');
            }
        }
    };
    xhr.send(JSON.stringify({description: description}));
}

function load_hardware_model_list() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/user/hardware-model-list', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                types = response.types;
                marques = response.marques;
                load_marques();
            } else {
                alert('Erreur lors du chargement des modèles');
            }
        }
    };
    xhr.send();
}

function check_data_changed() {
    date_debut = document.getElementById("date_debut").value;
    date_fin = document.getElementById("date_fin").value;
    select_type = document.getElementById("select-type").value;
    quantite = document.getElementById("quantite").value;
    if (date_debut !== "" && date_fin !== "" && select_type !== "" && quantite !== "" && quantite > 0) {
        envoyer_location()
    }
}

function envoyer_location() {
    date_debut = document.getElementById("date_debut").value;
    date_fin = document.getElementById("date_fin").value;
    select_type = document.getElementById("select-type").value;
    select_marque = document.getElementById("select-marque").value;
    quantite = document.getElementById("quantite").value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/user/add-location', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                openPageHistoriqueLocationClient()
            } else {
                alert("Erreur lors de l'envoi de la location");
            }
        }
    };
    xhr.send(JSON.stringify({
        date_debut: date_debut,
        date_fin: date_fin,
        id_modele: select_type,
        id_marque: select_marque,
        quantite: quantite
    }));
}

function check_quantity() {
    enter_loading_mode()
    date_debut = document.getElementById("date_debut").value;
    date_fin = document.getElementById("date_fin").value;
    select_type = document.getElementById("select-type").value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/user/check-quantity', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                if (response.quantity > 0) {
                    document.getElementById("affichage-quantite").value = `Quantité disponible : ${response.quantity}`;
                    document.getElementById("affichage-quantite").style.color = "green";
                } else {
                    document.getElementById("affichage-quantite").value = 'Quantité insuffisante';
                    document.getElementById("affichage-quantite").style.color = "red";
                }
                quit_loading_mode()
            } else {
                quit_loading_mode()
                alert('Erreur !');
            }
        }
    };
    xhr.send(JSON.stringify({date_debut: date_debut, date_fin: date_fin, id_modele: select_type}));
}


function load_types() {
    var select_type = document.getElementById("select-type");
    select_type.innerHTML = "";
    types.forEach(function (type) {
        if (type.marque_modele.id_marque === parseInt(document.getElementById("select-marque").value)) {
            select_type.innerHTML += `<option value="${type.id_modele}">${type.nom_modele}</option>`;
        }
    })
}

function load_marques() {
    var select_marque = document.getElementById("select-marque");
    select_marque.innerHTML = "";
    marques.forEach(function (marque) {
        select_marque.innerHTML += `<option value="${marque.id_marque}">${marque.nom_marque}</option>`;
    })
    load_types()
}

function envoyer_message() {
    var sujet = document.getElementById("sujet").value;
    var message = document.getElementById("message").value;
    var contact_btn = document.getElementById("contact-btn");
    contact_btn.disabled = true;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/user/send-message', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                contact_btn.disabled = false;
                openPageHistoriqueReclamationClient()
            } else {
                contact_btn.disabled = false;
                alert('Erreur lors de l\'envoi du message');
            }
        }
    };
    xhr.send(JSON.stringify({sujet: sujet, message: message}));
}

function envoyer_fermeture_reclamation(idr) {
    var message = document.getElementById("comment").value;

    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/user/fermer-reclamation/' + idr, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                openPageReclamationActiveClient()
            } else {
                alert('Erreur');
            }
        }
    };
    xhr.send(JSON.stringify({message: message}));
}

function load_client_alerts() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/message/client-alerts', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                var alerts = response.alerts;
                var alert_list = document.getElementById("client-alert-number");
                alert_list.innerHTML = alerts + "+";
                if (alerts === 0 || alerts === "0") {
                    alert_list.hidden = true;
                }
                else {
                    alert_list.hidden = false;
                }
            } else {
                alert('Erreur lors du chargement des alertes');
            }
        }
    };
    xhr.send();
}

function show_client_reclamation(reclamation) {
    var reclamation_list = document.getElementById("client-reclamation-list");
    reclamation_list.innerHTML += `
    
    <div class="col" data-aos="fade-up" data-aos-once="true" id="reclamation-bloc-${reclamation.id_reclamation}">
                    <div class="card border-0 h-100">
                        <div class="card-body d-flex flex-column justify-content-between p-4">
                            <div>
                                <h6 class="fw-bold text-muted">${reclamation.date_reclamation}</h6>
                                <h4 class="display-5 fw-bold mb-4">${reclamation.hardware_reclamation.modele_hardware.nom_modele} ${reclamation.hardware_reclamation.modele_hardware.marque_modele.nom_marque}</h4>
                                <h5 class="display-5 fw-bold mb-4">${reclamation.hardware_reclamation.numero_inventaire_hardware} </h5>

                                <ul class="list-unstyled">
                                    <li class="d-flex mb-2">
                                        <span>Salle : ${reclamation.hardware_reclamation.salle_hardware.nom_salle} .</span>
                                    </li>
                                    <li class="d-flex mb-2">
                                        <span>Par : ${reclamation.utilisateur_reclamation.nom_utilisateur} ${reclamation.utilisateur_reclamation.prenom_utilisateur} .</span>
                                    </li>
                                    <li class="d-flex mb-2">
                                        <span>Description : ${reclamation.description_reclamation} .</span>
                                    </li>

                                </ul>
                            </div>
                            <button class="btn btn-primary" role="button" onclick="openPageFermerReclamationClient('${reclamation.id_reclamation}')">Terminer Cette Réclamation.
                            </button>
                            <!--<button class="btn btn-warning" style="margin-top: 10px;" role="button" onclick="">Réclamation Fausse.</button>-->
                            <hr>
                        </div>
                    </div>
                </div>
    
    `
}

function delete_client_reclamation(idr) {
    d = document.getElementById("reclamation-bloc-" + idr);
    d.style.display = "none";
}


var socket = io();
socket.on('desactivate_client_account_by_id', function (data) {
    user_element = document.querySelector('clientdata').textContent;
    user_element = user_element.replaceAll("\'", "\"");
    user_data = JSON.parse(user_element);
    if (data.id_utilisateur === user_data.id_utilisateur) {
        console.log("closed session 5 : ", "ok")
        console.log("closed session : ", data)
        alert("Session Fermé par l'administrateur")
        window.location.href = "/auth/logout";
    }
});

socket.on('desactivate_all_client_accounts', function (data) {
    alert("Session Fermé par l'administrateur")
    window.location.href = "/auth/logout";
})