var lien = "http://127.0.0.1:5000/static/";
function login() {
    console.log('login')
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email === '' || password === '') {
        alert('Please fill all fields');
        return;
    }
    login_request(email, password)
}

function login_request(email, password) {
    console.log(email, password)
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/admin/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.status === 'success') {
                window.location.href = "/dashboard/fournisseur";
            } else {
                alert('Email ou mot de passe incorrect');
            }
        }
    };
    xhr.send(JSON.stringify({email: email, password: password}));

}

function load_messages_notifications() {
    console.log('load_messages_notifications')
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/message/messages-notifications', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
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
    console.log('load_alerts_notifications')
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/message/alertes-notifications', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
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
        if (alert.type === 'reclamation')
        {
            my_reclamation = alert.reclamation
            div.innerHTML += `
                      <a class="dropdown-item d-flex align-items-center"
                                                                         href="#">
                        <div class="me-3">
                            <div class="bg-warning icon-circle"><i class="fas fa-exclamation-triangle text-white"></i></div>
                        </div>
                        <div><span class="small text-gray-500">${my_reclamation.date_reclamation}</span>
                            <p>${my_reclamation.utilisateur_reclamation.nom_utilisateur} ${my_reclamation.utilisateur_reclamation.prenom_utilisateur} ${my_reclamation.hardware_reclamation.salle_hardware.nom_salle}</p>
                        </div>
                    </a>
                       
        `;
        }
        else {
            my_location = alert.location
            div.innerHTML += `
            <a class="dropdown-item d-flex align-items-center"
                                                                         href="#">
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
    div.innerHTML += ' <a class="dropdown-item text-center small text-gray-500" onclick="openPageMessage()">Afficher Tous les Messages.</a>'
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

//window.onload = load_messages_notifications;


var socket = io();
socket.on('update_admin_alert', function (data) {
    console.log("updated alert : ", data)
    load_alerts_notifications(data)
    alert_notification_sound()
});

