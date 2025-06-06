var lien = "http://127.0.0.1:5000/static/";

function login() {

    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email === '' || password === '') {
        alert('Please fill all fields');
        return;
    }
    login_request(email, password)
}

function login_request(email, password) {
    var b = document.getElementById('login-btn');
    b.innerHTML = 'Chargement...';
    b.disabled = true;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/admin/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                window.location.href = "/dashboard/fournisseur";
            } else {
                alert(response.message);
                b.innerHTML = 'Se Connecter';
                b.disabled = false;
            }
        } else {

        }
    };
    xhr.send(JSON.stringify({email: email, password: password}));

}

function change_settings() {
    nom = document.getElementById('nom').value;
    prenom = document.getElementById('prenom').value;
    email = document.getElementById('email').value;
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/admin/change-details', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                openPageReclamation()
            } else {
                alert('Error');
            }
        }
    };
    xhr.send(JSON.stringify({nom: nom, prenom: prenom, email: email}));
}

function load_messages_notifications() {

    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/message/messages-notifications', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                show_messages_notifications(response.messages)
                alert_message_number(response.messages.length)
            }
        }
    };
    xhr.send();
}

function show_messages_notifications(data) {
    div = document.getElementById('messages-notifications-div');
    div.innerHTML = '<h6 class="dropdown-header">Boite de récéption</h6>';
    data.slice(0, 7).forEach(function (message) {
        div.innerHTML += `
        
                        <a class="dropdown-item d-flex align-items-center"
                                                                         href="#">
                        </div>
                        <div class="fw-bold">
                           <div class="text-truncate"><span>${message.sujet_message}</span>
                            </div>
                            <p class="small text-gray-500 mb-0">${message.utilisateur_message.nom_utilisateur} ${message.utilisateur_message.prenom_utilisateur} - ${message.date_message}</p>
                        </div>
                    </a>
                       
        `;
    })
    div.innerHTML += ' <a class="dropdown-item text-center small text-gray-500" onclick="openPageMessage()">Afficher Tous les Messages.</a>'
}

function message_notification_sound() {
    var audio = document.getElementById("sound-message")
    audio.play();
}

function alert_message_number(number) {
    var alert = document.getElementById('alert-message-number');
    if (number === 0) {
        alert.style.display = 'none';
        return;
    }
    alert.style.display = 'block';
    alert.innerHTML = number;
}


function load_alerts_notifications() {

    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/message/alertes-notifications', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.status === 'success') {
                show_alerts_notifications(response.alertes)
                alert_alert_number(response.alertes.length)
            }
        }
    };
    xhr.send();
}


function show_alerts_notifications(data) {
    div = document.getElementById('alerts-notifications-div');
    div.innerHTML = '<h6 class="dropdown-header">Centre des Alertes</h6>';
    data.forEach(function (alert) {
        if (alert.type === 'reclamation') {
            my_reclamation = alert.reclamation
            div.innerHTML += `
                      <a class="dropdown-item d-flex align-items-center" onclick="openPageReclamation()">
                        <div class="me-3">
                            <div class="bg-warning icon-circle"><i class="fas fa-exclamation-triangle text-white"></i></div>
                        </div>
                        <div><span class="small text-gray-500">${my_reclamation.date_reclamation}</span>
                            <p>${my_reclamation.utilisateur_reclamation.nom_utilisateur} ${my_reclamation.utilisateur_reclamation.prenom_utilisateur} ${my_reclamation.hardware_reclamation.salle_hardware.nom_salle}</p>
                        </div>
                    </a>
                       
        `;
        } else {
            my_location = alert.location
            div.innerHTML += `
            <a class="dropdown-item d-flex align-items-center" onclick="openPageLocation()">
                        <div class="me-3">
                            <div class="bg-primary icon-circle"><i class="fas fa-file-alt text-white"></i></div>
                        </div>
                        <div><span class="small text-gray-500">${my_location.date_ajout_location}</span>
                            <p>${my_location.utilisateur_location.nom_utilisateur} ${my_location.utilisateur_location.prenom_utilisateur}</p>
                        </div>
                    </a>
            `;

        }
    })
    div.innerHTML += ' <div class="dropdown-item text-center small text-gray-500"><div style="display: flex; justify-content: space-between"><a onclick="openPageLocation()">Réservations.</a><a onclick="openPageReclamation()">Réclamations.</a></div></div>'
}

function alert_notification_sound() {
    var audio = document.getElementById("sound-alert")
    audio.play();
}

function alert_alert_number(number) {
    var alert = document.getElementById('alert-alert-number');
    if (number === 0) {
        alert.style.display = 'none';
        return;
    }
    alert.style.display = 'block';
    alert.innerHTML = number + '+';
}

function showInterventionParameters() {
    var toggle = document.getElementById('toggle-intervention');
    var parameters = document.getElementById('intervention-parameters');
    if (toggle.checked) {
        mode = 1
        parameters.innerHTML = `
        <input class="form-control form-control-user" type="text" 
                       id="code-ajout-interventien-utilisateur" style="margin-left: 15px" autofocus oninput=""
                       placeholder="Code Utilisateur..." >

            <input class="form-control form-control-user" type="text"  oninput=""
                   id="code-ajout-interventien-hardware" style="margin-left: 15px"
                   placeholder="Code Hardware..." >
                  <button class="btn btn-outline-primary" id="ajouter-intervention" style="margin-left: 15px" onclick="call_intervention_check_add()">Ajouter</button>
        `
    } else {
        mode = 2
        parameters.innerHTML = ''
    }
    change_scan_mode(mode)
    getScannMode(mode)
}

function change_scan_mode(mode) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', '/parameter/change-scan-mode/' + mode, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {

            } else {
                alert('Error');
            }
        }
    };
    xhr.send();
}

//window.onload = load_messages_notifications;


/*var socket = io();
socket.on('update_admin_alert', function (data) {

    load_alerts_notifications(data)
    alert_notification_sound()
});

socket.on('update_admin_message', function (data) {

    load_messages_notifications(data)
    message_notification_sound()
});

socket.on('close_admin_session', function (data) {
    user_element = document.querySelector('userdata').textContent;
    user_element = user_element.replaceAll("\'", "\"");
    user_data = JSON.parse(user_element);
    if (data.id_admin === user_data.id_admin) {

        alert("Session Fermé par l'administrateur")
        window.location.href = "/admin/logout";
    }
});*/
